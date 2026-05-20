from agents.state import AgentState
from agents.llm_setup import get_llm
from langchain_core.prompts import PromptTemplate

def synthesizer_node(state: AgentState):
    llm = get_llm()
    query = state["query"]
    category = state.get("category", "")
    
    history_str = ""
    if state.get("chat_history"):
        history_str = "\n".join([f"{msg['role'].upper()}: {msg['content']}" for msg in state["chat_history"]])
 
    if state.get("needs_clarification"):
        prompt = PromptTemplate.from_template(
            "You are a friendly and professional AI Legal Advisor. The user asked a vague legal question. "
            "Politely and warmly ask them to provide more details about their legal situation or the contract they are asking about.\n\n"
            "Previous Conversation:\n{history}\n\n"
            "User Query: {query}\n\n"
            "Response:"
        )
        chain = prompt | llm
        response = chain.invoke({"query": query, "history": history_str})
        return {"draft_response": response.content.strip()}
 
    if category == "Casual Conversation":
        prompt = PromptTemplate.from_template(
            "You are a friendly, helpful, and conversational AI Legal Advisor specializing in Business and Contract Law. "
            "The user is making casual conversation or greeting you. Respond politely and warmly, and ask how you can help them with their legal needs today.\n\n"
            "Previous Conversation:\n{history}\n\n"
            "User Query: {query}\n\n"
            "Response:"
        )
        chain = prompt | llm
        response = chain.invoke({"query": query, "history": history_str})
        return {"draft_response": response.content.strip()}
 
    context_str = "\n\n".join(state.get("context", []))
    prompt = PromptTemplate.from_template(
        "You are an expert, conversational, and human-like AI Legal Advisor. You have access to both specific context documents "
        "and a comprehensive, pre-trained knowledge of legal proceedings, business law, property transactions, and general jurisprudence.\n\n"
        "Instructions:\n"
        "1. Prioritize answering based on the provided Context Documents if they contain relevant info (such as terms of specific contracts, NDAs, or employment letters).\n"
        "2. If the context documents do not cover the user's query (e.g. if the question is a general legal topic like 'how to buy land', 'filing a lawsuit', 'court proceedings', 'starting a business'), "
        "draw upon your extensive pre-trained legal knowledge to provide a detailed, accurate, and step-by-step professional response.\n"
        "3. Write in a natural, conversational, structured (using markdown headers/bullet points), and approachable tone while maintaining professional legal standards.\n"
        "4. Citing References: When explaining a law, rule, or contract clause, cite the relevant section or article *selectively* and *only when directly needed* (e.g., 'Section 138 of the Negotiable Instruments Act' or 'Article 21 of the Constitution'). Do not over-clutter every sentence with citations; keep the response clean and natural.\n"
        "5. Conversational Follow-up: Conclude your response by naturally weaving 1 or 2 relevant follow-up questions into your final paragraph. Do not create a separate, robotic bulleted list of questions under a heading. Instead, ask these questions as a natural extension of your advice (e.g., asking about their specific jurisdiction, whether they've already taken initial steps, or if they have key documents on hand) to keep the conversation interactive, natural, and human-like.\n\n"
        "Context Documents:\n{context}\n\n"
        "Previous Conversation:\n{history}\n\n"
        "User Query: {query}\n\n"
        "Response:"
    )
    
    chain = prompt | llm
    response = chain.invoke({"query": query, "context": context_str, "history": history_str})
    
    return {"draft_response": response.content.strip()}
