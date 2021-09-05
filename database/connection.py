import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import sys
from .config import SQLITE_DB_PATH


def get_engine():
    return GetSQLiteEngine(SQLITE_DB_PATH)


def GetSQLiteEngine(dbFilePath):
    engine = create_engine('sqlite:///{}'.format(dbFilePath))
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    return (session, engine)
