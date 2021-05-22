a = 4
b = 2

resultado = a == b
#print(resultado)

resultado1 = a != b
#print(resultado1)

resultado2 = a > b
#print(resultado2) 

resultado3 = a >= b 
#print(resultado3)

resultado4 = a < b
#print(resultado4)

resultado5 = a <= b
#print(resultado5)

if a%2 == 0:
    print("Es par")
else:
    print("Es impar")
    
edadLimite = 18
edadPersona= int(input("Introduzca su edad: "))
if edadPersona >= edadLimite:
    print("Es mayor de edad")
else:
    print("Es menor de edad")