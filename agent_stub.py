from langgraph.graph import StateGraph
from typing import TypedDict

class AgentState(TypedDict):
    input: str
    decision: str

def classify_node(state: AgentState) -> AgentState:
    if "enrich" in state["input"]:
        state["decision"] = "enrich"
    else:
        state["decision"] = "classify"
    return state

def build_agent_graph():
    builder = StateGraph(AgentState)
    builder.add_node("classify", classify_node)
    builder.set_entry_point("classify")
    builder.set_finish_point("classify")
    return builder.compile()
