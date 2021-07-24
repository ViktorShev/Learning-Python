from logger_base import log
from Conexion import Connection

class PoolCursor:
    def __init__(self):
        self._conexion = None
        self._cursor = None
        
    def __enter__(self):
        log.debug('Inicio del metodo with __enter__')
        self._conexion = Connection.getConnection()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, exception, value, traceback):
        log.debug('Se ejecuta el metodo __exit__')
        if value:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion, se hizo un rollback: {exception} {value} {traceback}')
        else:
            self._conexion.commit()
            log.debug('Se ha hecho commit.')
            
        self._cursor.close()
        Connection.freeConn(self._conexion)
        
if __name__ == '__main__':
    with PoolCursor() as cur:
        log.debug('Dentro del bloque with')
        valores = ('Maximiliano', 'Lopez', 'mlopez@mail.com')
        cur.execute('INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)', valores)