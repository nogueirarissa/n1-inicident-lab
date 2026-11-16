from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True)
    valor = Column(Integer, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    # ⚠️ lazy loading padrão = problema N+1 quando iteramos sobre N pedidos
    cliente = relationship("Cliente")