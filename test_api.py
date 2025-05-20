import pytest
from fastapi.testclient import TestClient
from api_stub import app

client = TestClient(app)

def test_create_dataset():
    response = client.post("/datasets", json={"name": "Test", "description": "A test dataset"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test"

def test_duplicate_dataset():
    client.post("/datasets", json={"name": "Test", "description": "First"})
    response = client.post("/datasets", json={"name": "Test", "description": "Duplicate"})
    assert response.status_code == 400

def test_get_dataset():
    client.post("/datasets", json={"name": "Retrieve", "description": "Test"})
    response = client.get("/datasets/Retrieve")
    assert response.status_code == 200
    assert response.json()["description"] == "Test"

def test_missing_dataset():
    response = client.get("/datasets/Missing")
    assert response.status_code == 404
