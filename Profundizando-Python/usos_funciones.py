# Las funciones en python son ciudadanas de primeras clase
# First class citizens

# Definimos la funcion
def sumar(a, b):
    return a + b

# 1. Asignar una funcion a una variable (no se usan parentesis) ya que se esta asignando la referencia a la funcion, no queremos ejecutarla
mi_func = sumar

# Verificar el tipo de la variable
print(type(mi_func))

# LLamamos la funcion a traver de la variable
resultado = mi_func(5,8)
print(resultado)

# 2. Funcion como argumento
def operacion(a, b, sumar_arg):
    print(f'Resultado de sumar: {sumar_arg(a, b)}')

operacion(4, 5, sumar)

# 3. Podemos retornar una funcion
def retornar():
    # retornamos una funcion
    return sumar

func_retornada = retornar()
print(f'Resultado funcion retornada: {func_retornada(1,2)}')