from src.domain.entities.usuario import Usuario
from src.infrastructure.security.password_service import gerar_hash

class RegistrarUsuarioUseCase:
    def __init__(self, usuario_repository):
        self.usuario_repository = usuario_repository

    def execute(self, dados):
        if self.usuario_repository.buscar_por_email(dados.email):
            raise ValueError("Email já cadastrado.")
        senha_hash = gerar_hash(dados.senha)
        novo_usuario = Usuario(
            id=None,
            nome=dados.nome,
            email=dados.email,
            senha_hash=senha_hash,
            tipo=dados.tipo,
            localizacao=dados.localizacao
        )
        return self.usuario_repository.criar(novo_usuario)
