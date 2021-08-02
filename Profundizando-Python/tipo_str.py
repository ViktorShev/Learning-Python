# Profundizando en el tipo str

# Concatenacion automatica en Python
#variable = 'Adios'
#mensaje = 'Hola' 'Mundo' + variable
#mensaje += 'Universidad' 'Python'
#print(mensaje)

# Metodo help de cualquier clase, metodo, modulo, atributo, etc (en este caso el metodo help de la clase str)
# Y llama toda la documentacion de la clase (documentacion de los metodos, variables, parametros, etc)
#import math
#from mi_clase import MiClase

#help(str)
#help(str.capitalize)
#help(math)
#help(math.isnan)
#help(MiClase)

# Al imprimir el metodo x.__doc__, se imprime solo la descripcion (doc string) de la clase, no toda la documentacion.
# Para llamar documentacion de algun metodo dentro de la clase se debe hacer x.__metodo__.__doc__
#print(MiClase.__doc__)
#print(MiClase.__init__.__doc__)
#print(MiClase.mi_metodo.__doc__)

# Todo en Python es un objeto, hasta los metodos y funciones:
#print(MiClase.mi_metodo)
#print(type(MiClase.mi_metodo))

# Los tipos str son immutables, es decir no se pueden modificar una vez asignados
#mensaje1 = 'hola mundo'
#mensaje2 = mensaje1.capitalize()
#print(f'mensaje1: {mensaje1}, id: {hex(id(mensaje1))}')
#print(f'mensaje2: {mensaje2}, id: {hex(id(mensaje2))}')
#
#mensaje1 += 'adios'
#print(f'mensaje1: {mensaje1}, id: {hex(id(mensaje1))}')


# Metodo .join()

#help(str.join)

#tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')
#mensaje = ' '.join(tupla_str)
#print(f'Mensaje: {mensaje}')
#
#lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
#mensaje = ', '.join(lista_cursos)
#print(f'Mensaje: {mensaje}')
#
#cadena = 'HolaMundo'
#mensaje = '.'.join(cadena)
#print(f'Mensaje: {mensaje}')
#
#diccionario = {
#    'Nombre': 'Juan',
#    'Apellido': 'Perez',
#    'Edad': '18' #los valores numericos tienen que ser string o se deben convertir a string antes de join para que join funcione 
#}
#llaves = ' '.join(diccionario.keys())
#valores = ' '.join(diccionario.values())
#print(f'Llaves: {llaves}, type: {type(llaves)}')
#print(f'Valores: {valores}, type: {type(valores)}')


# Metodo .split() (inverso de .join)

#help(str.split)

#cursos = 'Java Python JavaScript Angular Spring Excel'
#lista_cursos = cursos.split()
#print(f'Lista cursos: {lista_cursos}')
#print(type(lista_cursos))

#cursos_separados_coma = 'Java, Python, JavaScript, Angular, Spring, Excel'
#lista_cursos = cursos_separados_coma.split(', ')
#print(f'Lista cursos: {lista_cursos}')
#print(len(lista_cursos))

#lista_cursos = cursos_separados_coma.split(', ', 3)
#print(f'Lista cursos: {lista_cursos}')
#print(len(lista_cursos))


# Dar formato a un str
#nombre = 'Juan'
#edad = 28
#mensaje_formato = 'Mi nombre es %s y tengo %d años' % (nombre, edad)
#print(mensaje_formato)

#persona = ('Karla', 'Gomez', 5000.00)
# mensaje_formato = 'Hola %s %s. Tu sueldo es: %.2f' % persona
# print(mensaje_formato)
#mensaje_formato = 'Hola %s %s. Tu sueldo es: %.2f'
# print(mensaje_formato % persona)


# Metodo .format()
# Metodo format utiliza placeholders: {}, no argumentos posicionales: %s

#nombre = 'Juan'
#edad = 28
#sueldo = 3000
#mensaje = 'Nombre: {} Edad: {} Sueldo: {:.2f}'.format(nombre, edad, sueldo)
##print(mensaje)
#
#mensaje = 'Nombre: {0} Edad: {1} Sueldo: {2:.2f}'.format(nombre, edad, sueldo)
##print(mensaje)
#
#mensaje = 'Sueldo: {2:.2f} Edad: {1} Nombre: {0}'.format(nombre, edad, sueldo)
##print(mensaje)
#
#mensaje = 'Nombre: {n}, Edad: {e}, Sueldo: {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
##print(mensaje)
#
#dict = {
#    'nombre': 'Ivan',
#    'edad': 35,
#    'sueldo': 8000.00
#}
#
#mensaje = 'Nombre: {dic[nombre]}, edad: {dic[edad]}, sueldo: {dic[sueldo]:.2f}'.format(dic=dict)
#print(mensaje)


# Dar formato utilizando f-string o Template Literal
#nombre = 'Juan'
#edad = 28
#sueldo = 3000
#mensaje = f'Nombre: {nombre}, edad: {edad}, sueldo: {sueldo:.2f}'
#print(mensaje)
#
# Metodo print()
#print(nombre, edad, sueldo, sep=', ')

# Multiplicacion de str
#resultado = 3*'Hola'
#print(f'Resultado: {resultado}')

# Multiplicacion de tuplas
#resultado = 5*('Hola', 10)
#print(f'Resultado: {resultado}')

# Multiplicacion de listas
#resultado = 10*[0]
#print(f'Resultado: {resultado}, largo: {len(resultado)}')

# Caracteres de escape
#resultado = 'Hola \' Mundo'
#print(f'Resultado: {resultado}')

# Usar \ en un str
#resultado = 'c:\\directorio\\juan'
#print(f'Resultado: {resultado}')

  # Raw string
#resultado = r'Cadena con \n salto de linea' 
#print(f'Resultado: {resultado}')

# Caracteres Unicode
#print('Hola\u0020Mundo')
#print('Notacion simple:', '\u0041')
#print('Notacion extendida:', '\U00000041')
#print('Notacion hexadecimal:', '\x41')
#print('Corazon:', '\u2665')
#print('Cara sonriendo:', '\U0001f600')
#print('Serpiente:', '\U0001f40d')

  # Caracteres ASCII
#caracter = chr(65)
#print(f'A mayuscula: {caracter}')
#caracter = chr(64)
#print(f'Simbolo @: {caracter}')
#caracter = chr(97)
#print(f'A minuscula: {caracter}')

# Caracteres bytes
#caracteres_bytes = b'Hola Mundo'
#print(caracteres_bytes)

#mensaje = b'Universidad Python'
#print(mensaje[0])
#print(chr(mensaje[0]))
#
#lista_caracteres = mensaje.split()
#print(lista_caracteres)


# Convertir de str a bytes
#string = 'Programación con Python'
#print('String original:', string)
#
#bytes = string.encode('UTF-8')
#print('Bytes codificado:', bytes)
#
## Convertir de bytes a str
#string2 = bytes.decode('UTF-8')
#print('String decodificada', string2)
#
#print(string == string2)

lista = [(1,), (2,)]
a, b = lista
print(a)
print(b)