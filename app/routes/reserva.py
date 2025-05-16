from fastapi import APIRouter
from app.models.reserva_model import Reserva
from app.services.sheets_service import salvar_reserva, gerar_mensagem_whatsapp

router = APIRouter()

@router.post("/reserva")
def criar_reserva(reserva: Reserva):
    salvar_reserva(reserva)
    mensagem = gerar_mensagem_whatsapp(reserva)
    return {"mensagem_whatsapp": mensagem}
