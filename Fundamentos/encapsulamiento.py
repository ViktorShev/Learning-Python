class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def get_nombre(self):
        return self.__nombre
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad
        
        
p1 = Persona('Juan', 18)
print(p1.get_nombre())
print(p1.get_edad())

p1.set_nombre('Karla')
print(p1.get_nombre())
p1.set_edad(24)
print(p1.get_edad())