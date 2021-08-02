from logger_base import log


class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        
    @property
    def id(self):
        return self._id_persona
     
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def email(self):
        return self._email
    
    @id.setter
    def id(self, id_persona):
        self._id_persona = id_persona
        
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
        
    @email.setter
    def email(self, email):
        self._email = email
        
    def __str__(self):
        return f'''
            ID Persona: {self._id_persona}, Nombre: {self._nombre},
            Apellido: {self._apellido}, Email: {self._email}
    '''

if __name__ == '__main__':
    p1 = Persona(1, 'Juan', 'Carlos', 'jcarlos@mail.com')
    log.debug(p1)
    
    # Simular un insert
    p1 = Persona(nombre='Juan', apellido='Perez', email='jperez@mail.com')
    log.debug(p1)
    
    # Simular un delete
    p1 = Persona(id_persona=1)
    log.debug(p1)