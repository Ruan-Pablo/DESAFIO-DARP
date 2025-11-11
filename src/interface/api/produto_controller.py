from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.infrastructure.db.connection import get_db
from src.infrastructure.repositories.produto_repository_impl import ProdutoRepositoryImpl
from src.infrastructure.security.dependencies import get_current_user
from src.application.dtos.produto_dto import CriarProdutoInputDTO, ProdutoOutputDTO
from src.application.use_cases.criar_produto_use_case import CriarProdutoUseCase
from src.application.use_cases.listar_produtos_use_case import ListarProdutosUseCase

router = APIRouter(prefix="/produtos", tags=["Produtos"])
"""
{
  "nome": "Teste",
  "descricao": "lorem ipsum",
  "preco": 1,
  "quantidade": 1,
  "categoria": "teste",
  "localizacao": "teste"
}
"""
@router.post("/", response_model=ProdutoOutputDTO)
def criar_produto(
    dados: CriarProdutoInputDTO,
    db: Session = Depends(get_db),
    usuario = Depends(get_current_user)
):
    if usuario.tipo != "produtor":
        raise HTTPException(status_code=403, detail="Apenas produtores podem criar produtos.")
    print("DEBUG - criar_produto - dados:", dados.dict())
    print("DEBUG - criar_produto - usuario:", {"id": usuario.id, "tipo": usuario.tipo})
    repo = ProdutoRepositoryImpl(db)
    use_case = CriarProdutoUseCase(repo)
    produto = use_case.execute(dados, produtor_id=usuario.id)
    return produto

@router.get("/", response_model=list[ProdutoOutputDTO])
def listar_produtos(db: Session = Depends(get_db)):
    repo = ProdutoRepositoryImpl(db)
    use_case = ListarProdutosUseCase(repo)
    return use_case.execute()
