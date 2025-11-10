from sqlalchemy import Column, Integer, String, Enum
from .connection import Base # ver se nn vai dar problema por nn ter completo

import enum

class RoleEnum(str, enum.Enum):
    ADMIN = "admin"
    PRODUTOR = "produtor"
    COMPRADOR = "comprador"

class UsuarioModel(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    tipo = Column(String(20), nullable=False)  # produtor / comprador / admin
    localizacao = Column(String(100))

