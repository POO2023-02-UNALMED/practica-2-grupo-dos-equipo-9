from abc import ABC, abstractmethod
from gestorAplicacion.administracion.Materia import Materia


class Usuario(ABC):
    _usuariosTotales = []

    def __init__(self, id, nombre, facultad, pw="0000"):
        self._id = id
        self._nombre = nombre
        self._pw = str(pw)
        self._facultad = facultad
        Usuario._usuariosTotales.append(self)

    @abstractmethod
    def __str__(self):
        pass

    @classmethod
    def mostrarUsuarios(cls) -> str:
        return '\n'.join(f"{i}. {usuario._nombre}, id: {usuario._id}" for i, usuario in enumerate(cls.getUsuariosTotales(), 1))

    def comprobacionFacultad(self, otro_usuario) -> bool:
        return self._facultad.lower() == otro_usuario._facultad.lower()

    @classmethod
    def desmatricularDelSistema(cls, usuario) -> None:
        cls._usuariosTotales = list(filter(lambda u: u != usuario, cls._usuariosTotales))

    @classmethod
    def eliminar_materia(cls, materia) -> None:
        Materia.getMateriasTotales().remove(materia)

    @classmethod
    def agregar_materia(cls, nombre, codigo, descripcion, creditos, facultad, prerrequisitos) -> None:
        nuevaMateria = Materia(nombre, codigo, descripcion, creditos, facultad, prerrequisitos)
        Materia.getMateriasTotales().append(nuevaMateria)

    def getTipo(self):
        return self._tipo
    def setTipo(self, tipo):
        self._tipo = tipo

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getPw(self):
        return self._pw

    def setPw(self, pw):
        self._pw = pw

    def getFacultad(self):
        return self._facultad

    def setFacultad(self, facultad):
        self._facultad = facultad

    @classmethod
    def getUsuariosTotales(cls):
        return cls._usuariosTotales

    @classmethod
    def setUsuariosTotales(cls, usuariosTotales):
        cls._usuariosTotales = usuariosTotales
