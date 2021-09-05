# https://pycryptodome.readthedocs.io/en/latest
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt(plaintext, passphrase):

    # TODO - generate key with argon2id
    key = get_random_bytes(16)
    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

def decrypt(ciphertext, passphrase):
    pass
