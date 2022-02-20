from cryptography.fernet import Fernet
from decouple import config


def encrypt(source):
    key = config('ENCRYPT_PASSWORD')
    return Fernet(key).encrypt(source)


def decrypt(source):
    key = config('ENCRYPT_PASSWORD')
    return Fernet(key).decrypt(source)
