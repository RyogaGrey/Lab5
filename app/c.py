from neomodel import config, db

config.DATABASE_URL = "bolt://neo4j:your_password@localhost:7687"

try:
    db.cypher_query("RETURN 1")
    print("Connected to Neo4j!")
except Exception as e:
    print(f"Connection failed: {e}")
