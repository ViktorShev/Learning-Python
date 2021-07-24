# * desempaquetar
numeros = [1, 2, 3]
print(numeros)
print(*numeros)
print(*numeros, sep=' - ')

# Desempaquetando a la hora de pasar un parametro a una funcion
def suma(a, b, c):
    print(f'Resultado de la suma: {a + b + c}')

suma(*numeros)

# Extraer algunas partes de una lista (o cualquier itreable)
mi_lista = list(range(1,7))
a, *b, c, d = mi_lista
print(a, b, c, d)

# Unir listas 
lista1 = list(range(1,4))
lista2 = list(range(4,7))
lista3 = [lista1, lista2]
print(f'Lista de listas: {lista3}')
lista3 = [*lista1, *lista2]
print(f'Unir listas: {lista3}')

# Unir diccionarios
dict1 = {
    'A': 1,
    'B': 2,
    'C': 3
}

dict2 = {
    'D': 4,
    'E': 5
}
dict3 = {
    **dict1,
    **dict2
}
print(f'Unir diccionarios: {dict3}')

# Construir una lista a partir de un str
lista = [*'HolaMundo']
print(lista)
print(*lista, sep='')