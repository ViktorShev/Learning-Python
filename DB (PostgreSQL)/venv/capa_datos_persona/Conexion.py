from logger_base import log
from psycopg2 import pool
import sys


class Connection:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None
    
    @classmethod
    def getPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.debug(f'Creacion del pool de conexiones existosa! {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool de conexiones: {e}')
                sys.exit()
        else:
            return cls._pool
        
    @classmethod
    def getConnection(cls):
        conexion = cls.getPool().getconn()
        log.debug(f'Conexion obtenida del pool {conexion}')
        return conexion
    
    @classmethod
    def freeConn(cls, conexion):
        cls.getPool().putconn(conexion)
        log.debug(f'Liberamos la conexion: {conexion}')
        
    @classmethod
    def closeConns(cls):
        cls.getPool().closeall()
               
if __name__ == '__main__':
    conexion1 = Connection.getConnection()
    Connection.freeConn(conexion1)
    conexion2 = Connection.getConnection()
    Connection.freeConn(conexion2)
    conexion3 = Connection.getConnection()
    conexion4 = Connection.getConnection()
    conexion5 = Connection.getConnection()
    Connection.freeConn(conexion5)
    conexion6 = Connection.getConnection()