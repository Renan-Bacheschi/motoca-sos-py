from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from app.database.connection import engine
from app.schemas.usuario import Usuario, UsuarioCreate
from app.schemas.moto import Moto

app = FastAPI(title="Moto Express API")


def get_session():
    with Session(engine) as session:
        yield session

@app.get("/motos")
def listar_motos(session: Session = Depends(get_session)):
    motos = session.exec(select(Moto)).all()
    return motos
@app.get("/usuarios")
def listar_usuarios(session: Session = Depends(get_session)):
    return session.exec(select(Usuario)).all()


@app.post("/usuarios", response_model=Usuario)
def cadastrar_usuario(usuario_data: UsuarioCreate, session: Session = Depends(get_session)):
    novo_usuario = Usuario.model_validate(usuario_data)

    # 2. Ciclo de persistência
    session.add(novo_usuario)  # Adiciona
    session.commit()  # Grava no banco de verdade
    session.refresh(novo_usuario)  # get o ID gerado pelo banco

    return novo_usuario