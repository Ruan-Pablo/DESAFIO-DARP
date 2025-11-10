from pydantic import BaseModel, EmailStr, constr
from src.domain.entities.usuario import TipoUsuario

class RegistrarUsuarioInput(BaseModel):
    nome: constr(min_length=3)
    email: EmailStr
    senha: constr(min_length=8)
    tipo: TipoUsuario  # <-- restrito ao enum
    localizacao: str | None = None

class LoginInput(BaseModel):
    email: EmailStr
    senha: str

class TokenOutput(BaseModel):
    access_token: str
    token_type: str = "bearer"
