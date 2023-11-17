from enum import Enum


class DiaSemana(Enum):
    # Indice y lenght
    LUNES = (0, 5)
    MARTES = (1, 6)
    MIERCOLES = (2, 9)
    JUEVES = (3, 6)
    VIERNES = (4, 7)
    SABADO = (5, 6)
    DOMINGO = (6, 7)

    @classmethod
    def getDiaPorIndice(cls, indice) -> str:
        for dia in cls:
            if dia.value[0] == indice:
                return dia.name
        return None


class Horario:
    _horariosTotales = []

    def __init__(self, diaSemana=0, horaInicio=0, horaFinal=0, grupo=""):
        self._horario = [[None] * 24 for _ in range(7)]
        self._grupoContenidos = []
        if grupo != "":
            self._grupoContenidos.append(grupo)
            for hora in range(horaInicio, horaFinal):
                self._horario[diaSemana][hora] = grupo