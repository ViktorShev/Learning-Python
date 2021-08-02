class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password
        
    def __str__(self):
        return f'''
[ID: {self._id_usuario}] Username: {self._username}, password: {self._password}
    ''' 
        
    @property
    def id(self):
        return self._id_usuario
    
    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self._password
    
    @id.setter
    def id(self, id_usuario):
        self._id_usuario =  id_usuario
        
    @username.setter
    def username(self, username):
        self._username = username
        
    @password.setter
    def password(self, password):
        self._password = password