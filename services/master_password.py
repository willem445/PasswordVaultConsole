import base64
from models import UserEncryptedData, MasterPasswordParameters
from .key_derivation_service import derive_key
from utilities import cryptographic_equals


def generate_master_hash(password: str, params):
    pass

def verify_password(password: str, salt: str, hash: str, params: MasterPasswordParameters):
    salt_bytes = base64.decodebytes(salt.encode("ascii")) 
    hash_bytes = base64.decodebytes(hash.encode("ascii")) 
    verify = derive_key(password, salt_bytes, params.key_derivation_parameters)
    return cryptographic_equals(hash_bytes, 0, verify, 0, len(hash_bytes))

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
