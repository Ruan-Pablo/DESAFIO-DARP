from pydantic import BaseModel, constr, conint, confloat

class CriarProdutoInput(BaseModel):
    nome: constr(min_length=3, max_length=100)
    descricao: str | None = None
    preco: confloat(gt=0)
    quantidade: conint(ge=0)
    categoria: constr(min_length=3, max_length=100)
    localizacao: str | None = None

class ProdutoOutput(BaseModel):
    id: int
    nome: str
    preco: float
    quantidade: int
    categoria: str
    localizacao: str | None = None
    produtor_id: int
