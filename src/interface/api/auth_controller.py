from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.infrastructure.db.connection import get_db
from src.infrastructure.repositories.usuario_repository_impl import UsuarioRepositoryImpl
from src.application.dtos.auth_dto import RegistrarUsuarioInput, LoginInput, TokenOutput
from src.application.use_cases.registrar_usuario_use_case import RegistrarUsuarioUseCase
from src.application.use_cases.login_use_case import LoginUseCase

router = APIRouter(prefix="/auth", tags=["Autenticação"])

@router.post("/register")
def registrar_usuario(dados: RegistrarUsuarioInput, db: Session = Depends(get_db)):
    repo = UsuarioRepositoryImpl(db)
    use_case = RegistrarUsuarioUseCase(repo)
    try:
        usuario = use_case.execute(dados)
        return {"id": usuario.id, "email": usuario.email, "tipo": usuario.tipo}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=TokenOutput)
def login(dados: LoginInput, db: Session = Depends(get_db)):
    repo = UsuarioRepositoryImpl(db)
    use_case = LoginUseCase(repo)
    try:
        token = use_case.execute(dados)
        return TokenOutput(access_token=token)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
