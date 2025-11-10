from src.infrastructure.security.password_service import verificar_senha
from src.infrastructure.security.jwt_service import criar_token

class LoginUseCase:
    def __init__(self, usuario_repository):
        self.usuario_repository = usuario_repository

    def execute(self, dados):
        usuario = self.usuario_repository.buscar_por_email(dados.email)
        if not usuario or not verificar_senha(dados.senha, usuario.senha_hash):
            raise ValueError("Credenciais inválidas.")
        token = criar_token({"sub": usuario.email, "tipo": usuario.tipo})
        return token
