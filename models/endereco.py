from sqlalchemy import Table, Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from repository.banco_de_dados import Base
from sqlalchemy.ext.declarative import declarative_base
from cliente import Cliente

Base = declarative_base()

class Endereco(Base):
    __tablename__= 'endereco'
    id = Column('id', Integer, autoincrement=True, primary_key=True)
    cep = Column('cep', String(12), nullable=False)
    logradouro = Column('logradouro', String(12), nullable=False)
    bairro = Column('bairro', String(12), nullable=False)
    cidade = Column('cidade', String(12), nullable=False)
    estado = Column('estado', String(2), nullable=False)
    pais = Column('pais', String(30), nullable=False)
    clientes = relationship("Cliente", back_populates="endereco")

