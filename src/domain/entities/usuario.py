from dataclasses import dataclass
from enum import Enum

class TipoUsuario(str, Enum):
    PRODUTOR = "produtor"
    COMPRADOR = "comprador"
    ADMIN = "admin"

@dataclass
class Usuario:
    id: int | None
    nome: str
    email: str
    senha_hash: str
    tipo: TipoUsuario
    localizacao: str | None = None
