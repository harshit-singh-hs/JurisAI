import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from langgraph.graph import StateGraph, END
from agents.state import AgentState
from agents.intake_agent import intake_node
from agents.researcher_agent import researcher_node
from agents.synthesizer_agent import synthesizer_node
from agents.reviewer_agent import reviewer_node
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

def build_graph():
    workflow = StateGraph(AgentState)
    
    workflow.add_node("intake", intake_node)
    workflow.add_node("researcher", researcher_node)
    workflow.add_node("synthesizer", synthesizer_node)
    workflow.add_node("reviewer", reviewer_node)
    
    workflow.set_entry_point("intake")
    workflow.add_edge("intake", "researcher")
    workflow.add_edge("researcher", "synthesizer")
    workflow.add_edge("synthesizer", "reviewer")
    workflow.add_edge("reviewer", END)
    
    if os.environ.get("VERCEL"):
        db_path = "/tmp/checkpoints.sqlite"
    else:
        os.makedirs(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data"), exist_ok=True)
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "checkpoints.sqlite")
    
    conn = sqlite3.connect(db_path, check_same_thread=False)
    memory = SqliteSaver(conn)
    
    return workflow.compile(checkpointer=memory)

graph_app = build_graph()
