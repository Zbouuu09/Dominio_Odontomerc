"""
dominio/cliente/expediente.py

Entidad: Expediente
Pertenece al agregado Cliente (no es un Aggregate Root).

Extraído de la regla de negocio en cliente_servicio.registrar_cliente:
"un cliente tiene un expediente", el cual se crea automáticamente al
registrar al cliente. Al vivir dentro del límite del agregado Cliente,
Expediente solo debe modificarse a través de la raíz Cliente.
"""

from __future__ import annotations
from dataclasses import dataclass
from datetime import date
import uuid


@dataclass(frozen=True)
class ExpedienteId:
    valor: str

    @staticmethod
    def nueva() -> "ExpedienteId":
        return ExpedienteId(str(uuid.uuid4())[:4].upper())


@dataclass
class Expediente:
    """Entidad interna del agregado Cliente."""
    id: ExpedienteId
    descripcion: str
    fecha_creacion: str

    @staticmethod
    def inicial_para(nombre: str, apellido: str) -> "Expediente":
        return Expediente(
            id=ExpedienteId.nueva(),
            descripcion=f"Expediente inicial de {nombre} {apellido}",
            fecha_creacion=str(date.today()),
        )

    def actualizar_descripcion(self, descripcion: str) -> None:
        self.descripcion = descripcion
