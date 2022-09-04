from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from app_controle_gastos.backend.DB.connection import RegistroDB

_, engine = RegistroDB.get_connection()
Base = declarative_base()


class Pessoa(Base):
    ...