# Generador de numeros del 1 al 5
def gen_num():
    for numero in range(1,6):
        yield numero
        print('Se reanuda la ejecucion de la funcion')

# Utilizamos el generador
generador = gen_num()
print(f'Objeto generator: {generador}')
print(type(generador))

# Consumimos los valores del generador
for valor in generador:
    print(f'Numero producido: {valor}')

# Consumir a demanda
print()
generador = gen_num()
try:
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
except StopIteration as e:
    print('Eror al cosumir generador', e)

# Otra forma de consumir un generador
generador = gen_num()
while True:
    try:
        valor = next(generador)
        print(valor)
    except StopIteration as e:
        print('Se termino de iterar el generador')
        break