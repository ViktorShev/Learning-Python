#set es una coleccion sin orden y tampoco tienen indices, no permite elementos repetidos
#y los elementos no se pueden modificar, pero si agregar o eliminar
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)
#largo
print(len(planetas))
#revisar si un elemento esta presente
print("Marte" in planetas)
#agregar
planetas.add("Tierra")
print(planetas)
planetas.add("Tierra") #no se pueden agregar elementos duplicados
print(planetas)
#eliminar con remove posibilemente arroja una excepcion si el elemento no existe
planetas.remove("Tierra")
print(planetas)

#planetas.remove("Tierra")
#print(planetas)

#eliminar con discard no arroja una excepcion si el elemento no existe
planetas.discard("Jupiters")
print(planetas)

planetas.discard("Jupiter")
print(planetas)

#limpiar el set
planetas.clear()
print(planetas)
#eliminar el set
del planetas
print(planetas)