import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import json
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy
from agents.graph import graph_app
from agents.llm_setup import get_llm
from langchain_community.embeddings import HuggingFaceEmbeddings
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
    
    from langchain_huggingface import HuggingFaceEmbeddings
    
    llm = get_llm()
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    print("\nRunning Ragas metrics (Faithfulness, Answer Relevancy)...")
    result = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy],
        llm=llm,
        embeddings=embeddings
    )
    
    print("\n=== EVALUATION RESULTS ===")
    print(result)
    
if __name__ == "__main__":
    run_evaluation()
