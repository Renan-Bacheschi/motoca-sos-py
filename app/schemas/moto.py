from sqlalchemy import table
from sqlmodel import SQLModel, Field
from typing import Optional


class MotoBase(SQLModel):
    marca: str
    modelo: str
    ano_modelo: str

class MotoCreate(MotoBase):
    usuario_id: int

class Moto(MotoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    usuario_id: Optional[int] = Field(default=None, foreign_key="usuario.id")

