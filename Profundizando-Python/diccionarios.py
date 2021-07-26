# Profundizando en diccionarios

# Los diccionarios guardan un order (a diferencia de un set)
dict = {
    'Nombre': 'Juan',
    'Apellido': 'Perez',
    'Edad': 28
} 
print(dict)

# Los diccionarios son mutables, pero las llaves deben ser immutables
#dicc = {[1,2]: 'Valor1}
#dicc = {(1,2): 'Valor1'}

# Se agrega una llave si no se encuentra 
dict['Departamento'] = 'Sistemas'
print(dict)

# No hay valores duplicados en las llaves de un diccionario, pero si se admiten duplicaciones en los valores
# Si la llave ya existe, se reemplaza
dict['Nombre'] = 'Juan Carlos'
print(dict)

# Recuperar un valor indicando una llave
print(dict['Nombre'])

# Si no se encuentra la llave se lanza una excepcion
#print(dict['nombre'])

# Metodo .get() recupera una llave, y si no existe no lanza excepcion
# Ademas podemos regresar un valor en caso de que no exista la llave
print(dict.get('Nombres', 'No se encontro la llave'))
print(dict)

# .setdefault() si modifica el diccionario en caso de no encontrar una llave, ademas se agrega un valor por default
nombre = dict.setdefault('Nombres', 'Valor por default')
print(nombre)
print(dict)

# imprimir con pprint
from pprint import pprint as pp
#help(pp)
pp(dict, sort_dicts=False)