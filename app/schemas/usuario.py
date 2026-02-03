from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from typing import Optional

# Base, Campos que existem em ambos
class UsuarioBase(SQLModel):
    nome: str
    sobrenome: str
    email: EmailStr = Field(unique=True, index=True)


# Entrada: (inclui senha, mas não o ID)
class UsuarioCreate(UsuarioBase):
    senha: str

# Banco: (Contém tudo + id) final para inserção
class Usuario(UsuarioBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    senha: str