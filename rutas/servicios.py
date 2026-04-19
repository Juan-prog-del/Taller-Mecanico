from fastapi import APIRouter
from modelos import Servicio

router = APIRouter()

servicios = []

@router.get("/")
def obtener_servicios():
    return servicios

@router.get("/{id}")
def obtener_servicio(id: int):
    return servicios[id]

@router.post("/")
def crear_servicio(servicio: Servicio):
    servicios.append(servicio)
    return {"mensaje": "Servicio creado"}

@router.put("/{id}")
def actualizar_servicio(id: int, servicio: Servicio):
    servicios[id] = servicio
    return {"mensaje": "Servicio actualizado"}

@router.delete("/{id}")
def eliminar_servicio(id: int):
    servicios.pop(id)
    return {"mensaje": "Servicio eliminado"}