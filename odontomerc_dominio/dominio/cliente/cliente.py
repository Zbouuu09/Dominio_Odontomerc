

from __future__ import annotations
from dataclasses import dataclass
import uuid

from dominio.shared import NombreCompleto, Telefono, Email
from .expediente import Expediente


@dataclass(frozen=True)
class ClienteId:
    valor: str

    @staticmethod
    def nueva() -> "ClienteId":
        return ClienteId(str(uuid.uuid4())[:4].upper())


@dataclass
class Cliente:
    id: ClienteId
    nombre_completo: NombreCompleto
    fecha_nacimiento: str
    telefono: Telefono
    email: Email
    expediente: Expediente  

    @staticmethod
    def registrar(nombre: str, apellido: str, fecha_nac: str,
                telefono: str, email: str) -> "Cliente":

        nombre_completo = NombreCompleto(nombre, apellido)
        return Cliente(
            id=ClienteId.nueva(),
            nombre_completo=nombre_completo,
            fecha_nacimiento=fecha_nac,
            telefono=Telefono(telefono),
            email=Email(email),
            expediente=Expediente.inicial_para(nombre, apellido),
        )

    def actualizar_datos(self, nombre: str, apellido: str, fecha_nac: str,
                        telefono: str, email: str) -> None:
        self.nombre_completo = NombreCompleto(nombre, apellido)
        self.fecha_nacimiento = fecha_nac
        self.telefono = Telefono(telefono)
        self.email = Email(email)

    def actualizar_expediente(self, descripcion: str) -> None:

        self.expediente.actualizar_descripcion(descripcion)
