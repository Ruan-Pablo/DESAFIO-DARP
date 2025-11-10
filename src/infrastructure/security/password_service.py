from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


def gerar_hash(senha: str) -> str:
    senha = str(senha)[:72]  # Garante string e corta no limite de 72 bytes
    return pwd_context.hash(senha)

def verificar_senha(senha: str, senha_hash: str) -> bool:
    senha = str(senha)[:72]
    return pwd_context.verify(senha, senha_hash)
