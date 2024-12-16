Данный проект представляет собой REST API с использованием FastAPI для работы с графовой базой данных Neo4j. API предоставляет возможности работы с узлами (пользователями и группами) и их связями.

---

# Установка и запуск проекта

1. Убедитесь, что Neo4j установлен и запущен.
   - По умолчанию Neo4j доступен на `bolt://localhost:7687`.
   - Настройте логин и пароль в файле `.env`.

2. Клонируйте репозиторий и перейдите в его директорию:
   ```
   git clone <ссылка на репозиторий>
   cd <имя папки>
   ```

3. Установите зависимости:
   ```
   python -m venv .venv
   source .venv/bin/activate   # Для Linux/macOS
   .venv\Scripts\activate      # Для Windows
   pip install -r requirements.txt
   ```

4. Запустите сервер:
   ```
   python -m app.main
   ```

   API будет доступен по адресу: `http://localhost:8000`.

---

# Тестирование

Для запуска тестов используйте команду:
```
pytest
```

---

# Примеры API-запросов

### GET всех узлов
```
GET /nodes
```

### GET узла и его связей
```
GET /nodes/{node_id}
```

### POST добавление узла и связей
```
POST /nodes
Headers: { "Authorization": "Bearer <ваш токен>" }
Body:
{
    "node": {
        "vk_id": 1,
        "name": "Test User",
        "screen_name": "testuser",
        "sex": 2,
        "city": "Test City"
    },
    "relationships": [
        { "type": "FOLLOWS", "target_id": 2 },
        { "type": "SUBSCRIBES", "target_id": 3 }
    ]
}
```

### DELETE удаление узла и его связей
```
DELETE /nodes/{node_id}
Headers: { "Authorization": "Bearer <ваш токен>" }
```

---

# Конфигурация

Настройки хранятся в файле `.env`. Пример:
```
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password
SECRET_TOKEN=your_secret_token
```

---

# Структура проекта

```
app/
├── main.py        # Точка входа
├── routes.py      # Маршруты API
├── models.py      # Модели для работы с Neo4j
├── auth.py        # Функции аутентификации
└── tests/
    └── test_api.py  # Тесты
```
