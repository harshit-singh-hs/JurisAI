from agents.state import AgentState
from agents.llm_setup import get_llm
from langchain_core.prompts import PromptTemplate
from agents.prompts import SYSTEM_PROMPT, LONG_TERM_MEMORY_PREFIX, RAG_CONTEXT_PREFIX

def synthesizer_node(state: AgentState):
    llm = get_llm()
    query = state["query"]
    category = state.get("category", "")
    
    history_str = ""
    if state.get("chat_history"):
        history_str = "\n".join([f"{msg['role'].upper()}: {msg['content']}" for msg in state["chat_history"]])
        
    user_context = ""
    formatted_system = SYSTEM_PROMPT.format(user_context=user_context)
    
    if history_str:
        formatted_system += "\n" + LONG_TERM_MEMORY_PREFIX.format(memory_summary=history_str)
        
    if state.get("needs_clarification"):
        prompt = PromptTemplate.from_template(
            "{system_instructions}\n\n"
            "Context: The user's query is too vague to provide meaningful advice.\n"
            "Action: Politely and warmly ask the user to provide more details about their specific legal situation, contract type, or question.\n\n"
            "User Query: {query}\n\n"
            "Response:"
        )
        chain = prompt | llm
        response = chain.invoke({"system_instructions": formatted_system, "query": query})
        return {"draft_response": response.content.strip()}
        
    if category == "Casual Conversation":
        prompt = PromptTemplate.from_template(
            "{system_instructions}\n\n"
            "Context: The user is greeting you or making casual conversation.\n"
            "Action: Respond warmly and politely, and ask how you can assist them with their legal queries or contract needs today.\n\n"
            "User Query: {query}\n\n"
            "Response:"
        )
        chain = prompt | llm
        response = chain.invoke({"system_instructions": formatted_system, "query": query})
        return {"draft_response": response.content.strip()}
        
    context_str = "\n\n".join(state.get("context", []))
    if context_str:
        formatted_system += "\n" + RAG_CONTEXT_PREFIX.format(rag_context=context_str)
        
    prompt = PromptTemplate.from_template(
        "{system_instructions}\n\n"
        "Context: The user is asking a legal query or requesting contract drafting/review assistance. Provide a detailed, accurate, step-by-step response based on the relevant legal material or your pre-trained legal knowledge.\n\n"
        "User Query: {query}\n\n"
        "Response:"
    )
    
    chain = prompt | llm
    response = chain.invoke({"system_instructions": formatted_system, "query": query})
    
    return {"draft_response": response.content.strip()}
