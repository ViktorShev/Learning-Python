import psycopg2
from psycopg2 import pool

class Connection:
    _DATABASE = 'mining_game_db'
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
            cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON, host = cls._HOST, user = cls._USERNAME, password = cls._PASSWORD, port = cls._DB_PORT, database = cls._DATABASE)
            return cls._pool
        else:
            return cls._pool

    @classmethod
    def getConnection(cls):
        connection = cls.getPool().getconn()
        return connection
    
    @classmethod
    def freeConn(cls, connection):
        cls.getPool().putconn(connection)
        
    @classmethod
    def closeConns(cls):
        cls.getPool().closeall()

