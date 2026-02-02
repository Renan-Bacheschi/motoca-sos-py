from fastapi import FastAPI
from app.database.connection import create_db_and_tables

app = FastAPI(title="Moto Express")

@app.on_event("startup")
def on_startup():
    print("Tentando conectar ao banco e criar tabelas...")
    create_db_and_tables()
    print("✅ Sucesso!")

@app.get("/")
def read_root():
    return {"status": "Online", "database": "Conectado"}