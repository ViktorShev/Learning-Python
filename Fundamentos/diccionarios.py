#un diccionario esta compuesto de (key,value)
diccionario = {
    "IDE": "Integrated Development Environment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System"
}

print(diccionario)

#largo
print(len(diccionario))
#acceder a un elemento
print(diccionario["IDE"])
#otra forma, mismo resultado
print(diccionario.get("IDE"))
#modificar valores
diccionario["IDE"] = "Integrated development environment"
print(diccionario)
#iterar 
for termino in diccionario:
    print(termino)
    
for termino in diccionario:
    print(diccionario[termino])
    
for valor in diccionario.values():
    print(valor)
#comprobar existencia de un elemento
print("IDE" in diccionario)

#agregar nuevos elementos
diccionario["PK"] = "Primary Key"
print(diccionario)

#remover elementos
diccionario.pop("DBMS")
print(diccionario)

#limpiar
diccionario.clear()
print(diccionario)

#eliminar por completo
del diccionario
print(diccionario)