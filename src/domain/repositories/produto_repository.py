from abc import ABC, abstractmethod
from src.domain.entities.produto import Produto

class ProdutoRepository(ABC):
    @abstractmethod
    def criar(self, produto: Produto) -> Produto:
        pass

    @abstractmethod
    def listar_todos(self) -> list[Produto]:
        pass

    @abstractmethod
    def buscar_por_id(self, id: int) -> Produto | None:
        pass

    @abstractmethod
    def atualizar(self, produto: Produto) -> Produto:
        pass

    @abstractmethod
    def deletar(self, produto: Produto):
        pass
