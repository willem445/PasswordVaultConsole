

class User(object):

    def __init__(self, unique_id: str, encrypted_key: str, username: str, hash, firstname: str, lastname: str, phone_number: str, email: str, sw_version: str, valid_user: bool = False, plaintext_random_key: str = None, plaintext_password: str = None):
        self.unique_id = unique_id
        self.encrypted_key = encrypted_key
        self.username = username
        self.hash = hash
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        self.email = email
        self.sw_version = sw_version
        self.valid_user = valid_user
        self.plaintext_random_key = plaintext_random_key
        self.plaintext_password = plaintext_password
