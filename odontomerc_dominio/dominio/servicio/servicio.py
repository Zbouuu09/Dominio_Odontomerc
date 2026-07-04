

from __future__ import annotations
from dataclasses import dataclass
import uuid


@dataclass(frozen=True)
class ServicioId:
    valor: str

    @staticmethod
    def nueva() -> "ServicioId":
        return ServicioId(str(uuid.uuid4())[:4].upper())


@dataclass
class ServicioOdontologico:
    """Aggregate Root del agregado ServicioOdontologico."""
    id: ServicioId
    nombre: str
    descripcion: str

    @staticmethod
    def crear(nombre: str, descripcion: str) -> "ServicioOdontologico":
        return ServicioOdontologico(
            id=ServicioId.nueva(),
            nombre=nombre,
            descripcion=descripcion,
        )

    def actualizar(self, nombre: str, descripcion: str) -> None:
        self.nombre = nombre
        self.descripcion = descripcion
