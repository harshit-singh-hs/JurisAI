import os
import sys
import types
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import json
from datasets import Dataset

# ragas 0.4.x imports ChatVertexAI from a module langchain-community 0.4 removed. ragas only uses
# it in an isinstance() check, so a placeholder class is enough to let ragas import.
try:
    import langchain_community.chat_models.vertexai  # noqa: F401
except ImportError:
    _vertexai_stub = types.ModuleType("langchain_community.chat_models.vertexai")
    _vertexai_stub.ChatVertexAI = type("ChatVertexAI", (), {})
    sys.modules["langchain_community.chat_models.vertexai"] = _vertexai_stub

from ragas import evaluate, RunConfig
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import faithfulness, answer_relevancy
from agents.graph import graph_app
from agents.llm_setup import get_llm
from database.chroma_setup import get_embedding_model
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

def run_evaluation():
    data_path = os.path.join(os.path.dirname(__file__), "eval_dataset.json")
    if not os.path.exists(data_path):
        print("Run generate_dataset.py first.")
        return
        
    with open(data_path, "r") as f:
        raw_data = json.load(f)
        
    eval_data = {
        "question": [],
        "answer": [],
        "contexts": [],
        "ground_truth": []
    }
    
    print("Running queries through the LangGraph AI Pipeline...")
    for i, item in enumerate(raw_data):
        print(f"Evaluating Question {i+1}: {item['question']}")
        question = item["question"]
        gt = item["ground_truth"]
        
        initial_state = {
            "query": question,
            "category": "",
            "context": [],
            "draft_response": "",
            "final_response": "",
            "needs_clarification": False
        }
        config = {"configurable": {"thread_id": f"eval_thread_{i}"}}
        result = graph_app.invoke(initial_state, config=config)
        
        eval_data["question"].append(question)
        eval_data["answer"].append(result["final_response"])
        eval_data["contexts"].append(result["context"])
        eval_data["ground_truth"].append(gt)
        
    dataset = Dataset.from_dict(eval_data)

    # Groq rejects n > 1, so have ragas send separate requests instead of asking for n completions
    llm = LangchainLLMWrapper(get_llm(), bypass_n=True)
    embeddings = get_embedding_model()
    # Groq's free-tier tokens-per-minute limit can't absorb ragas' default 16 parallel jobs;
    # run them one at a time with room for rate-limit retries
    run_config = RunConfig(max_workers=1, timeout=600)

    print("\nRunning Ragas metrics (Faithfulness, Answer Relevancy)...")
    result = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy],
        llm=llm,
        embeddings=embeddings,
        run_config=run_config
    )
    
    print("\n=== EVALUATION RESULTS ===")
    print(result)
    
if __name__ == "__main__":
    run_evaluation()
