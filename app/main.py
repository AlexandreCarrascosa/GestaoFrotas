from fastapi import FastAPI
from app.routes import reserva
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS para permitir chamadas do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou coloque o domínio específico
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(reserva.router, prefix="/api")
