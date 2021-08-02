#  Leer contenido online
from urllib.request import urlopen


with urlopen('https://globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
    contenido = mensaje.read().decode('utf-8')
    
# Contar ocurrencias de una cadena
#print('No. veces Universidad:', contenido.count('Universidad'))

# .upper() convierte a mayusculas un str
#print(contenido.upper())
#print(contenido)

# .lower() convierte a minusculas un str
#print(contenido.lower())

# Estos metodos sirven por ejemplo para estandarizar busquedas de str en archivos 
#print('Existe python?:', 'python'.lower() in contenido.lower())
#print('Existe python?:', 'Python'.upper() in contenido.upper())
#print(contenido.lower().count('python'))

# .startswith() - inicia con cierto str
#print('Inicia con:', contenido.startswith('En GlobalMentoring.com.mx'))
#print(contenido.upper().startswith('en globalmentoring.com.mx'.upper()))

# .endswith() - termina con cierto str
#print('Termina con:', contenido.endswith('GlobalMentoring.com.mx'))
#print('Termina con:', contenido.lower().endswith('GLOBALMENTORING.COM.MX'.lower()))

#mensaje = 'Hola Mundo'
#print(mensaje.islower())
#print(mensaje.isupper())

#print(mensaje.lower().islower())  # Devuelve true
#print(mensaje.upper().isupper())  # Devuelve true 


# Alinear cadenas

# Centrar un str .center()
titulo = 'Sitio Web de GlobalMentoring.com.mx'
#print(len(titulo))
#print(titulo.center(50, '*'))
#print(len(titulo.center(50, '*')))
#print(titulo.center(len(titulo)+10, '-'))

# .ljust() mueve el texto a la izquierda y rellena en la derecha
#print(titulo.ljust(len(titulo)+10, '-'))

# .rjust() mueve el texto a la derecha y rellena en la izquierda
#print(titulo.rjust(len(titulo)+10, '-'))


# Reemplazar contenido en un str
#print(contenido.replace(' ', '-'))

# .strip() elimina los caracteres al inicio y final de una cadena
titulo = ' *** GlobalMentoring.com.mx *** '
print('Cadena original:', titulo, len(titulo))
titulo = titulo.strip()
print('Cadena modificada:', titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.strip('*')
print('Cadena modificada:', titulo)
titulo = '***GlobalMentoring.com.mx***'.lstrip('*')
print('Cadena modificada:', titulo)
titulo = '***GlobalMentoring.com.mx***'.rstrip('*')
print('Cadena modificada:', titulo)
titulo = ' *** GlobalMentoring.com.mx *** '.strip().strip('*').strip()
print('Cadena modificada:', titulo)