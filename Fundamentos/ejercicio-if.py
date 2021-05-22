mes = int(input("Proporciona el mes del año (1-12): "))
estacion = None
MesMin = 1
MesMax = 12

if mes == 1 or mes == 2 or mes == 12:
    estacion = "Invierno"
elif mes == 3 or mes == 4 or mes == 5:
    estacion = "Primavera"
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "Verano"
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "Otoño"
else:
    estacion = "Mes no existe."

print("Estacion:", estacion + ",", "para el mes:", mes) if mes >= MesMin and mes <= MesMax else print(estacion)