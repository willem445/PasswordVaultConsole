# https://pycryptodome.readthedocs.io/en/latest
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
from .key_derivation_service import derive_key
from enum import IntEnum
from models import Mac, CipherSuite, KeyDerivationParameters
from .integrity_service import get_hmac_hash_size_in_bits, get_hmac_key_size_in_bits
from utilities import to_num_bytes

class PackedCipherSuiteParametersIndex(IntEnum):
    EncryptionAlgorithmIndex = 0,
    KDFAlgorithmIndex=1,
    KDFInterationsIndex=2,
    KDFMemoryIndex=6,
    KDFParallelizationIndex=10,
    MACAlgorithmIndex=11,
    KDFSaltSizeIndex=12,
    IVSizeIndex=13,
    NumCipherSuiteParameterBytes=14



def encrypt(plaintext, passphrase):

    # TODO - generate key with argon2id
    key = get_random_bytes(16)
    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

def decrypt(ciphertext, passphrase):
    plaintext = None
    cipher_raw = base64.decodebytes(ciphertext.encode("ascii")) 

    enc_alg, mac_alg, kdf_alg, kdf_itr, kdf_mem, kdf_par = unpack_cipher_params(cipher_raw)
    salt_size_bytes, iv_size_bytes = unpack_salt_iv_size(cipher_raw)

    header_size_in_bytes = int(PackedCipherSuiteParametersIndex.NumCipherSuiteParameterBytes)
    auth_size_in_bytes = int(to_num_bytes(get_hmac_hash_size_in_bits(mac_alg)))
    hmac_size_in_bytes = int(to_num_bytes(get_hmac_key_size_in_bits(mac_alg)))
    block_size_in_bytes = 16 # 128 bits for AES               
    key_size_in_bytes = int(get_keysize_from_cipher_raw(enc_alg))

    auth_offset = header_size_in_bytes
    salt_offset = auth_offset + auth_size_in_bytes
    iv_offset = salt_offset + salt_size_bytes
    cipher_offset = iv_offset + iv_size_bytes
    cipher_length = len(cipher_raw) - cipher_offset
    min_len = cipher_offset + block_size_in_bytes

    salt = cipher_raw[salt_offset: salt_offset+salt_size_bytes]
    
    kdf_params = KeyDerivationParameters(kdf_alg, 0, salt_size_bytes, kdf_itr, kdf_par, kdf_mem)
    combined_key = derive_key(passphrase, salt, kdf_params, key_size_in_bytes + hmac_size_in_bytes)
    cipher_key = combined_key[0: key_size_in_bytes]
    hmac_key = combined_key[key_size_in_bytes : key_size_in_bytes+key_size_in_bytes]

    # authenticate




    # cipher = AES.new(key, AES.MODE_CBC)
    # cipher.iv = None


    return plaintext


def unpack_cipher_params(cipher_raw: bytes):
    
    enc_alg = cipher_raw[PackedCipherSuiteParametersIndex.EncryptionAlgorithmIndex]
    mac_alg = cipher_raw[PackedCipherSuiteParametersIndex.MACAlgorithmIndex]
    kdf_alg = cipher_raw[PackedCipherSuiteParametersIndex.KDFAlgorithmIndex]
    kdf_itr = (cipher_raw[PackedCipherSuiteParametersIndex.KDFInterationsIndex + 3] << 24) | (cipher_raw[PackedCipherSuiteParametersIndex.KDFInterationsIndex + 2] << 16) | (cipher_raw[PackedCipherSuiteParametersIndex.KDFInterationsIndex + 1] << 8) | (cipher_raw[PackedCipherSuiteParametersIndex.KDFInterationsIndex + 0] << 0) 
    kdf_mem = (cipher_raw[PackedCipherSuiteParametersIndex.KDFMemoryIndex + 3] << 24) | (cipher_raw[PackedCipherSuiteParametersIndex.KDFMemoryIndex + 2] << 16) | (cipher_raw[PackedCipherSuiteParametersIndex.KDFMemoryIndex + 1] << 8) | (cipher_raw[PackedCipherSuiteParametersIndex.KDFMemoryIndex + 0] << 0) 
    kdf_par = cipher_raw[PackedCipherSuiteParametersIndex.KDFParallelizationIndex]

    return (enc_alg, mac_alg, kdf_alg, kdf_itr, kdf_mem, kdf_par)

def unpack_salt_iv_size(cipher_raw: bytes):
    salt_size_bytes = cipher_raw[PackedCipherSuiteParametersIndex.KDFSaltSizeIndex]
    iv_size_bytes = cipher_raw[PackedCipherSuiteParametersIndex.IVSizeIndex]

    return (salt_size_bytes, iv_size_bytes)

def get_keysize_from_cipher_raw(suite: CipherSuite):
    size_bytes = None

    if suite in [CipherSuite.Aes128CbcPkcs7, CipherSuite.Rijndael128CbcPkcs7, CipherSuite.Aes128CbcPkcs7]:
        size_bytes = 16
    elif suite in [CipherSuite.Aes256CfbPkcs7, CipherSuite.Rijndael256CbcPkcs7, CipherSuite.Aes256CbcPkcs7]:
        size_bytes = 32

    return size_bytes


