# Un closure es una funcion que define a otra, y ademas la regresa
# la funcion anidada puede acceder a las variables locales definidas en la funcion principal o externa

# Funcion principal/externa
#def operacion(a,b):
#    # Definimos la funcion interna/anidada/nested
#    def sumar():
#        return a + b
#
#    # Retornar la funcion
#    return sumar

def operacion(a,b):
    #1. definimos una funcion lambda interna/anidada/nested y la retornamos
    return lambda: a + b

closure_func = operacion(5,2)
print(type(closure_func))
print(f'Resultado de la funcion closure: {closure_func()}')

# Llamar la funcion regresada al vuelo
print(f'Resultado de la funcion closure pero ejecutada al vuelo: {operacion(2,3)()}')
