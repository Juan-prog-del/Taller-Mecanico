# modulo  clientes activos

from fastapi import APIRouter
from modelos import Cliente

router = APIRouter()

clientes = []

@router.get("/")
def obtener_clientes():
    return clientes

@router.post("/")
def crear_cliente(cliente: Cliente):
    clientes.append(cliente)
    return {"mensaje": "Cliente creado"}