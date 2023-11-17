from excepciones.ErrorAplicacion import ErrorAplicacion

class ErrorManejo(ErrorAplicacion):
    def __init__(self, error):
        super().__init__(error)

class CampoVacio(ErrorManejo):
    def __init__(self):
        super().__init__("Los campos del formulario no fueron llenados")

class CampoInvalido(ErrorManejo):
    def __init__(self):
        super().__init__("Los campos del formulario fueron llenados incorrectamente")

class MateriaMatriculada(ErrorManejo):
    def __init__(self, nombre):
        super().__init__(f"El estudiante ya tiene la materia {nombre} matriculada")

class EstudianteSinCreditos(ErrorManejo):
    def __init__(self, nombre=""):
        super().__init__(f"El estudiante {nombre} no tiene créditos suficientes")

class EstudianteSinMatriculaPagada(ErrorManejo):
    def __init__(self, nombre=""):
        super().__init__(f"El estudiante {nombre} no tiene la matrícula pagada")

class PrerrequisitosMateria(ErrorManejo):
    def __init__(self, nombre=""):
        super().__init__(f"El estudiante {nombre} no cumple con los prerrequisitos")

class MateriaSinCupo(ErrorManejo):
    def __init__(self, nombre=""):
        super().__init__(f"La materia {nombre} no cuenta con cupos suficientes")

class GrupoNoAgregado(ErrorManejo):
    def __init__(self):
        super().__init__("El grupo no ha sido agregado a la materia. El profesor y/o el salón no contaban con disponibilidad")

class BecaExistente(ErrorManejo):
    def __init__(self):
        super().__init__("El nombre que intenta asignar a la nueva beca ya existe. Inténtelo nuevamente.")
