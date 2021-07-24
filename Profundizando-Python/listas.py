# Profundizando en listas
# Listas son mutables


#nombres1 = ['Juan', 'Karla', 'Pedro']
#nombres2 = 'Laura Maria Gonzalo Ernesto'.split()

# Sumar listas
#print(f'Sumar listas: {nombres1 + nombres2}')

# Extender una lista con otra lista
#nombres1.extend(nombres2)
#print(f'Extender la lista1: {nombres1}')

# .index() obtiene el indice de la primera coincidencia proporcionada, es decir que en caso de tener valores repetido se va a devolver
# el indice de la primera occurencia y no todas. (Se lee de izquierda a derecha)
#numeros1 = [1, 2, 3, 4 , 5, 3, 2]
#print(f'Lista original: {numeros1}')
#help(list.index)
#print(f'Indice del numero 3: {numeros1.index(3)}')

# .reverse() Invertir el orden de los elementos de una lista
#numeros1.reverse()
#print(f'Lista invertida: {numeros1}')

# .sort() Ordenar los elementos de una lista de forma ascendente y descendete\
#numeros1.sort()
#print(f'Lista ordenada (ascendente): {numeros1}')

# .sort(reverse=True) Ordenar de manera descententemente
#numeros1.sort(reverse=True)
#print(f'Lista ordenada (descendente): {numeros1}')

# min() / max() Obtener el valor minimo y maximo de una lista
#print(f'Valor minimo: {min(numeros1)}')
#print(f'Valor maximo: {max(numeros1)}')

# Copiar los elementos de una lista
# .copy() solamente hace una copia superficial de una lista, es decir no copia los objetos o valores, sino copia las referencias de los valores en memoria 
# y regresa un objeto DISTINTO del original en memoria, es decir, el objeto retornado es nuevo con su propia referencia en memoria
#numeros2 = numeros1.copy()
#help(list.copy)
#print(numeros1)
#print(numeros2)
#print(f'Misma referencia?: {numeros1 is numeros2}')
#print(f'Mismo contenido? {numeros1 == numeros2}')

#  Podemos utilizar el constructor de la lista
#  mismo comportamiento que .copy()
#numeros2 = list(numeros1)
#print(f'Misma referencia?: {numeros1 is numeros2}')
#print(f'Mismo contenido? {numeros1 == numeros2}')

#  Slicing
#numeros2 = numeros1[:]
#print(f'Misma referencia?: {numeros1 is numeros2}')
#print(f'Mismo contenido? {numeros1 == numeros2}')

# Multiplicacion de listas
# Todos los objetos multiplicados dentro de la lista tienen la misma referencia a mememoria
#lista_multiplicacion = 5*[[2, 5]]
#print(lista_multiplicacion)
#print(f'Misma referencia en memoria?: {lista_multiplicacion[0] is lista_multiplicacion[1]}')
#print(f'Misma contenido?: {lista_multiplicacion[0] == lista_multiplicacion[1]}')

# Al ser todos los objetos la misma referencia en memoria, al modificar uno, se modifican todos
#lista_multiplicacion[2].append(10)
#print(lista_multiplicacion)

# Matrices en Python
#matriz = [
#    [10, 20], 
#    [30, 40, 50], 
#    [60, 70, 80, 90]
#]
#print(f'Matriz original: {matriz}')
#print(f'Renglon 0, Columna 0: {matriz[0][0]}')
#print(f'Renglon 2, Columna 3: {matriz[2][3]}')
#matriz[2][0] = 65
#print(f'Matriz modificada: {matriz}')

# Ordenar una matriz
#lista_listas = [[10, 14, 87, 90, 71], [4, 5, 6, 7], [9, 0, 11, 15, 45, 61, 70]]
#lista_listas.sort(key=len)
#print(f'Ordenar lista: {lista_listas}')

# sorted built-in
#help(sorted)
nombres1 = ['Juan Carlos', 'Karla', 'Pedro', 'Esperanza']
nombres1 = sorted(nombres1)
print(nombres1)

# ordenar de manera descendiente
nombres1 = sorted(nombres1, reverse=True)
print(nombres1)

# ordenar por la cantidad de caracteres (largo)
nombres1 = sorted(nombres1, key=len)
print(nombres1)

# built-in reversed
nombres1 = reversed(nombres1)
print(list(nombres1))
