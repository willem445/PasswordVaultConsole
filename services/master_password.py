import base64
from models import UserEncryptedData, MasterPasswordParameters
from .key_derivation_service import derive_key

def generate_master_hash(password: str, params):
    pass

def verify_password(password: str, salt: str, hash: str, params: MasterPasswordParameters):
    salt_bytes = base64.decodebytes(salt.encode("ascii")) 
    hash_bytes = base64.decodebytes(hash.encode("ascii")) 
    verify = derive_key(password, salt_bytes, params.key_derivation_parameters)
    return cryptographic_equals(hash_bytes, 0, verify, 0, len(hash_bytes))

def cryptographic_equals(a: bytes, a_offset: int, b: bytes, b_offset: int, length: int) -> bool:
    result = 0
    
    if (len(a) - a_offset) < length or (len(b) - b_offset) < length:
        return False

    for i in range(length):
        result = result | (a[i + a_offset] - b[i + b_offset])

    return result == 0

def flatten_hash(params):
    pass

def un_flatten_hash(hash: str) -> UserEncryptedData:
    raw = hash.split(':')
    unflattened = None

    unflattened = UserEncryptedData(
        int(raw[0]),
        int(raw[1]),
        raw[6],
        int(raw[2]),
        raw[7],
        int(raw[3]),
        int(raw[5]),
        int(raw[4]),
        None
    )

    return unflattened
