def mi_funcion():
    print("Ejecutando mi funcion")

mi_funcion()
mi_funcion()
mi_funcion()

dict = {
    "Hola": "Como estas",
    "Bien": "Yo tambien"
}

for keys in dict:
    print(keys,end=(": "))
    print(dict[keys])
