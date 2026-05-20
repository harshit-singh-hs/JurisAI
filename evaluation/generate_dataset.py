import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ingestion.document_loader import load_documents, split_documents
from agents.llm_setup import get_llm
from langchain_core.prompts import PromptTemplate
import json
import re

def generate_test_data():
    documents = load_documents()
    chunks = split_documents(documents)
    llm = get_llm()
    
    prompt = PromptTemplate.from_template(
        "Generate a realistic user question based on the following legal text, and extract the exact ground truth answer from the text.\n\n"
        "Text: {text}\n\n"
        "Output format as valid JSON only, no markdown formatting:\n"
        "{{\n"
        "  \"question\": \"The generated question\",\n"
        "  \"ground_truth\": \"The exact answer based on the text\"\n"
        "}}"
    )
    
    chain = prompt | llm
    
    dataset = []
    print("Generating synthetic questions from chunks...")
    for i, chunk in enumerate(chunks[:2]): # Generate 2 questions for quick eval
        try:
            print(f"Processing chunk {i+1}...")
            res = chain.invoke({"text": chunk.page_content})
            
            # Simple json extraction
            match = re.search(r'\{.*\}', res.content.replace('\n', ''), re.DOTALL)
            if match:
                data = json.loads(match.group())
                data["context"] = chunk.page_content
                dataset.append(data)
            else:
                print("Could not extract JSON.")
        except Exception as e:
            print("Failed to generate for a chunk:", e)
            
    out_path = os.path.join(os.path.dirname(__file__), "eval_dataset.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(dataset, f, indent=2)
    print(f"Generated {len(dataset)} evaluation pairs in {out_path}")

if __name__ == "__main__":
    generate_test_data()
