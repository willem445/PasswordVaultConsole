import hmac
from models import Mac
from Crypto.Hash import HMAC, SHA256, SHA512
from utilities import to_num_bytes, cryptographic_equals

def generate_integrity_hash(mac: Mac, key: bytes, suite_bytes: bytes, salt_bytes: bytes, iv_bytes: bytes, cipher_bytes: bytes):
    auth = get_hmac(mac, key)
    auth.update(suite_bytes)
    auth.update(salt_bytes)
    auth.update(iv_bytes)
    auth.update(cipher_bytes)
    n = 2
    out = [(auth.hexdigest()[i:i+n]) for i in range(0, len(auth.hexdigest()), n)]
    out = [int(out[i], 16) for i in range(0, len(out))]
    return out

def verify_integrity(mac: Mac, key: bytes, cipher: bytes, salt_size_bytes: int, iv_size_bytes: int, block_size_bytes: int, header_size_bytes: int) -> bool:
    auth = get_hmac(mac, key)
    auth_size_bytes = to_num_bytes(get_hmac_hash_size_in_bits(mac))

    auth_offset = int(header_size_bytes)
    salt_offset = int(auth_offset + auth_size_bytes)
    iv_offset = int(salt_offset + salt_size_bytes)
    cipher_offset = int(iv_offset + iv_size_bytes)
    cipher_len = int(len(cipher) - cipher_offset)
    min_len = int(cipher_offset + block_size_bytes)

    if (len(cipher) < min_len):
        raise Exception()

    auth.update(cipher[0:header_size_bytes])
    auth.update(cipher[salt_offset:salt_offset+salt_size_bytes])
    auth.update(cipher[iv_offset:iv_offset+iv_size_bytes])
    auth.update(cipher[cipher_offset:cipher_offset+cipher_len])
    n = 2
    out = [(auth.hexdigest()[i:i+n]) for i in range(0, len(auth.hexdigest()), n)]
    out = [int(out[i], 16) for i in range(0, len(out))]
    return cryptographic_equals(bytes(out), 0, cipher, auth_offset, auth_size_bytes)

def get_hmac(mac: Mac, hmac_key: bytes):
    digest = None
    if mac == Mac.HMACSHA256:
        digest = SHA256
    elif mac == Mac.HMACSHA512:
        digest = SHA512
    else:
        raise Exception("Invalid MAC type!")

    return HMAC.new(hmac_key, digestmod=digest)


def get_hmac_hash_size_in_bits(mac: Mac):
    if mac == Mac.HMACSHA256:
        return 256
    elif mac == Mac.HMACSHA512:
        return 512
    else:
        raise Exception("Invalid MAC type!")

def get_hmac_key_size_in_bits(mac: Mac):
    if mac == Mac.HMACSHA256:
        return 256
    elif mac == Mac.HMACSHA512:
        return 512
    else:
        raise Exception("Invalid MAC type!")
        