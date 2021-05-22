#a = int(input("Introduzca un numero: "))
a = 3
valorMinimo = 0
valorMaximo = 5
dentroRango = a >=valorMinimo and a <= valorMaximo
#print(dentroRango)
if dentroRango == True:
    print("Dentro del rango")
else:
    print("Fuera del rango")
    
    
vacaciones = False
diaDescanso = True

if vacaciones or diaDescanso:
    print("Podemos ir al parque!")
else:
    print("No podemos ir al parque!")
    
#vacaciones = False
#diaDescanso = True

#if (not (vacaciones or diaDescanso)):
#    print("No podemos ir al parque")
#else:
#    print("Podemos ir al parque")
    
#print(not(vacaciones))