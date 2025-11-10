from src.domain.entities.produto import Produto
from src.domain.repositories.produto_repository import ProdutoRepository
from src.infrastructure.db.models import ProdutoModel

class ProdutoRepositoryImpl(ProdutoRepository):
    def __init__(self, db):
        self.db = db

    def criar(self, produto: Produto) -> Produto:
        model = ProdutoModel(
            nome=produto.nome,
            descricao=produto.descricao,
            preco=produto.preco,
            quantidade=produto.quantidade,
            categoria=produto.categoria,
            localizacao=produto.localizacao,
            produtor_id=produto.produtor_id
        )
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return Produto(**model.__dict__)

    def listar_todos(self) -> list[Produto]:
        produtos = self.db.query(ProdutoModel).all()
        return [Produto(**p.__dict__) for p in produtos]

    def buscar_por_id(self, id: int) -> Produto | None:
        p = self.db.query(ProdutoModel).filter(ProdutoModel.id == id).first()
        return Produto(**p.__dict__) if p else None

    def atualizar(self, produto: Produto) -> Produto:
        model = self.db.query(ProdutoModel).filter(ProdutoModel.id == produto.id).first()
        if not model:
            return None
        model.nome = produto.nome
        model.descricao = produto.descricao
        model.preco = produto.preco
        model.quantidade = produto.quantidade
        model.categoria = produto.categoria
        model.localizacao = produto.localizacao
        self.db.commit()
        self.db.refresh(model)
        return Produto(**model.__dict__)

    def deletar(self, produto: Produto):
        model = self.db.query(ProdutoModel).filter(ProdutoModel.id == produto.id).first()
        if model:
            self.db.delete(model)
            self.db.commit()
