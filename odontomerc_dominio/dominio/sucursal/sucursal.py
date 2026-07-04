

from __future__ import annotations
from dataclasses import dataclass
import uuid

from dominio.shared import Direccion


@dataclass(frozen=True)
class SucursalId:
    valor: str

    @staticmethod
    def nueva() -> "SucursalId":
        return SucursalId(str(uuid.uuid4())[:4].upper())


@dataclass
class Sucursal:

    id: SucursalId
    nombre: str
    direccion: Direccion

    @staticmethod
    def crear(nombre: str, direccion: str) -> "Sucursal":
        return Sucursal(
            id=SucursalId.nueva(),
            nombre=nombre,
            direccion=Direccion(direccion),
        )

    def actualizar(self, nombre: str, direccion: str) -> None:
        self.nombre = nombre
        self.direccion = Direccion(direccion)
