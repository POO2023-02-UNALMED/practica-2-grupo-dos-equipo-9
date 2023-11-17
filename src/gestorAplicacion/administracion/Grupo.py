class Grupo:
    _gruposTotales = []

    def __init__(self, materia, numero, profesor, horario=[], cupos=None, salon=None):
        self._materia = materia
        self._numero = numero
        self._profesor = profesor
        self._horario = horario if horario is not None else []
        self._cupos = cupos
        self._salon = salon
        self._estudiantes = []
        Grupo._gruposTotales.append(self)

    def mostrarInformacionGrupo(self):
        return "Número del grupo: {}, Profesor: {}, Horario: {}, Cupos: {}, Salón: {}".format(
            self.numero, self.profesor, self.horario, self.cupos, self.salon
        )

    def existenciaEstudiante(self, estudiante):
        for e in self._estudiantes:
            if e.getId() == estudiante.getId():
                return True
        return False

    def eliminarEstudiante(self, estudiante):
        indice = -1
        for i, e in enumerate(self._estudiantes):
            if e.getNombre() == estudiante.getNombre():
                indice = i
                self._cupos += 1
                estudiante.eliminarGrupo(self)
                break
        if indice != -1:
            self._estudiantes.pop(indice)

    @staticmethod
    def buscarGrupo(materiaE, grupoE):
        from gestorAplicacion.administracion.Materia import Materia
        
        indicei = -1
        indicej = -1
        for i in range(len(Materia.getMateriasTotales())):
            materia = Materia.getMateriasTotales()[i]
            if materia.getNombre() == materiaE.getNombre():
                indicei = i
                for j in range(len(materia.getGrupos())):
                    grupo = materia.getGrupos()[j]
                    if grupo.getNumero() == grupoE.getNumero():
                        indicej = j
                        break

        return Materia.getMateriasTotales()[indicei].getGrupos()[indicej]

    def agregarEstudiante(self, estudiante):
        self._estudiantes.append(estudiante)
        self._cupos -= 1

    def getNumero(self):
        return self._numero