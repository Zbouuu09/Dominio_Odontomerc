

from __future__ import annotations
from dataclasses import dataclass, field
import uuid


@dataclass(frozen=True)
class EspecialidadId:
    valor: str

    @staticmethod
    def nueva() -> "EspecialidadId":
        return EspecialidadId(str(uuid.uuid4())[:4].upper())


@dataclass
class Especialidad:
    """Aggregate Root del agregado Especialidad."""
    id: EspecialidadId
    nombre: str
    descripcion: str

    @staticmethod
    def crear(nombre: str, descripcion: str) -> "Especialidad":
        return Especialidad(
            id=EspecialidadId.nueva(),
            nombre=nombre,
            descripcion=descripcion,
        )

    def actualizar(self, nombre: str, descripcion: str) -> None:
        self.nombre = nombre
        self.descripcion = descripcion
