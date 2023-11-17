from gestorAplicacion.administracion.Horario import Horario
from gestorAplicacion.administracion.Materia import Materia
from gestorAplicacion.usuario.Estudiante import Estudiante
from gestorAplicacion.usuario.Profesor import Profesor
from gestorAplicacion.usuario.Usuario import Usuario
from gestorAplicacion.administracion.Beca import Beca
from excepciones.ErrorManejo import *
from excepciones.ObjetoInexistente import *

class Coordinador(Usuario):
    _usuarioIngresado = None
    _LIMITES_CREDITOS = 20
    _coordinadoresTotales = []
    _facultades = [
        "Facultad de arquitectura",
        "Facultad de ciencias",
        "Facultad de ciencias agrarias",
        "Facultad de ciencias humanas y economicas",
        "Facultad de minas",
        "Sede",
    ]

    def __init__(self, facultad, id, nombre, pw):
        super().__init__(id, nombre, facultad, pw)
        super().setTipo("Coordinador")
        Coordinador._coordinadoresTotales.append(self)

    # METODOS

    @staticmethod
    def desmatricular(estudiante, grupo):
        estaMatriculado = grupo.existenciaEstudiante(estudiante)

        if estaMatriculado:
            grupo.eliminarEstudiante(estudiante)
            return "El estudiante ha sido desmatriculado de la materia y su respectivo grupo"
        else:
            return "El estudiante no estaba matriculado"

    @staticmethod
    def restaurarMateria(materia):
        for i in range(len(materia.getGrupos())):
            puntero_Grupo = materia.getGrupos()[i]
            puntero_Grupo.getProfesor().desvincularGrupo(puntero_Grupo)

            for j in range(len(puntero_Grupo.getEstudiantes())):
                puntero_Estudiante = puntero_Grupo.getEstudiantes()[j]
                Coordinador.desmatricular(puntero_Estudiante, puntero_Grupo)


    def desmatricularDelSistema(self, estudiante):
        e1 = None
        for e in Estudiante.getEstudiantes():
            if e == estudiante:
                e1 = e

        if e1 is not None:
            Estudiante.getEstudiantes().remove(e1)

        for usuario in Usuario.getUsuariosTotales():
            if isinstance(usuario, Estudiante):
                if usuario == estudiante:
                    Usuario.getUsuariosTotales().remove(usuario)
                    break