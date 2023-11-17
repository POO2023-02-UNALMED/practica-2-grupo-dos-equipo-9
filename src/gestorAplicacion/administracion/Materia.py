from gestorAplicacion.administracion.Grupo import Grupo
from excepciones.ErrorManejo import *
# from Salon import Salon


class Materia:
    materiasTotales = []

    def __init__(
        self,
        nombre,
        codigo,
        descripcion,
        creditos,
        facultad,
        prerrequisitos=None,
        grupos=None,
    ):
        self.nombre = nombre
        self.codigo = codigo
        self.descripcion = descripcion
        self.creditos = creditos
        self.facultad = facultad
        self.prerrequisitos = prerrequisitos or []
        self.grupos =[]
        # self.cupos =0
        self.hacerAbreviatura(nombre)
        Materia.materiasTotales.append(self)

    # MÉTODOS ESTÁTICOS

    @staticmethod
    def buscarMateria(nombre, codigo):
        # Si existe la materia, retorna su índice en la lista materiasTotales.
        # Si no existe, retorna -1.

        for i in range(len(Materia.materiasTotales)):
            if (
                Materia.materiasTotales[i].getNombre() == nombre
                and Materia.materiasTotales[i].getCodigo() == codigo
            ):
                return i
        return -1

    @staticmethod
    def puedeVerMateria(estudiante, grupo):
        from gestorAplicacion.usuario.Coordinador import Coordinador
        
        # Comprueba si un estudiante puede estar en un grupo.

        if not (
            estudiante.getCreditos() + grupo.getMateria().getCreditos()
            <= Coordinador.getLimitesCreditos()
        ):
            return False
        if not estudiante.getHorario().comprobarDisponibilidad(grupo.getHorario()):
            return False
        if grupo.getCupos() == 0:
            return False
        if not Materia.comprobarPrerrequisitos(estudiante, grupo.getMateria()):
            return False
        return True

    @staticmethod
    def comprobarPrerrequisitos(estudiante, materiap):
        # Comprueba si un estudiante cumple con los prerrequisitos de una materia.

        materiasVistas = []
        materias_estudiante=[]
        for materia in estudiante.getMaterias():
            materias_estudiante.append(materia.getCodigo())
        for grupo in estudiante.getGruposVistos():
            materiasVistas.append(grupo.getMateria().getCodigo())
        for materia in materiap.getPrerrequisitos():
            flag = False
            for vista in materiasVistas:
                if materia.getCodigo() == vista:
                    flag = True
                    break
            if not flag:
                return False
        if materiap.getCodigo() in materiasVistas:
            return False
        if materiap.getCodigo() in materias_estudiante:
            return False
        return True

    @staticmethod
    def encontrarMateria(nombre):
        mater = None
        for materia in Materia.getMateriasTotales():
            if materia.getNombre() == nombre:
                mater = materia
        return mater

    @staticmethod
    def mostrarMaterias():
        retorno = ""
        i = 1
        for materia in Materia.materiasTotales:
            retorno += f"{i}. {materia.nombre}.\n"
            i += 1
        return retorno
    
    @staticmethod
    def listaNombresMaterias():
        retorno = []
        for materia in Materia.materiasTotales:
            retorno.append(materia.getNombre())
        return retorno

