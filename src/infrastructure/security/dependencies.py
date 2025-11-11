from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from src.infrastructure.security.jwt_service import SECRET_KEY, ALGORITHM
from src.infrastructure.db.connection import get_db
from src.infrastructure.repositories.usuario_repository_impl import UsuarioRepositoryImpl

# Middleware de autenticação simples com Bearer
oauth2_scheme = HTTPBearer()

def get_current_user(
    token: HTTPAuthorizationCredentials = Depends(oauth2_scheme),
    db = Depends(get_db)
):
    cred_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido ou ausente",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # 👇 Aqui está o detalhe: pega o token real
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise cred_exc
    except JWTError:
        raise cred_exc

    repo = UsuarioRepositoryImpl(db)
    user = repo.buscar_por_email(email)
    if user is None:
        raise cred_exc
    return user
