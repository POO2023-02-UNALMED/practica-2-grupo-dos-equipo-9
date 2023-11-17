from gestorAplicacion.administracion.Horario import Horario
import random


class Profesor:
    _profesores = []

    def __init__(self, nombre, facultad, materiasDadas, horario=Horario(), grupos=[]):
        self._nombre = nombre
        self._facultad = facultad
        self._materiasDadas = materiasDadas
        self._horario = horario
        self._grupos = grupos if grupos is not None else []
        Profesor._profesores.append(self)

    def vincularGrupo(self, g):
        self._grupos.append(g)
        self._horario.ocuparHorario(g, g.getHorario())

    def desvincularGrupo(self, g):
        if g in self._grupos:
            indice = self._grupos.index(g)
            horaLibre = self._grupos[indice].getHorario()
            self._horario.liberarHorario(horaLibre)
            self._grupos.remove(g)

    def daMateria(self, nombre):
        for materia in self.getMateriasDadas():
            if materia.getNombre() == nombre:
                return True
        return False

    @classmethod
    def recomendarEstudiante(cls, estudiante):
        for profesor in cls._profesores:
            chance = 0
            suerte = random.randint(1, 10)
            for grupo in estudiante.getGruposVistos():
                if grupo.getProfesor().getNombre() == profesor.getNombre():
                    chance += 5
                    break
            if estudiante.getFacultad() == profesor.getFacultad():
                chance += 3
            if chance >= suerte:
                return True
        return False

    @classmethod
    def mostrarProfesores(cls):
        r = ""
        i = 1
        for profesor in cls._profesores:
            r += f"{i}. {profesor.getNombre()}. Materias: "
            for materia in profesor.getMateriasDadas():
                if (
                    profesor.getMateriasDadas().index(materia)
                    == len(profesor.getMateriasDadas()) - 1
                ):
                    r += f"{materia.getNombre()}.\n"
                else:
                    r += f"{materia.getNombre()}, "
            i += 1
        return r

    @classmethod
    def profesoresDeMateria(cls, nombre):
        profes = []
        for profesor in cls._profesores:
            if profesor.daMateria(nombre) and profesor not in profes:
                profes.append(profesor)
        return profes
    
    @classmethod
    def nombresProfesDeMateria(cls, materia):
        profes = []
        for profesor in cls._profesores:
            if profesor.daMateria(materia) and profesor not in profes:
                profes.append(profesor.getNombre())
        return profes
