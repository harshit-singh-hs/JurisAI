import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from agents.state import AgentState
from database.hybrid_search import get_ensemble_retriever

def researcher_node(state: AgentState):
    if state.get("needs_clarification"):
        return {"context": []}
        
    query = state["query"]
    retriever = get_ensemble_retriever()
    
    # Retrieve top 3 relevant documents
    docs = retriever.invoke(query)
    context = [doc.page_content for doc in docs]
    
    return {"context": context}
