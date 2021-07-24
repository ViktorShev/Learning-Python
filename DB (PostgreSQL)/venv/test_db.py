import psycopg2


connection = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

try:
    with connection as conn:
        with conn.cursor() as cur:
          sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
          entrada = input('Proporciona los id_persona a eliminar separados por coma: ')
          valores = (tuple(entrada.split(',')),)
          cur.execute(sentencia, valores)
          registros_eliminados = cur.rowcount
          print(f'Registros eliminados: {registros_eliminados}')
          
          #sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
          #cantidad = int(input('Inserte la cantidad de registros que quiera insertar: '))
          #lista = []
          #for i in range(cantidad):
          #  valores = input('Proporcione los valores de nombre, apellido, email: ')
          #  lista.append(tuple(valores.split(', ')))
          #ejec = tuple(lista)
          #cur.executemany(sentencia, ejec)
          ##conn.commit()
          #registros_insertados = cur.rowcount
          #print(f'Registros insertados {registros_insertados}')               
finally:
    conn.close()