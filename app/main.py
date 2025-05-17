from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routes import reserva

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota da API
app.include_router(reserva.router, prefix="/api")

# Static files (CSS/JS)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Templates (HTML)
templates = Jinja2Templates(directory="frontend")

# Página principal
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
