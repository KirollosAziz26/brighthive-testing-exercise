from langgraph.graph import StateGraph
from typing import TypedDict

class AgentState(TypedDict):
    input: str
    decision: str
    classification_type: str

def classify_node(state: AgentState) -> AgentState:
    if "enrich" in state["input"]:
        state["decision"] = "enrich"
    else:
        state["decision"] = "classify"
    return state

def post_classify_node(state: AgentState) -> AgentState:
    if "critical" in state["input"]:
        state["classification_type"] = "critical"
    else:
        state["classification_type"] = "normal"
    return state

def build_agent_graph():
    builder = StateGraph(AgentState)
    builder.add_node("classify", classify_node)
    builder.add_node("post_classify", post_classify_node)

    def classify_router(state: AgentState) -> str:
        if state["decision"] == "classify":
            return "post_classify"
        else:
            return "__end__"

    builder.add_conditional_edges("classify", classify_router)
    builder.set_entry_point("classify")
    builder.set_finish_point("post_classify")

    return builder.compile()