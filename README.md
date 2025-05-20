

## 📄 Automated Testing Engineer - Take-Home Exercise

### Welcome!

At **Brighthive**, we build an AI Agent Data Workspace designed to orchestrate and evaluate agentic workflows and datasets across the AI stack. This exercise evaluates your skills in **automated testing** for both the **SaaS layer** and the **Agent (LangGraph) layer**.

---

### 🧪 Your Task

You will write **automated tests** for:

1. A simplified **SaaS layer** API (provided as `api_stub.py`)
2. A minimal **LangGraph-based agent** that makes decisions based on structured input (provided as `agent_stub.py`)

---

### 📁 Files Provided

* `api_stub.py` — A FastAPI app simulating a basic Brighthive-style API.
* `agent_stub.py` — A toy LangGraph with a decision-making agent node.
* `test_api.py` — Add your API tests here using `pytest` and `httpx`.
* `test_agent.py` — Add your LangGraph tests here.
* `conftest.py` — Shared fixtures (optional use).
* `README.md` — This file.

---

### 🔧 Setup Instructions

```bash
git clone https://github.com/your-org/brighthive-testing-exercise.git
cd brighthive-testing-exercise
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
```

---

### 🧠 What We’re Looking For

| Area                     | Expectation                                                                |
| ------------------------ | -------------------------------------------------------------------------- |
| **Test Design**          | Clear, isolated, well-named, logically grouped tests                       |
| **Coverage**             | Includes both **unit** and **integration** level tests                     |
| **Edge Case Thinking**   | Handles error cases, unexpected inputs, and state transitions              |
| **LangGraph Validation** | Simulates realistic agent inputs and asserts correct node behavior/outputs |
| **Use of Tools**         | Good use of `pytest`, `httpx`, and LangGraph’s testing patterns            |
| **Documentation**        | Tests are readable, intention-revealing, and include brief inline comments |
| **Bonus Points**         | Use of parameterization, mocking external calls, or custom fixtures        |

---

### 🧪 Sample Tasks

#### For the SaaS Layer (`test_api.py`)

* Test happy path: creating and retrieving a dataset via the API
* Test failure path: posting malformed input or missing fields
* Test auth enforcement (mocking token validation logic)
* Test edge case: large payload or conflicting names

#### For the Agent Layer (`test_agent.py`)

* Feed the agent input with known outcomes, assert state transitions
* Test fallback or error paths in LangGraph node logic
* Validate outputs (e.g., emitted actions, updates) for decision correctness
* Simulate agent looping or multi-node scenarios

---

### 🧩 Stretch Challenge (Optional)

* Extend the agent with one extra decision node (e.g., classify vs. enrich) and write tests for that
* Use `pytest-xdist` for parallel test execution and note performance gains in a comment

---

## 🏁 Submission

Please submit a **GitHub repo link** or a **zipped folder** with your test files, with clear commit history or changelog notes if applicable.

---

### 💡 Evaluation Criteria (Summary)

* ✅ Functional coverage of both SaaS and LangGraph layers
* 🧠 Thoughtful edge case handling
* 📚 Readability and documentation of test logic
* 🧪 Effective use of testing tools
* 🚀 Optional: Extension of agent graph logic or advanced tooling

---

## 🐍 Included Files (Stubs)

Here are simplified versions of the files:

---

### `api_stub.py`

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()
db: Dict[str, dict] = {}

class Dataset(BaseModel):
    name: str
    description: str

@app.post("/datasets")
def create_dataset(dataset: Dataset):
    if dataset.name in db:
        raise HTTPException(status_code=400, detail="Dataset already exists")
    db[dataset.name] = dataset.dict()
    return dataset

@app.get("/datasets/{name}")
def get_dataset(name: str):
    if name not in db:
        raise HTTPException(status_code=404, detail="Not found")
    return db[name]
```

---

### `agent_stub.py`

```python
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
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
    builder.set_finish_point("classify")  # single-node for simplicity
    return builder.compile()
```


