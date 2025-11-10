from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from src.infrastructure.security.jwt_service import SECRET_KEY, ALGORITHM
from src.infrastructure.db.connection import get_db
from src.infrastructure.repositories.usuario_repository_impl import UsuarioRepositoryImpl

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    cred_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
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

