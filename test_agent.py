from agent_stub import build_agent_graph

def test_classify_agent_classify():
    graph = build_agent_graph()
    result = graph.invoke({"input": "run classification"})
    assert result["decision"] == "classify"

def test_classify_agent_enrich():
    graph = build_agent_graph()
    result = graph.invoke({"input": "please enrich this"})
    assert result["decision"] == "enrich"
