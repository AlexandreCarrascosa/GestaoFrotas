import requests
from app.models.reserva_model import Reserva

GOOGLE_SHEET_URL = "https://script.google.com/macros/s/AKfycbx_vJldHQLqcyKouHDYzvmXl6mJSjXihzFiu_8q7FdYsSj90pa9f5zb0Z4xWrNQOGs1aA/exec"

def salvar_reserva(reserva: Reserva):
    data = reserva.dict()
    response = requests.post(GOOGLE_SHEET_URL, json=data)  # Enviando como x-www-form-urlencoded

    if response.status_code != 200:
        raise Exception("Erro ao salvar no Google Sheets")

def gerar_mensagem_whatsapp(reserva: Reserva) -> str:
    return f"""🛻Reserva de Veiculo 🛻

PLACA - {reserva.placa}

Solicitante: {reserva.solicitante}
Motorista: {reserva.motorista}
Motivo: {reserva.motivo}
Gestor Responsável : {reserva.gestor}

Data da Retirada: {reserva.data_retirada}
Hora da Retirada: {reserva.hora_retirada}

Data da Devolução: {reserva.data_devolucao}
Hora da Devolução: {reserva.hora_devolucao}
"""
