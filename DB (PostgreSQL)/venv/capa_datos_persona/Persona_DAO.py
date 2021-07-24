from Persona import Persona
from logger_base import log
from Conexion import Connection
from Cursor_Del_Pool import PoolCursor
import psycopg2


class PersonaDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'
    
    @classmethod
    def seleccionar(cls):
        with PoolCursor() as cur:
                cur.execute(cls._SELECCIONAR)
                registros = cur.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas
    
    @classmethod
    def insertar(cls, persona):
        with PoolCursor() as cur:
                valores = (persona.nombre, persona.apellido, persona.email)
                cur.execute(cls._INSERTAR, valores)
                log.debug(f'Persona insertada: {persona}')
                return cur.rowcount
            
    @classmethod
    def actualizar(cls, persona):
        with PoolCursor() as cur:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id)
            cur.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {persona}')
            return cur.rowcount
            
    @classmethod
    def eliminar(cls, persona):
        with PoolCursor() as cur:
            valores = (persona.id,)
            cur.execute(cls._ELIMINAR, valores)
            log.debug(f'Persona eliminada: {persona}')
            return cur.rowcount
                
                
if __name__ == '__main__':
  # Insertar un registro
  persona1 = Persona(nombre='Test', apellido='Test', email='TT@mail.com')
  personas_insertadas = PersonaDAO.insertar(persona1)
  log.debug(f'Personas insertadas: {personas_insertadas}')
  
  # Eliminar un registro
  persona1 = Persona(id_persona=36)
  personas_eliminadas = PersonaDAO.eliminar(persona1)
  log.debug(f'Personas eliminadas: {personas_eliminadas}')
  
  # Actualizar un registro
  persona1 = Persona(1, 'Juan', 'Perez', 'jperez@mail.com')
  personas_actualizadas = PersonaDAO.actualizar(persona1)
  log.debug(f'Personas actualizadas: {personas_actualizadas}')
  
  # Seleccionar los objetos
  personas = PersonaDAO.seleccionar()
  for persona in personas:
      log.debug(persona)