
from __future__ import annotations
from dataclasses import dataclass
import uuid

from dominio.shared import ValorInvalidoError
from dominio.sucursal import SucursalId
from dominio.doctor import DoctorId
from dominio.cliente import ExpedienteId
from dominio.servicio import ServicioId


@dataclass(frozen=True)
class CitaId:
    valor: str

    @staticmethod
    def nueva() -> "CitaId":
        return CitaId(str(uuid.uuid4())[:4].upper())


@dataclass(frozen=True)
class Horario:
    """Fecha y hora en que se agenda la Cita."""
    fecha: str
    hora: str


@dataclass(frozen=True)
class Conclusion:
    texto: str

    def __post_init__(self):
        if not self.texto or len(self.texto.strip()) < 5:
            raise ValorInvalidoError(
                "La conclusión debe tener al menos 5 caracteres."
            )


@dataclass
class Cita:

    id: CitaId
    sucursal_id: SucursalId
    doctor_id: DoctorId
    expediente_id: ExpedienteId
    servicio_id: ServicioId
    horario: Horario
    conclusion: Conclusion | None = None

    @staticmethod
    def agendar(sucursal_id: SucursalId, doctor_id: DoctorId,
                expediente_id: ExpedienteId, servicio_id: ServicioId,
                hora: str, fecha: str) -> "Cita":
        return Cita(
            id=CitaId.nueva(),
            sucursal_id=sucursal_id,
            doctor_id=doctor_id,
            expediente_id=expediente_id,
            servicio_id=servicio_id,
            horario=Horario(fecha=fecha, hora=hora),
        )

    def cerrar(self, conclusion: str) -> None:

        self.conclusion = Conclusion(conclusion)
