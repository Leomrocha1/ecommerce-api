from curses import KEY_MARK
import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text, Float

from ecommerce_carros import db

Base = db.Model


class Carros(Base):
    __tablename__ = 'carros'
    id = Column(Integer, primary_key=True, nullable=False)
    marca = Column(String(128), nullable=False)
    modelo = Column(String(128), nullable=False)
    ano_fabricacao = Column(Integer, nullable=False)
    ano_modelo = Column(Integer, nullable=False)
    km = Column(Integer, nullable=False)
    cambio = Column(String(128), nullable=False)
    combustivel = Column(String(128), nullable=False)
    cor = Column(String(128), nullable=False)
    valor = Column(Float, nullable=False)
    descricao = Column(Text, nullable=False)
    criado_em = Column(DateTime(), nullable=False, default=datetime.datetime.utcnow)