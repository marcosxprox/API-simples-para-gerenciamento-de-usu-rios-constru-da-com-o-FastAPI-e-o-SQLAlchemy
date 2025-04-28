from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})
session_local = sessionmaker(autocommit = False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

