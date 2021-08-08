# Alcance de variables (scope)

var_global = 'Variable global'

def imprimir():
    # Acceder a una variable global
    global var_global # Se utiliza cuando se quiere utilizar la variable global para lectura y escritura, ya que si a esta variable global se le asigna otro valor dentro de un
    # scope local, nos va a arrojar un error.
    print(f'Variable global desde funcion: {var_global}')
    # Definicion de variable local
    var_local = 'Variable local'
    print(f'Variable local desde funcion: {var_local}')
    var_global = 'Nuevo valor de la variable global'
    # Destruccion de la variable local (estas solo existen hasta el final de un bloque de codigo en el cual fueron definidas)
    # Las variables locales se pueden utilizar dentro de funciones anidadas (nested functions)
    def nested():
        print(f'Variable local dentro de la funcion anidada: {var_local}')
    
    nested()


imprimir()
print(f'Variable global fuera funcion: {var_global}')
#print(f'Variable local fuera funcion: {var_local}') Es vista como indefinida (undefined) ya que no es posible de acceder a variables local fuera del bloque en el que 
# se definieron