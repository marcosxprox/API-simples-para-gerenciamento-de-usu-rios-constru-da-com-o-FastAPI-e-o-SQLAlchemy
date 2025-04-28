from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(String(36), primary_key=True, index=True)
    nome = Column(String(255), index=True)
    idade = Column(Integer)
    email = Column(String(255), unique=True, index=True)
