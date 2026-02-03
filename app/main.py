from fastapi import FastAPI, Depends, HTTPException, Request
from sqlmodel import Session, select
from app.database.connection import engine
from app.schemas.usuario import Usuario, UsuarioCreate, UsuarioBase
from app.schemas.moto import  MotoCreate, MotoBase, Moto
from app.logger_config import setup_app_logger
from starlette.responses import JSONResponse

app = FastAPI(title="Moto Express API")

logger = setup_app_logger()

@app.middleware("http")
async def log_errors_middleware(request: Request, call_next):
    try:
        return  await call_next(request)
    except Exception as e:
        # arquivo log para aonde os erros serao inseridos caso exista
        logger.exception(f"Erro Crítico na rota: {request.url.path}")

        return JSONResponse(
            status_code=500,
            content={"Detalhes": "Erro interno no servidor. verifique as logs system."}
        )



def get_session():
    with Session(engine) as session:
        yield session

@app.get("/motos")
def listar_motos(session: Session = Depends(get_session)):
    motos = session.exec(select(MotoBase)).all()
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

@app.post("/motos", response_model=Moto)
def cadastrar_moto(moto_data: MotoCreate, session: Session = Depends(get_session)):
    nova_moto = Moto.model_validate(moto_data)
    session.add(nova_moto)
    session.commit()
    session.refresh(nova_moto)
    return nova_moto