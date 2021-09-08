

def cryptographic_equals(a: bytes, a_offset: int, b: bytes, b_offset: int, length: int) -> bool:
    result = 0
    
    if (len(a) - a_offset) < length or (len(b) - b_offset) < length:
        return False

    for i in range(length):
        result = result | (a[i + a_offset] - b[i + b_offset])

    return result == 0


def to_num_bytes(num_bits: int):
    num_bytes = num_bits / 8
    return num_bytes

def to_num_bits(num_bytes: int):
    num_bits = num_bytes * 8
    return num_bits
    