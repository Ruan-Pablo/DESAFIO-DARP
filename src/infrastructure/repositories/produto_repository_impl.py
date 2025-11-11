from src.domain.entities.produto import Produto
from src.domain.repositories.produto_repository import ProdutoRepository
from src.infrastructure.db.models import ProdutoModel

class ProdutoRepositoryImpl:
    def __init__(self, db):
        self.db = db

    def criar(self, produto: Produto):
        # 1️⃣ Converte a entidade de domínio em modelo ORM
        model = ProdutoModel(
            nome=produto.nome,
            descricao=produto.descricao,
            preco=produto.preco,
            quantidade=produto.quantidade,
            produtor_id=produto.produtor_id,
        )

        # 2️⃣ Salva no banco
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        # 3️⃣ Converte de volta para entidade de domínio
        return Produto(
            id=model.id,
            nome=model.nome,
            descricao=model.descricao,
            preco=model.preco,
            quantidade=model.quantidade,
            produtor_id=model.produtor_id,
        )
    
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
