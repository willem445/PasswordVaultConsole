

def cryptographic_equals(a: bytes, a_offset: int, b: bytes, b_offset: int, length: int) -> bool:
    result = 0
    
    if (len(a) - a_offset) < length or (len(b) - b_offset) < length:
        return False

    for i in range(length):
        result = result | (a[i + a_offset] - b[i + b_offset])

    return result == 0