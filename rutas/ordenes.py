from fastapi import APIRouter
from modelos import Orden

router = APIRouter()

ordenes = []

@router.get("/")
def obtener_ordenes():
    return ordenes

@router.get("/{id}")
def obtener_orden(id: int):
    return ordenes[id]

@router.post("/")
def crear_orden(orden: Orden):
    ordenes.append(orden)
    return {"mensaje": "Orden creada"}

@router.put("/{id}")
def actualizar_orden(id: int, orden: Orden):
    ordenes[id] = orden
    return {"mensaje": "Orden actualizada"}

@router.delete("/{id}")
def eliminar_orden(id: int):
    ordenes.pop(id)
    return {"mensaje": "Orden eliminada"}