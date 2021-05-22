class Persona:
    def __init__(self, nombre, edad, *v, **d):
        self.nombre = nombre
        self.edad = edad
        self.valores = v
        self.dict = d
        
    def desplegar(self):
        print('Nombre:', self.nombre)
        print('Edad:', self.edad)
        print('Valores (Tupla):', self.valores)
        print('Diccionario:', self.dict)

p1 = Persona('Juan', 25)
p1.desplegar()
print('')
p2 = Persona('Karla', 24, 4,9,7)
p2.desplegar()
print('')
p3 = Persona('Paola', 27, 6,7,8)
p3.desplegar()