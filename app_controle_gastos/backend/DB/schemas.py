from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
                    ForeignKey, Column, Integer,
                    String, Date, Boolean
                )
from app_controle_gastos.backend.DB.connection import RegistroDB

_, engine = RegistroDB.get_connection()
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    address_id = Column(Integer, ForeignKey('address.id'))
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    cpf = Column(String(11), nullable=False)
    email = Column(String(200))
    birthDate = Column(Date)

    person_address = relationship('Address', back_populates='address_person')
    person_user = relationship('User', back_populates='person')


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    cep = Column(String(8), nullable=False)
    address_cep = Column(String(150), nullable=False)
    complement = Column(String(100))
    district = Column(String(30))
    locale = Column(String(40), nullable=False)
    uf = Column(String(50), nullable=False)
    isHouse = Column(Boolean, nullable=False)
    isApartment = Column(Boolean, nullable=False)

    address_person = relationship('Person', back_populates='address')

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    username = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)

    user_person = relationship('Person', back_populates='person_user')


Base.metadata.create_all(bind=engine)
