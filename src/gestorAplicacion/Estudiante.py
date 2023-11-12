import Persona
class Estudiante(Persona):
    estudiantes_registrados = []

    def __init__(self, cedula, nombre, direccion, estrato=3, promedio=0.0, ingresos=400000, numerocreditosmatriculados=11):
        super().__init__(cedula, nombre, direccion)
        self.estrato = estrato
        self.promedio = promedio
        self.ingresos = ingresos
        self.numerocreditosmatriculados = numerocreditosmatriculados
        self.valormatricula = self.calcular_matricula()
        Estudiante.estudiantes_registrados.append(self)

    def get_estrato(self):
        return self.estrato

    def set_estrato(self, estrato):
        self.estrato = estrato

    def get_promedio(self):
        return self.promedio

    def calcular_matricula(self):
        MATBASE = 100000
        descuento = 0.2
        matricula_sin_descuento = MATBASE * self.numerocreditosmatriculados

        if self.estrato <= 3:
            matriculacero = 0
            self.valormatricula = matriculacero
            return matriculacero
        elif self.promedio >= 4.5:
            matricula_con_descuento = matricula_sin_descuento * descuento
            return matricula_con_descuento
        else:
            self.valormatricula = matricula_sin_descuento
            return matricula_sin_descuento

    @classmethod
    def encontrar_estudiante_con_cc(cls, cedula):
        for estudiante in cls.estudiantes_registrados:
            if estudiante.get_cedula() == cedula:
                return True
        return False

    def __str__(self):
        return f"\nNombre: {self.nombre}\nCedula: {self.cedula}\nDireccion: {self.direccion}"