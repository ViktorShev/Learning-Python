from psycopg2 import pool
from logger_base import log
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
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                return cls._pool
            except Exception as e:
                log.error(f'An exception has occured: {e}, shutting down.')
                sys.exit()
        else:
            return cls._pool
        
    @classmethod 
    def getConn(cls):
        conn = cls.getPool().getconn()
        return conn
    
    @classmethod
    def freeConn(cls, conn):
        cls.getPool().putconn(conn)
        
    @classmethod
    def closeConn(cls):
        cls.getPool().closeall()