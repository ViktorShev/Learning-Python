# Simulacion de sobrecarga de constructores en Python
# otras formas de crear objetos en Python

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None)

    @classmethod
    def crear_persona_con_valores(cls, nombre, apellido):
        return cls(nombre, apellido)

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}'


p1 = Persona('Juan', 'Perez')
print(p1)
pVacia = Persona.crear_persona_vacia()
print(pVacia)
pConValores = Persona.crear_persona_con_valores('Karla', 'Gomez')
print(pConValores)