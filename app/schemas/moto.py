from sqlmodel import SQLModel, Field
from typing import Optional


class Moto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    marca: str
    modelo: str
    ano_modelo: str

    usuario_id:  int = Field(foreign_key="usuario_id")
