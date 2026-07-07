
from __future__ import annotations
from dataclasses import dataclass


class ValorInvalidoError(ValueError):
    pass


@dataclass(frozen=True)
class NombreCompleto:

    nombre: str
    apellido: str

    def __post_init__(self):
        if not self.nombre or not self.nombre.strip():
            raise ValorInvalidoError("El nombre es obligatorio.")
        if not self.apellido or not self.apellido.strip():
            raise ValorInvalidoError("El apellido es obligatorio.")

    def completo(self) -> str:
        return f"{self.nombre} {self.apellido}"


@dataclass(frozen=True)
class Telefono:

    numero: str

    def __post_init__(self):
        if self.numero and len(self.numero) > 9:
            raise ValorInvalidoError(
                "El teléfono no puede superar 9 caracteres."
            )


@dataclass(frozen=True)
class Email:

    direccion: str | None = None

    def __post_init__(self):
        if self.direccion and "@" not in self.direccion:
            raise ValorInvalidoError("El email no tiene un formato válido.")


@dataclass(frozen=True)
class Direccion:
    texto: str

    def __post_init__(self):
        if not self.texto or not self.texto.strip():
            raise ValorInvalidoError("La dirección no puede estar vacía.")
