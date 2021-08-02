from connection import Connection
from logger_base import log
import sys


class PoolCursor:
    def __init__(self):
        self._conn = None
        self._cursor = None
        
    def __enter__(self):
        if self._conn is None:
            try:
                self._conn = Connection.getConn()
                self._cursor = self._conn.cursor()
                return self._cursor
            except Exception as e:
                log.error(f'An error has occured: {e}, shutting down.')
                sys.exit()
        else:
            return self._cursor
    
    def __exit__(self, exception, exception_value, traceback):
        if exception_value:
            self._conn.rollback()
            log.error(f'An error has occured: {exception} {exception_value}\nROLLBACK.')
        else:
            self._conn.commit()
            log.info('Transaction commit.')
            
        self._cursor.close()
        Connection.freeConn(self._conn)