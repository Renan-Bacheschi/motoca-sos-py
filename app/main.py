from fastapi import FastAPI
from fastapi.params import Depends
from sqlmodel import SQLModel, Session, select
from app.database.connection import engine
from app.schemas.usuario import Usuario
from app.schemas.moto import Moto

app = FastAPI(title="Motoca-SOS-TESTE-GET")

def get_session():
    with Session(engine) as session:
        yield session

@app.get("/")
def home():
    return {"mensagem": "Motoca Rodandooooo! La ele"}

@app.get("/usuarios")
def listar_usuarios(session: Session = Depends(get_session)):
    usuarios = session.exec(select(Usuario)).all()

    return usuarios