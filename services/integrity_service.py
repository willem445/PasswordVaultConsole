import hmac
from models import Mac

def generate_integrity_hash(mac: Mac, key: bytes, suite_bytes: bytes, salt_bytes: bytes, iv_bytes: bytes, cipher_bytes: bytes):
    pass

def verify_integrity(mac: Mac, key: bytes, cipher: bytes, salt_size_bits: int, iv_size_bits: int, block_size_bits: int, header_size_bits: int) -> bool:
    pass

def get_hmac_hash_size_in_bits(mac: Mac):
    pass

def get_hmac_key_size_in_bits(mac: Mac):
    pass