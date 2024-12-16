from fastapi import APIRouter, Depends, HTTPException, Header
from app.models import UserNode, GroupNode
from app.database import db_connection
from app.auth import verify_token

router = APIRouter()

# Защищённые точки POST и DELETE
def get_token(authorization: str = Header(...)):
    if not verify_token(authorization):
        raise HTTPException(status_code=401, detail="Unauthorized")

# GET: всех узлов
@router.get("/nodes", summary="Получить все узлы")
def get_all_nodes():
    query = """
    MATCH (n) 
    RETURN n.id AS id, labels(n) AS label
    """
    results = db_connection().run(query)
    return [record for record in results]

# GET: узел и все его связи
@router.get("/nodes/{node_id}", summary="Получить узел и его связи")
def get_node_with_relationships(node_id: str):
    query = """
    MATCH (n {id: $node_id})-[r]->(m)
    RETURN n, r, m
    """
    results = db_connection().run(query, node_id=node_id)
    return [record for record in results]

# POST: добавить узел и связи
@router.post("/nodes", summary="Добавить узел и связи", dependencies=[Depends(get_token)])
def add_node_and_relationships(data: dict):
    # Пример структуры data: {"node": {"id": "123", "label": "User", "name": "John"}, "relationships": [...]}
    # Логика добавления узлов и связей в Neo4j
    return {"message": "Node and relationships added"}

# DELETE: удалить узел и связи
@router.delete("/nodes/{node_id}", summary="Удалить узел и связи", dependencies=[Depends(get_token)])
def delete_node_and_relationships(node_id: str):
    query = """
    MATCH (n {id: $node_id}) DETACH DELETE n
    """
    db_connection().run(query, node_id=node_id)
    return {"message": f"Node {node_id} and its relationships deleted"}
