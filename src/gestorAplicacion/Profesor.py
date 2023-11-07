import pickle

class Profesor(Persona):
    profesores_con_lau = []

    def __init__(self, cedula, nombre, direccion, tipodeafiliacion, salario, horasdeclasesemanal):
        super().__init__(cedula, nombre, direccion)
        self.tipodeafiliacion = tipodeafiliacion
        self.salario = salario
        self.horasdeclasesemanal = horasdeclasesemanal
        Profesor.profesores_con_lau.append(self)

    @property
    def tipodeafiliacion(self):
        return self._tipodeafiliacion

    @tipodeafiliacion.setter
    def tipodeafiliacion(self, value):
        self._tipodeafiliacion = value

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, value):
        self._salario = value

    @property
    def horasdeclasesemanal(self):
        return self._horasdeclasesemanal

    @horasdeclasesemanal.setter
    def horasdeclasesemanal(self, value):
        self._horasdeclasesemanal = value

    @classmethod
    def get_profesoresconlau(cls):
        return cls.profesores_con_lau

    @classmethod
    def set_profesoresconlau(cls, profesores):
        cls.profesores_con_lau = profesores

    def serialize(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, file_name):
        with open(file_name, 'rb') as file:
            return pickle.load(file)
