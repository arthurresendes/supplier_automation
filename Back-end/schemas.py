from pydantic import BaseModel

class Envio(BaseModel):
    Admin: str
    Valor: float
    Colaborador: str
    Matricula: str