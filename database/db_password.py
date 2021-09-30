from database import connection, entity
from datetime import datetime
from sqlalchemy import extract  
from sqlalchemy import or_
from models import Password
from typing import List, Dict

def get_passwords_by_user_uuid(user_uuid: str):
    session, engine = connection.get_engine()
    entity.Base.metadata.create_all(engine)
    passwords = session.query(entity.PasswordDB).filter_by(
            UserUuid=user_uuid
            ).all()
    session.close()
    return passwords
