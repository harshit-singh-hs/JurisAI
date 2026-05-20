from agents.state import AgentState
from agents.llm_setup import get_llm
from langchain_core.prompts import PromptTemplate

def intake_node(state: AgentState):
    llm = get_llm()
    query = state["query"]
    
    prompt = PromptTemplate.from_template(
        "You are an expert intake specialist for a legal advisory firm specializing in Indian, Business, and Contract Law.\n\n"
        "Your task is to analyze the user's query and classify it into exactly ONE of the following categories:\n"
        "- 'Contract Drafting': User wants to create/draft a contract, agreement, NDA, will, or deed.\n"
        "- 'Contract Review': User wants to analyze, review, explain, or check an existing contract/agreement.\n"
        "- 'General Legal Question': User is asking a legal question about a law, procedure, right, or compliance (e.g. buying land, GST, Article 14, criminal complaint, bail).\n"
        "- 'Casual Conversation': User is saying hello, greeting you, thanking you, or making general small talk (e.g. 'hello', 'hi', 'how are you', 'thanks').\n"
        "- 'Unclear': The user's query is too vague, short, or ambiguous to understand what legal topic they need help with (e.g. 'help me', 'what', 'law').\n\n"
        "Rules:\n"
        "1. Prioritize 'Casual Conversation' for all greetings and casual messages.\n"
        "2. If the query asks about a specific legal concept (like a fundamental right, land transaction, ROC, court filing), classify it as 'General Legal Question'.\n"
        "3. Respond with ONLY the exact category name from the list. Do not include any punctuation, quotes, or explanatory text.\n\n"
        "User Query: {query}\n\n"
        "Category:"
    )
    
    chain = prompt | llm
    response = chain.invoke({"query": query})
    category_raw = response.content.strip().lower()
    
    # Robust normalization to map LLM response to one of the strict categories
    if "casual" in category_raw or "conversation" in category_raw:
        category = "Casual Conversation"
    elif "drafting" in category_raw or "draft" in category_raw:
        category = "Contract Drafting"
    elif "review" in category_raw:
        category = "Contract Review"
    elif "general" in category_raw or "question" in category_raw or "legal" in category_raw:
        category = "General Legal Question"
    else:
        category = "Unclear"
        
    needs_clarification = category == "Unclear"
    
    return {"category": category, "needs_clarification": needs_clarification}
