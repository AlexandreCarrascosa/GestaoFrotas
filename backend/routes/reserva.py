from fastapi import APIRouter
from models.reserva_model import Reserva
from services.sheets_service import salvar_reserva

router = APIRouter()

@router.post("/reserva")
def criar_reserva(reserva: Reserva):
    salvar_reserva(reserva)
    return {"status": "ok", "mensagem": "Reserva criada com sucesso"}
