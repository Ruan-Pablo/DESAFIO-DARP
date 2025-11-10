# DESAFIO-DARP
Aqui conterá os detalhes da aplicação desenvolvida para atender o desafio da Darp. Infelizmente não está completa.

# Decisões arquiteturais

Clean Arquiteture + Repository Pattern

## Estrutura de pastas da Clean Arquiteture
```
src/
├─ domain/ → Entidades e interfaces (regras de negócio puras)
│ ├─ entities/ → Classes de domínio (Usuario, Produto)
│ └─ repositories/ → Interfaces dos repositórios
│
├─ application/ → Casos de uso (regras de aplicação)
│ ├─ dtos/ → Modelos de entrada e saída (Pydantic)
│ └─ use_cases/ → Lógica de aplicação (login, registro, CRUD)
│
├─ infrastructure/ → Implementações técnicas (banco, segurança)
│ ├─ db/ → Conexão e modelos SQLAlchemy
│ ├─ repositories/ → Implementações concretas dos repositórios
│ └─ security/ → JWT, hash e dependências
│
├─ interface/ → Camada de entrada (controllers FastAPI)
│ └─ api/ → Endpoints RESTful
│
└─ main.py → Ponto de entrada da aplicação
```

# Tecnologias utilizadas
- Linguagem: Python 3.11
- Framework: FastAPI
- ORM: SQLAlchemy ORM
- Arquitetura: Clean Architecture (Domain / Application / Infrastructure / Interface)
- Padrões: Repository Pattern 
- Auth: JWT (python-jose) + bcrypt (passlib) para senhas
- Validação e DTOs: Pydantic
- Migrations SQLAlchemy: alembic
- Documentação: Swagger automático do FastAPI (/docs)

# Dependencias
- Ambiente virtual python: venv

Para instalar as dependencias utilize `pip install`

```
pip install fastapi uvicorn sqlalchemy psycopg2-binary
pip install python-jose passlib
pip install pydantic 
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
| **passlib[pbkdf2_sha256]** | Criptografia de senhas |
| **pydantic** | Validação e tipagem de dados (DTOs) |
| **alembic** | Migrations do banco |
| **python-dotenv** | Ler variáveis de ambiente (.env) |

> As dependencias estão em [requirements.txt](requirements.txt)
```
pip install -r requirements.txt
```


Para executar

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