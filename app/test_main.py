import pytest
from app.main import app, todos


@pytest.fixture
def client():
    app.config["TESTING"] = True
    todos.clear()
    with app.test_client() as c:
        yield c


def test_get_todos_empty(client):
    res = client.get("/todos")
    assert res.status_code == 200
    assert res.get_json() == []


def test_add_todo(client):
    res = client.post("/todos", json={"task": "Buy milk"})
    assert res.status_code == 201
    assert res.get_json()["task"] == "Buy milk"


def test_todo_appears_after_creation(client):
    client.post("/todos", json={"task": "Buy milk"})
    res = client.get("/todos")
    assert len(res.get_json()) == 1


def test_generated_fields(client):
    res = client.post("/todos", json={"task": "Buy milk"})
    data = res.get_json()
    assert "id" in data
    assert "done" in data
    assert data["done"] is False


def test_invalid_request(client):
    res = client.post("/todos", json={})
    assert res.status_code == 400