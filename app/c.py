import secrets

# Генерация случайного ключа длиной 32 символа
secret_key = secrets.token_hex(32)
print(f"Ваш Secret Key: {secret_key}")
