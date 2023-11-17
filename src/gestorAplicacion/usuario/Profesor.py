from gestorAplicacion.administracion.Horario import Horario
import random

class Profesor:
    _profesores = []

    def __init__(self, nombre, facultad, materiasDadas, horario=Horario(), grupos=None):
        self._nombre = nombre
        self._facultad = facultad
        self._materiasDadas = materiasDadas
        self._horario = horario
        self._grupos = grupos if grupos is not None else []
        Profesor._profesores.append(self)

    def vincularGrupo(self, grupo):
        self._grupos.append(grupo)
        self._horario.ocuparHorario(grupo, grupo.getHorario())

    def desvincularGrupo(self, grupo):
        if grupo in self._grupos:
            self._horario.liberarHorario(grupo.getHorario())
            self._grupos.remove(grupo)

    def daMateria(self, nombre):
        return any(materia.getNombre() == nombre for materia in self._materiasDadas)

    @classmethod
    def recomendarEstudiante(cls, estudiante):
        for profesor in cls._profesores:
            chance = 0
            suerte = random.randint(1, 10)
            if any(grupo.getProfesor() == profesor for grupo in estudiante.getGruposVistos()):
                chance += 5
            if estudiante.getFacultad() == profesor.getFacultad():
                chance += 3
            if chance >= suerte:
                return True
        return False

    @classmethod
    def mostrarProfesores(cls):
        return '\n'.join(f"{i}. {profesor.getNombre()}. Materias: {', '.join(materia.getNombre() for materia in profesor.getMateriasDadas())}." for i, profesor in enumerate(cls._profesores, 1))

    @classmethod
    def profesoresDeMateria(cls, nombre):
        return [profesor for profesor in cls._profesores if profesor.daMateria(nombre)]

    @classmethod
    def nombresProfesDeMateria(cls, materia):
        return [profesor.getNombre() for profesor in cls._profesores if profesor.daMateria(materia)]

    @classmethod
    def encontrarProfe(cls, nombre):
        return next((profe for profe in cls._profesores if profe.getNombre() == nombre), None)

    @classmethod
    def mostrarProfesMateria(cls, nombre):
        profes = cls.profesoresDeMateria(nombre)
        return '\n'.join(f"{i}. {profesor.getNombre()}." for i, profesor in enumerate(profes, 1))

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def facultad(self):
        return self._facultad

    @facultad.setter
    def facultad(self, facultad):
        self._facultad = facultad

    @property
    def materiasDadas(self):
        return self._materiasDadas

    @materiasDadas.setter
    def materiasDadas(self, materiasDadas):
        self._materiasDadas = materiasDadas

    @property
    def grupos(self):
        return self._grupos

    @grupos.setter
    def grupos(self, grupos):
        self._grupos = grupos

    @property
    def horario(self):
        return self._horario

    @horario.setter
    def horario(self, horario):
        self._horario = horario
    @classmethod
    def getProfesores(cls):
        return cls._profesores

    @classmethod
    def setProfesores(cls, profesores):
        cls._profesores = profesores