from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Тест GET всех узлов
def test_get_all_nodes():
    response = client.get("/nodes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Тест GET узла и его связей
def test_get_node_with_relationships():
    response = client.get("/nodes/123")
    assert response.status_code == 200

# Тест POST с токеном
def test_post_node_with_auth():
    headers = {"Authorization": "Bearer your_secret_token"}
    response = client.post("/nodes", json={"node": {"id": "1", "label": "User"}}, headers=headers)
    assert response.status_code == 200
    assert response.json()["message"] == "Node and relationships added"

# Тест DELETE с токеном
def test_delete_node_with_auth():
    headers = {"Authorization": "Bearer your_secret_token"}
    response = client.delete("/nodes/1", headers=headers)
    assert response.status_code == 200
