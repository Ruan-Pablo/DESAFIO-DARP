
class ListarProdutosUseCase:
    def __init__(self, produto_repository):
        self.produto_repository = produto_repository

    def execute(self):
        return self.produto_repository.listar_todos()
