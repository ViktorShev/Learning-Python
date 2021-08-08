# Funciones lambda
# Son funciones anonimas, y son pequeñas (una linea de codigo)

# NO es posible asignar una funcion a una variable a la hora de definirla
# mi_func = def sumar(a, b): return a + b

# Con una funcion lambda(anonima, sin nombre, y una sola linea de codigo)
# No se necesita agregar parentesis para los parametros
# No se necesita usar la palabra return, pero si debe regresar una expresion valida

lambda_func = lambda a, b: a + b
result = lambda_func(4, 6)
print(f'Resultado de sumar: {result}')

# Funcion lambda que no recibe argumentos (debemos regresar una expresion valida)
lambda_func = lambda: 'Funcion sin argumentos'
print(f'Llamar funcion lambda sin argumentos: {lambda_func()}')

# Funcion lambda con parametros por default
lambda_func = lambda a=2, b=3: a + b
print(f'Resultado argumentos por default: {lambda_func()}')

# *args **kwargs en funciones lambda
lambda_func = lambda *args, **kwargs: len(args) + len(kwargs)
print(f'Resultado de argumentos variables: {lambda_func(1,2,3, a=5, b=6)}')

# Funciones lambda con argumentos, argumentos variables y valor por default
lambda_func = lambda a, b, c=1, *args, **kwargs: a + b + c + len(args) + len(kwargs)
print(f'Resultado funcion lambda: {lambda_func(1,1,1, 5,6,7, x=5, y=7)}')