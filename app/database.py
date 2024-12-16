from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

def db_connection():
    uri = os.getenv("NEO4J_URI")
    user = os.getenv("NEO4J_USER")
    password = os.getenv("NEO4J_PASSWORD")
    driver = GraphDatabase.driver(uri, auth=(user, password))
    return driver.session()
