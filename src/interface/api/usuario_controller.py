from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.infrastructure.db.connection import get_db
from src.infrastructure.repositories.usuario_repository_impl import UsuarioRepositoryImpl
from src.application.dtos.auth_dto import RegistrarUsuarioInput, LoginInput, TokenOutput
from src.application.use_cases.listar_usuarios_use_case import ListarUsuariosUseCase
from src.application.use_cases.login_use_case import LoginUseCase

router = APIRouter(prefix="/user", tags=["Usuarios"])

@router.get("/listarUsuario")
def listar_usuario(db: Session = Depends(get_db)):
    repo = UsuarioRepositoryImpl(db)
    use_case = ListarUsuariosUseCase(repo)
    try:
        return use_case.execute()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
