import os

from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine

from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL1")

def get_session():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    return Session(engine)

