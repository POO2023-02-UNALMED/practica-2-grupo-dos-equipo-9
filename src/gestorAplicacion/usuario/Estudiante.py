from gestorAplicacion.administracion.Grupo import Grupo
from gestorAplicacion.usuario.Usuario import Usuario
from gestorAplicacion.administracion.Horario import Horario
# import pickle;


class Estudiante(Usuario):
    _estudiantes = []
    def __init__(self,id,nombre,programa,semestre,facultad,estrato,sueldo,materias=None,gruposVistos=None):
        

        super().__init__(id, nombre, facultad)
        super().setTipo("Estudiante")
        self._programa = programa
        self._semestre = semestre
        self._creditos = 0
        self._materias = materias or []  # no se que tan bien este esto
        self._grupos = []
        self._estrato = estrato
        self._sueldo = sueldo
        self._valorMatricula = 1234567 * estrato
        self._matriculaPagada = False
        self._promedio = 0
        self._avance = 0
        self._CREDITOS_PARA_GRADURASE = 120
        self._beca = None
        self._notas = None
        self._gruposVistos = gruposVistos or []
        self._horario = Horario()  # Revisar
        Estudiante._estudiantes.append(self)

    # METODOS
    
    def __str__(self):
        return "Nombre Estudiante: "+self.getNombre()+" Documento: "+ self.getId()

    def mostrarMaterias():
        retorno = ""
        i = 1
        for grupo in Estudiante._grupos:
            retorno += (
                str(i)
                + "- "
                + grupo._materia._nombre
                + " | Grupo "
                + str(grupo._numero)
                + "\n"
            )
            i += 1
        return retorno

    @staticmethod
    def buscarEstudiante(nombre, id):
        # Si el estudiante existe, retorna su indice en la lista 'estudiantes'
        # Si no existe, retorna -1.
        for i in range(len(Estudiante._estudiantes)):
            if (Estudiante._estudiantes[i].getNombre() == nombre) and (
                Estudiante._estudiantes[i].getId() == id
            ):
                return i
        return -1
