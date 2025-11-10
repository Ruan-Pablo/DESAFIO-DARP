from fastapi import FastAPI
from src.infrastructure.db.connection import Base, engine
from src.infrastructure.db import models
from src.interface.api import auth_controller, produto_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Marketplace Agro API")

app.include_router(auth_controller.router)
app.include_router(produto_controller.router)

@app.get("/")
def root():
    return {"message": "🚜 API Marketplace Agro funcionando!"}
