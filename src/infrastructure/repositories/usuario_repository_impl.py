from src.domain.entities.usuario import Usuario
from src.domain.repositories.usuario_repository import UsuarioRepository
from src.infrastructure.db.models import UsuarioModel

class UsuarioRepositoryImpl(UsuarioRepository):
    def __init__(self, db):
        self.db = db

    def criar(self, usuario: Usuario) -> Usuario:
        model = UsuarioModel(
            nome=usuario.nome,
            email=usuario.email,
            senha_hash=usuario.senha_hash,
            tipo=usuario.tipo,
            localizacao=usuario.localizacao
        )
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return Usuario(
            id=model.id,
            nome=model.nome,
            email=model.email,
            senha_hash=model.senha_hash,
            tipo=model.tipo,
            localizacao=model.localizacao
        )

    def buscar_por_email(self, email: str) -> Usuario | None:
        model = self.db.query(UsuarioModel).filter(UsuarioModel.email == email).first()
        if not model:
            return None
        return Usuario(
            id=model.id,
            nome=model.nome,
            email=model.email,
            senha_hash=model.senha_hash,
            tipo=model.tipo,
            localizacao=model.localizacao
        )
