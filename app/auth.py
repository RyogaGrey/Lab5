import os
from dotenv import load_dotenv

load_dotenv()
SECRET_TOKEN = os.getenv("SECRET_TOKEN")

def verify_token(token: str):
    return token == f"Bearer {SECRET_TOKEN}"
