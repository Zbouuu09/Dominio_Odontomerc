

from __future__ import annotations
from dataclasses import dataclass
import uuid

from dominio.shared import NombreCompleto, Telefono, Email
from dominio.especialidad import EspecialidadId


@dataclass(frozen=True)
class DoctorId:
    valor: str

    @staticmethod
    def nueva() -> "DoctorId":
        return DoctorId(str(uuid.uuid4())[:4].upper())


@dataclass
class Doctor:
    """Aggregate Root del agregado Doctor."""
    id: DoctorId
    nombre_completo: NombreCompleto
    correo: Email
    telefono: Telefono
    especialidad_id: EspecialidadId

    @staticmethod
    def registrar(nombre: str, apellido: str, correo: str,
                telefono: str, especialidad_id: EspecialidadId) -> "Doctor":
        return Doctor(
            id=DoctorId.nueva(),
            nombre_completo=NombreCompleto(nombre, apellido),
            correo=Email(correo),
            telefono=Telefono(telefono),
            especialidad_id=especialidad_id,
        )

    def actualizar(self, nombre: str, apellido: str, correo: str,
                    telefono: str, especialidad_id: EspecialidadId) -> None:
        self.nombre_completo = NombreCompleto(nombre, apellido)
        self.correo = Email(correo)
        self.telefono = Telefono(telefono)
        self.especialidad_id = especialidad_id

    def reasignar_especialidad(self, especialidad_id: EspecialidadId) -> None:
        self.especialidad_id = especialidad_id
