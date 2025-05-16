import requests

url = "https://script.google.com/macros/s/AKfycbx_vJldHQLqcyKouHDYzvmXl6mJSjXihzFiu_8q7FdYsSj90pa9f5zb0Z4xWrNQOGs1aA/exec"

data = {
    "placa": "TCJ0C68",
    "solicitante": "Jeferson",
    "motorista": "Jeferson",
    "motivo": "Consultoria",
    "gestor": "Leandro",
    "data_retirada": "2025-05-16",
    "hora_retirada": "08:00",
    "data_devolucao": "2025-05-16",
    "hora_devolucao": "18:00"
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Resposta:", response.text)