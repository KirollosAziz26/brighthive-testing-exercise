import pytest
from agent_stub import build_agent_graph

@pytest.mark.parametrize("input_text,expected_decision,expected_type", [
    ("please enrich this data", "enrich", None),
    ("this is a critical classification", "classify", "critical"),
    ("normal classification required", "classify", "normal"),
])
def test_agent_with_additional_node(input_text, expected_decision, expected_type):
    graph = build_agent_graph()
    result = graph.invoke({"input": input_text})
    assert result["decision"] == expected_decision
    if expected_type:
        assert result["classification_type"] == expected_type
    else:
        assert "classification_type" not in result

def test_agent_missing_input_key():
    graph = build_agent_graph()
    with pytest.raises(KeyError):
        graph.invoke({})