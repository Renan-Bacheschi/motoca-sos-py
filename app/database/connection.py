import os
from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv # cofre libs
from app.schemas.usuario import Usuario
from app.schemas.usuario import UsuarioCreate
from app.schemas.usuario import UsuarioBase
from app.schemas.moto import MotoBase, MotoCreate, Moto

# Carrega as variáveis do arquivo .env
load_dotenv()

# senha protegida
postgres_url = os.getenv("DATABASE_URL")

# Segurança EXTRA
if not postgres_url:
    raise ValueError("A variável DATABASE_URL não foi encontrada no arquivo .env")

engine = create_engine(postgres_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session