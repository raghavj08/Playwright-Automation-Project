from cryptography.fernet import Fernet
import os

from dotenv import load_dotenv


def decrypt_password(encrypted_password):

    # Read secret key
    load_dotenv()

    # Read secret key
    key = os.getenv("SECRET_KEY")

    if not key:
        raise Exception("SECRET_KEY not found in .env")

    cipher = Fernet(key)

    # Decrypt password
    password = cipher.decrypt(
        encrypted_password.encode()
    ).decode()

    return password