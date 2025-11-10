from abc import ABC, abstractmethod
from src.domain.entities.usuario import Usuario

class UsuarioRepository(ABC):
    @abstractmethod
    def criar(self, usuario: Usuario) -> Usuario:
        pass

    @abstractmethod
    def buscar_por_email(self, email: str) -> Usuario | None:
        pass
