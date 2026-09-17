import json
from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

load_dotenv()

# Read secret key
key = os.getenv("SECRET_KEY")

if not key:
    raise Exception("SECRET_KEY not found in .env")

cipher = Fernet(key)


# Read credentials.json
with open("data/credentials.json", "r") as file:
    data = json.load(file)


# Encrypt passwords
for user in data["user_credentials"]:

    password = user["password"]

    encrypted_password = cipher.encrypt(
        password.encode()
    ).decode()

    user["password"] = encrypted_password


# Save encrypted passwords
with open("data/credentials.json", "w") as file:
    json.dump(data, file, indent=4)


print("Passwords encrypted successfully!")