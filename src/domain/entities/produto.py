from dataclasses import dataclass

@dataclass
class Produto:
    id: int | None
    nome: str
    descricao: str | None
    preco: float
    quantidade: int
    categoria: str
    localizacao: str | None
    produtor_id: int
