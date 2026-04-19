from pydantic import BaseModel

class Cliente(BaseModel):
    nombre: str
    cedula: str
    telefono: str
    direccion: str

class Vehiculo(BaseModel):
    placa: str
    marca: str
    modelo: str
    cliente_id: int

class Orden(BaseModel):
    fecha: str
    descripcion: str
    vehiculo_id: int

class Servicio(BaseModel):
    nombre: str
    costo: float
    orden_id: int