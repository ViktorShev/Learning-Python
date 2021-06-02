class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property    
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
       
    @property 
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
        
    @property
    def todo(self):
        print('Persona:', self._nombre, self._apellido, self._edad)
        
    def __del__(self):
        print('Persona:', self._nombre, self._apellido)
        
if __name__ == '__main__':
    p1 = Persona('Juan', 'Perez', 28)
    p1.nombre = 'Juan Carlos'
    p1.apellido = 'Lara'
    p1.edad = 30
    p1.todo

    print(__name__)