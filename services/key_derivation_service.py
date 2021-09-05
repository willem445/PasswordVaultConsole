import argon2
from argon2 import PasswordHasher, Parameters, Type
from models import KeyDerivationParameters

def derive_key(password: str, salt: bytes, paramters: KeyDerivationParameters, key_size_in_bytes: int = 0):

    key_size = 0

    if key_size_in_bytes != 0:
        key_size = key_size_in_bytes
    else:
        key_size = paramters.keysize

    # ph = PasswordHasher(paramters.iterations, paramters.memory_size, paramters.degree_of_parallelism, key_size, len(salt))
    # ph.hash()
    result = argon2.low_level.hash_secret_raw(password.encode('utf-8'), salt, paramters.iterations, paramters.memory_size, paramters.degree_of_parallelism, key_size, Type.ID, 19)
    return result