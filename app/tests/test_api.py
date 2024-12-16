import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import UserNode, GroupNode

client = TestClient(app)

# Тестовые данные
test_node = {
    "node": {
        "vk_id": 1,
        "name": "Test User",
        "screen_name": "testuser",
        "sex": 2,
        "city": "Test City"
    },
    "relationships": [
        {"type": "FOLLOWS", "target_id": 2},
        {"type": "SUBSCRIBES", "target_id": 3}
    ]
}

AUTH_TOKEN = "Bearer your_secret_token"

# Фикстура для создания тестовых данных
@pytest.fixture
def create_test_data():
    user = UserNode(vk_id=1, name="Test User", screen_name="testuser", sex=2, city="Test City").save()
    group = GroupNode(vk_id=2, name="Test Group", screen_name="testgroup").save()
    user.subscriptions.connect(group)
    return user, group

# Фикстура для заголовков авторизации
@pytest.fixture
def auth_headers():
    return {"Authorization": AUTH_TOKEN}


# Тест GET всех узлов
def test_get_all_nodes(create_test_data):
    response = client.get("/nodes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Тест GET узла и его связей
def test_get_node_with_relationships(create_test_data):
    response = client.get("/nodes/1")  # Используем vk_id=1
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "n" in data[0]  # Проверяем, что возвращается информация об узле
    assert "r" in data[0]  # Проверяем, что возвращаются связи


# Тест POST с токеном авторизации
def test_post_node_with_auth(auth_headers):
    response = client.post("/nodes", json=test_node, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["message"] == "Node and relationships added"


# Тест POST без токена авторизации
def test_post_node_without_auth():
    response = client.post("/nodes", json=test_node)
    assert response.status_code == 401
    assert response.json()["detail"] == "Unauthorized"


# Тест DELETE узла с токеном авторизации
def test_delete_node_with_auth(auth_headers, create_test_data):
    node_id = 1  # Удаляем тестовый узел
    response = client.delete(f"/nodes/{node_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["message"] == f"Node {node_id} and its relationships deleted"


# Тест DELETE узла без токена авторизации
def test_delete_node_without_auth():
    node_id = 1
    response = client.delete(f"/nodes/{node_id}")
    assert response.status_code == 401
    assert response.json()["detail"] == "Unauthorized"
