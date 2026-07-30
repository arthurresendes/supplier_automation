from pydantic import BaseModel

class Envio(BaseModel):
    Solicitante: str
    Valor: float
    Colaborador: str
    Matricula: int