import psycopg2 as db


connection = db.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

try:
    with connection:
        with connection.cursor() as cur:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Alex', 'Rojas', 'arojas@mail.com')
            cur.execute(sentencia, valores)
    
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan', 'Perez', 'jperez@mail.com', 1)
            cur.execute(sentencia, valores)
except Exception as e:
    print(f'Se hizo un rollback de la transaccion debido a: {e}.')
finally:
    connection.close()
print('Termina la transaccion, se hizo commit.')