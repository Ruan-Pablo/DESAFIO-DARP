from src.domain.entities.produto import Produto
from src.domain.repositories.produto_repository import ProdutoRepository
from src.infrastructure.db.models import ProdutoModel

class ProdutoRepositoryImpl:
    def __init__(self, db):
        self.db = db

    def criar(self, produto: Produto):
        print("DEBUG - repo.criar - produto entity:", produto)
        model = ProdutoModel(
            nome=produto.nome,
            descricao=produto.descricao,
            preco=produto.preco,
            quantidade=produto.quantidade,
            categoria=produto.categoria,
            localizacao=produto.localizacao,
            produtor_id=produto.produtor_id
        )
        print("DEBUG - repo.criar - model to persist:", {
            "nome": model.nome, "categoria": model.categoria, "localizacao": model.localizacao
        })
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return Produto(
            id=model.id,
            nome=model.nome,
            descricao=model.descricao,
            preco=model.preco,
            quantidade=model.quantidade,
            categoria=model.categoria,
            localizacao=model.localizacao,
            produtor_id=model.produtor_id
        )
    
    def listar_todos(self) -> list[Produto]:
        produtos = self.db.query(ProdutoModel).all()
        return [
            Produto(
                id=p.id,
                nome=p.nome,
                descricao=p.descricao,
                preco=p.preco,
                quantidade=p.quantidade,
                categoria=p.categoria,
                localizacao=p.localizacao,
                produtor_id=p.produtor_id
            )
            for p in produtos
        ]
   

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
