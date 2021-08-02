from logger_base import log
from pool_cursor import PoolCursor
from usuario import Usuario

class UsuarioDAO:
    _SELECT = 'SELECT * FROM usuarios ORDER BY id_usuario'
    _INSERT = 'INSERT INTO usuarios(username, password) VALUES(%s, %s)'
    _UPDATE = 'UPDATE usuarios SET username=%s, password=%s WHERE id_usuario=%s'
    _DELETE = 'DELETE FROM usuarios WHERE id_usuario=%s'
    
    @classmethod
    def select(cls):
        with PoolCursor() as cur:
            cur.execute(cls._SELECT)
            registros = cur.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
        return usuarios
    
    @classmethod
    def insert(cls, usuario):
        with PoolCursor() as cur:
            values = (usuario.username, usuario.password)
            cur.execute(cls._INSERT, values)
            
    @classmethod
    def update(cls, usuario):
        with PoolCursor() as cur:
            values = (usuario.username, usuario.password, usuario.id)
            cur.execute(cls._UPDATE, values)
            
    @classmethod
    def delete(cls, usuario):
        with PoolCursor() as cur:
            values = (usuario.id,)
            cur.execute(cls._DELETE, values)