from sqlalchemy import Column, Integer, String, Enum
from .connection import Base # ver se nn vai dar problema por nn ter completo
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
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



class ProdutoModel(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(500))
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)
    categoria = Column(String(100), nullable=False)
    localizacao = Column(String(100))
    produtor_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    produtor = relationship("UsuarioModel", backref="produtos")
