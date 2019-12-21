from abc import ABC, abstractmethod

class Encryption(ABC):

    @abstractmethod
    def __init__(self, keysize, blocksize, iterations):
        pass

    @abstractmethod
    def encrypt(self, plaintext, passphrase):
        pass

    @abstractmethod
    def decrypt(self, ciphertext, passphrase):
        pass