from agents.state import AgentState

def reviewer_node(state: AgentState):
    draft = state["draft_response"]
    final_response = draft
    
    new_history = [{"role": "user", "content": state["query"]}, {"role": "ai", "content": final_response}]
    
    return {"final_response": final_response, "chat_history": new_history}
