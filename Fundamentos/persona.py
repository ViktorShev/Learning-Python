class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

#Modificar los valores
Persona.nombre = 'Juan'
Persona.edad = 28

#Acceder a los valores
print(Persona.nombre)
print(Persona.edad)

#Creacion de objeto
persona = Persona('Karla', 30)
print(persona.nombre)
print(persona.edad)
print(id(persona))

#Creacion de un segundo objeto
persona2 = Persona('Carlos', 40)
print(persona2.nombre)
print(persona2.edad)
print(id(persona2)) 