class Persona:
    def __init__(self, nombre, edad):
        self.edad = edad
        self.nombre = nombre
        
    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'
    
    def __sub__(self, other):
        return self.edad - other.edad
        

persona1 = Persona('Juan', 28)
persona2 = Persona('Carlos', 20)

print(persona1 + persona2)
print(persona1 - persona2)

#obj1 + obj1
#obj1.__add__(obj2)