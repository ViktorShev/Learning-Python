#Tupla mantiene el orden, pero ya no se puede modificar (inmutable)
frutas = ("Naranja", "Platano", "Guayaba")
print(frutas)
#largo de la tupla
print(len(frutas))
#accediendo a un elemento
print(frutas[2])
#navegacion inversa
print(frutas[-1])
#rango
print(frutas[0:2]) #excluyendo el indice 2
#modificar un valor
#frutas[0] = "Naranjita"
frutasLista = list(frutas)
frutasLista[1] = "Platanito"
frutas = tuple(frutasLista)
del frutasLista
print(frutas)
#iterar una tupla
for fruta in frutas:
    print(fruta,end=" ")
#no podemos agregar ni eliminar elementos de una tupla
del frutas
print(frutas)