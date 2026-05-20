from typing import TypedDict, List, Annotated
import operator

class AgentState(TypedDict):
    query: str
    chat_history: Annotated[List[dict], operator.add]
    category: str
    context: List[str]
    draft_response: str
    final_response: str
    needs_clarification: bool
