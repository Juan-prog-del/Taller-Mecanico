from fastapi import APIRouter
from modelos import Vehiculo

router = APIRouter()

vehiculos = []

@router.get("/")
def obtener_vehiculos():
    return vehiculos

@router.get("/{id}")
def obtener_vehiculo(id: int):
    return vehiculos[id]

@router.post("/")
def crear_vehiculo(vehiculo: Vehiculo):
    vehiculos.append(vehiculo)
    return {"mensaje": "Vehículo creado"}

@router.put("/{id}")
def actualizar_vehiculo(id: int, vehiculo: Vehiculo):
    vehiculos[id] = vehiculo
    return {"mensaje": "Vehículo actualizado"}

@router.delete("/{id}")
def eliminar_vehiculo(id: int):
    vehiculos.pop(id)
    return {"mensaje": "Vehículo eliminado"}