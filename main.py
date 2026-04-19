from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "API Taller Mecánico funcionando"}

clientes = []

@app.get("/clientes")
def obtener_clientes():
    return clientes

@app.post("/clientes")
def crear_cliente(cliente: dict):
    clientes.append(cliente)
    return {"mensaje": "Cliente creado"}

from fastapi import FastAPI
from rutas import clientes, vehiculos, ordenes, servicios

app = FastAPI()

app.include_router(clientes.router, prefix="/clientes")
app.include_router(vehiculos.router, prefix="/vehiculos")
app.include_router(ordenes.router, prefix="/ordenes")
app.include_router(servicios.router, prefix="/servicios")