from encryption.encryption_base import Encryption

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

class Aes(Encryption):

    def __init__(self, keysize, blocksize, iterations):
        self.keysize = keysize
        self.blocksize = blocksize
        self.iterations = iterations

    def encrypt(self, plaintext, passphrase):
        pass

    def decrypt(self, ciphertext, passphrase):
        plaintext = None

        data = base64.b64decode(ciphertext)

        salt = data[0:16]
        iv = data[16:32]
        cipherbytes = data[32:48]

        password = PBKDF2(passphrase, salt, 32, 2500)

        cipher = AES.new(password, AES.MODE_CBC, IV=iv)
        byte_string = cipher.decrypt(cipherbytes)
        plaintext = unpad(byte_string, 16, 'pkcs7').decode("utf-8")

        return plaintext