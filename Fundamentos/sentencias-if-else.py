condicion = False

print("Condicion verdadera") if condicion else print("Condicion falsa")

if condicion == True:
    print("La condicion es verdadera")
else:
    print("La condcion es falsa")
    
numero = int(input("Introduzca un numero entre 1 o 3: "))
if numero == 1:
    numeroTexto = "1"
elif numero == 2:
    numeroTexto = "2"
elif numero == 3:
    numeroTexto = "3"
else:
    numeroTexto = "Valor fuera de rango"
    
print("Numero proporicionado:", numeroTexto)
