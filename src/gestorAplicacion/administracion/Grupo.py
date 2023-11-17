class Grupo:
    _gruposTotales = []

    def __init__(self, materia, numero, profesor, horario=None, cupos=None, salon=None):
        self._materia = materia
        self._numero = numero
        self._profesor = profesor
        self._horario = horario if horario is not None else []
        self._cupos = cupos
        self._salon = salon
        self._estudiantes = []
        Grupo._gruposTotales.append(self)

    def mostrar_informacion_grupo(self):
        return "Número del grupo: {}, Profesor: {}, Horario: {}, Cupos: {}, Salón: {}".format(
            self._numero, self._profesor, self._horario, self._cupos, self._salon
        )

    def existencia_estudiante(self, estudiante):
        return any(e.getId() == estudiante.getId() for e in self._estudiantes)

    def eliminar_estudiante(self, estudiante):
        for i, e in enumerate(self._estudiantes):
            if e.getNombre() == estudiante.getNombre():
                self._cupos += 1
                estudiante.eliminar_grupo(self)
                self._estudiantes.pop(i)
                break

            
    @staticmethod
    def buscar_grupo(materia_e, grupo_e):
        from gestorAplicacion.administracion.Materia import Materia
        
        for materia in Materia.getMateriasTotales():
            if materia.getNombre() == materia_e.getNombre():
                for grupo in materia.getGrupos():
                    if grupo.getNumero() == grupo_e.getNumero():
                        return grupo

    def agregar_estudiante(self, estudiante):
        self._estudiantes.append(estudiante)
        self._cupos -= 1


    def getNumero(self):
        return self._numero
    def setNumero(self, numero):
        self._numero = numero

    def getProfesor(self):
        return self._profesor

    def setProfesor(self, profesor):
        self._profesor = profesor

    def getHorario(self):
        return self._horario

    def setHorario(self, horario):
        self._horario = horario

    def getCupos(self):
        return self._cupos

    def setCupos(self, cupos):
        self._cupos = cupos

    def getSalon(self):
        return self._salon

    def setSalon(self, salon):
        self._salon = salon

    def getEstudiantes(self):
        return self._estudiantes

    def setEstudiantes(self, estudiantes):
        self._estudiantes = estudiantes

    def getMateria(self):
        return self._materia

    def setMateria(self, materia):
        self._materia = materia

    @classmethod
    def getGruposTotales(cls):
        return cls._gruposTotales

    @classmethod
    def setGruposTotales(cls, grupos):
        cls._gruposTotales = grupos