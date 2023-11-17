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

    # Métodos

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
        for grupo in materia.getGrupos():
            grupo.getProfesor().desvincularGrupo(grupo)

            for estudiante in grupo.getEstudiantes():
                Coordinador.desmatricular(estudiante, grupo)

    def desmatricularDelSistema(self, estudiante):
        e1 = next((e for e in Estudiante.getEstudiantes() if e == estudiante), None)

        if e1 is not None:
            Estudiante.getEstudiantes().remove(e1)

        for usuario in Usuario.getUsuariosTotales():
            if isinstance(usuario, Estudiante) and usuario == estudiante:
                Usuario.getUsuariosTotales().remove(usuario)
                break

    @staticmethod
    def crearHorario(materias):
        resultado = [None, None, None]
        horario = Horario()
        ok = True
        materiaObstaculo = None

        gPosible = [0] * len(materias)
        mPosibles = [0] * len(materias)
        i = 0  # índice de materias

        while True:
            pClases = materias[i].getGrupos()[gPosible[i]].getHorario()
            if horario.comprobarDisponibilidad(pClases):
                horario.ocuparHorario(materias[i].getGrupos()[gPosible[i]])
                mPosibles[i] = 1
                i += 1
                if i == len(materias):
                    break
            else:
                gPosible[i] += 1

                if gPosible[i] == len(materias[i].getGrupos()):
                    i -= 1
                    horario.liberarHorario(
                        materias[i].getGrupos()[gPosible[i]].getHorario()
                    )
                    gPosible[i] += 1
                    gPosible[i + 1] = 0

                    if gPosible[i] == len(materias[i].getGrupos()):
                        m = 0
                        for k in mPosibles:
                            if k == 0:
                                materiaObstaculo = materias[m]
                                ok = False
                            else:
                                m += 1
                        break

        resultado[0] = ok
        resultado[1] = horario
        resultado[2] = materiaObstaculo

        return resultado

    def eliminarMateria(self, materia):
        if materia in Materia.getMateriasTotales():
            Coordinador.restaurarMateria(materia)
            Materia.getMateriasTotales().remove(materia)
        else:
            raise CampoVacio("Se ha ingresado un valor inválido")
    
    def agregarMateria(self, nombre, codigo, descripcion, creditos, facultad, prerrequisitos):
        nombreMaterias = [materia.getNombre() for materia in Materia.getMateriasTotales()]

        if nombre not in nombreMaterias:
            Materia(nombre, codigo, descripcion, creditos, facultad, prerrequisitos)

    @classmethod
    def candidatoABeca(cls, estudiante, tipoDeBeca):
        if tipoDeBeca.getCupos() > 0:
            if (
                estudiante.getPromedio() >= tipoDeBeca.getPromedioRequerido()
                and estudiante.getAvance() >= tipoDeBeca.getAvanceRequerido()
                and estudiante.getCreditos() >= tipoDeBeca.getCreditosInscritosRequeridos()
                and estudiante.getEstrato() <= tipoDeBeca.getEstratoMinimo()
            ):
                if tipoDeBeca.getNecesitaRecomendacion():
                    return Profesor.recomendarEstudiante(estudiante)
                return True  # No necesita recomendación, pero cumple los demás requisitos
        return False

    @classmethod
    def mostrarFacultades(cls):
        retorno = ""
        for i, facultad in enumerate(cls._facultades, start=1):
            retorno += f"{i}. {facultad}\n"
        return retorno

    def __str__(self):
        return f"Nombre Coordinador: {self.getNombre()}\nDocumento: {self.getId()}"

    # Setters y Getters

    @classmethod
    def getLimitesCreditos(cls):
        return cls._LIMITES_CREDITOS
    
    @classmethod
    def getCoordinadoresTotales(cls):
        return cls._coordinadoresTotales

    @classmethod
    def setCoordinadoresTotales(cls, coordinadores):
        cls._coordinadoresTotales = coordinadores

    @classmethod
    def getFacultades(cls):
        return cls._facultades

    @classmethod
    def setFacultades(cls, facultades):
        cls._facultades = facultades
    
    @classmethod
    def mostrarBecas(cls):
        i = 1
        for beca in Beca.getBecas():
            a = beca.getConvenio()
    
    @classmethod
    def getUsuarioIngresado(cls):
        return cls._usuarioIngresado
    
    @classmethod
    def setUsuarioIngresado(cls, usuario):
        cls._usuarioIngresado = usuario