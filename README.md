# DESAFIO-DARP
Aqui conterá os detalhes da aplicação desenvolvida para atender o desafio da Darp.

# Decisões arquiteturais

Clean Arquiteture + Repository Pattern

# Tecnologias utilizadas

- Framework: FastAPI
- ORM: SQLAlchemy ORM
- Arquitetura: Clean Architecture (Domain / Application / Infrastructure / Interface)
- Padrões: Repository Pattern 
- Auth: JWT (python-jose) + bcrypt (passlib) para senhas
- Validação e DTOs: Pydantic
- Migrations SQLAlchemy: alembic
- Documentação: Swagger automático do FastAPI (/docs)
- Docker: Dockerfile + docker-compose.yml (Postgres + app)

# Dependencias
- Ambiente virtual python: venv

Para instalar as dependencias utilize `pip install`

```
pip install fastapi uvicorn sqlalchemy psycopg2-binary
pip install python-jose[cryptography] passlib[bcrypt]
pip install pydantic email-validator
pip install alembic
pip install python-dotenv
```
### Explicando as dependências:

| Lib | Função |
| --- | --- |
| **fastapi** | Framework principal (rotas, validações, docs automáticas) |
| **uvicorn** | Servidor ASGI |
| **sqlalchemy** | ORM oficial para banco de dados |
| **psycopg2-binary** | Driver PostgreSQL |
| **python-jose** | Geração e validação de tokens JWT |
| **passlib[bcrypt]** | Criptografia de senhas |
| **pydantic** | Validação e tipagem de dados (DTOs) |
| **email-validator** | Validação automática de e-mails |
| **alembic** | Migrations do banco |
| **python-dotenv** | Ler variáveis de ambiente (.env) |

### Executando
```uvicorn main:app --reload```

## Fluxo de comunicação
```
[ Interface (controllers) ]
        ↓
[ Application (use cases) ]
        ↓
[ Domain (interfaces, entidades) ]
        ↓
[ Infrastructure (implementações concretas) ]
```

## Descrição do desafio
Link: [Descrição do desafio](descrição.md)