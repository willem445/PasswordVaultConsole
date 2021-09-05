from database import connection, entity
from datetime import datetime
from sqlalchemy import extract  
from sqlalchemy import or_
from models import User
from typing import List, Dict

def get_user_names()->List[str]:
    session, engine = connection.get_engine()
    entity.Base.metadata.create_all(engine)
    dbnames = session.query(entity.UserDB).all()
    names = []
    for name in dbnames:
        names.append(name.Username)
    session.close()
    return names

def get_user(username) -> User:
    session, engine = connection.get_engine()
    entity.Base.metadata.create_all(engine)
    user = session.query(entity.UserDB).filter_by(
            Username=username
            ).first()
            
    if user is None:
        return None

    return User(user.Uuid,
                user.EncryptedKey,
                user.Username,
                user.Hash,
                user.FirstName,
                user.LastName, 
                user.PhoneNumber,
                user.Email,
                user.SwVersion)

