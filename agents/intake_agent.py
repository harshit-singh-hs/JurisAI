from agents.state import AgentState
from agents.llm_setup import get_llm
from langchain_core.prompts import PromptTemplate

def intake_node(state: AgentState):
    llm = get_llm()
    query = state["query"]
    
    prompt = PromptTemplate.from_template(
        "You are an intake specialist for a legal advisory firm specializing in Business and Contract Law. "
        "Analyze the user's query and categorize it into one of the following: "
        "'Contract Drafting', 'Contract Review', 'General Legal Question', 'Casual Conversation', 'Unclear'. "
        "If the user is saying hello, greeting you, or making casual conversation, categorize it as 'Casual Conversation'. "
        "If the query is a legal question but too vague to provide meaningful advice, categorize it as 'Unclear'.\n\n"
        "User Query: {query}\n\n"
        "Category (respond with ONLY the category name):"
    )
    
    chain = prompt | llm
    response = chain.invoke({"query": query})
    category = response.content.strip().replace("'", "").replace('"', '')
    
    needs_clarification = category == "Unclear"
    
    return {"category": category, "needs_clarification": needs_clarification}
