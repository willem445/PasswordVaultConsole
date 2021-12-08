from database import get_passwords_by_user_uuid
from models import Password, EncryptionParameters


def get_passwords_from_db(uuid: str, key: str):
    passwords = get_passwords_by_user_uuid(uuid)
    print(passwords)

def add_password(user_uuid: str, password: Password, key: str, params: EncryptionParameters):
    pass