from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from typing import Optional

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    sobrenome: str
    email: EmailStr = Field(unique=True, index=True )
    senha: str

