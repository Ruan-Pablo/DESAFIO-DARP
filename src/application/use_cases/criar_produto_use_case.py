from src.domain.entities.produto import Produto

class CriarProdutoUseCase:
    def __init__(self, produto_repository):
        self.produto_repository = produto_repository

    def execute(self, dados, produtor_id: int):
        novo = Produto(
            nome=dados.nome,
            descricao=dados.descricao,
            preco=dados.preco,
            quantidade=dados.quantidade,
            categoria=dados.categoria,
            localizacao=dados.localizacao,
            produtor_id=produtor_id,
        )

        return self.produto_repository.criar(novo)
