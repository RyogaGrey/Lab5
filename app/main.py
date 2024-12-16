from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Graph API with Neo4j", version="1.0.0")

# Подключение маршрутов
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Graph API is running. Use /docs for Swagger UI."}
