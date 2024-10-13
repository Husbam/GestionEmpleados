from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.persons import person


app= FastAPI()
# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # O usa ["*"] para permitir todas las origines
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(person)
print("Bienvenido a mi aplicacion")