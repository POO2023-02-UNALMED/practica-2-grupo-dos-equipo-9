import pickle

class Persona:
    cantidad_personas = 0
    personas_en_sistema = []

    def __init__(self, cedula, nombre, direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.direccion = direccion
        Persona.cantidad_personas += 1
        Persona.personas_en_sistema.append(self)

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, value):
        self._cedula = value

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    @classmethod
    def get_personas_en_sistema(cls):
        return cls.personas_en_sistema

    @classmethod
    def set_personas_en_sistema(cls, personas):
        cls.personas_en_sistema = personas

    def serialize(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, file_name):
        with open(file_name, 'rb') as file:
            return pickle.load(file)
