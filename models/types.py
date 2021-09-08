from enum import IntEnum


class Mac(IntEnum):
    Unknown = 0,
    HMACSHA256 = 1,
    HMACSHA512 = 2

class CipherSuite(IntEnum):
    Unknown = 0,
    Aes256CfbPkcs7 = 1,
    Aes128CfbPkcs7 = 2,
    Rijndael256CbcPkcs7 = 3,
    Rijndael128CbcPkcs7 = 4,
    Aes256CbcPkcs7 = 5,
    Aes128CbcPkcs7 = 6,

class KeyDerivationAlgorithm(IntEnum):
    Argon2Id = 0,
    Pbkdf2 = 1,


class AuthenticateResult(IntEnum):
    PasswordIncorrect = 0,
    UsernameDoesNotExist = 1,
    Successful = 2,
    Failed = 3

class LogoutResult(IntEnum):
    Success = 1,
    Failed = 2


class UserEncryptedData(object):

    def __init__(self, alg: KeyDerivationAlgorithm, keysize: int, salt: str, saltsize: int, hash: str, iterations: int, degree_of_parallelism: int, memory_size: int, random_gen_key: str):
        self.alg = alg
        self.keysize = keysize
        self.salt = salt
        self.saltsize = saltsize
        self.hash = hash
        self.iterations = iterations
        self.degree_of_parallelism = degree_of_parallelism
        self.memory_size = memory_size
        self.random_gen_key = random_gen_key

class KeyDerivationParameters(object):

    def __init__(self, alg: KeyDerivationAlgorithm, keysize: int, saltsize: int, iterations: int, degree_of_parallelism: int, memory_size: int):
        self.alg = alg
        self.keysize = keysize
        self.saltsize = saltsize
        self.iterations = iterations
        self.degree_of_parallelism = degree_of_parallelism
        self.memory_size = memory_size

class MasterPasswordParameters(object):

    def __init__(self, key_derivation_parameters: KeyDerivationParameters, random_keysize: int):
        self.key_derivation_parameters = key_derivation_parameters
        self.random_keysize = random_keysize
