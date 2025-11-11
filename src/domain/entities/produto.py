from dataclasses import dataclass
from typing import Optional
@dataclass
class Produto:
    
    nome: str
    descricao: str | None
    preco: float
    quantidade: int
    categoria: str
    localizacao: str | None
    produtor_id: int | None
    id: Optional[int] = None
