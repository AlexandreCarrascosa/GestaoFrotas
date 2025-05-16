from pydantic import BaseModel

class Reserva(BaseModel):
    placa: str
    solicitante: str
    motorista: str
    motivo: str
    gestor: str
    data_retirada: str
    hora_retirada: str
    data_devolucao: str
    hora_devolucao: str
