from database import get_passwords_by_user_uuid

def get_passwords_from_db(uuid: str, key: str):
    passwords = get_passwords_by_user_uuid(uuid)
    print(passwords)