# Expresion generadora (es un generador anonimo)


multiplicacion = (valor*valor for valor in range(4))
print(multiplicacion)
print(type(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
#print(next(multiplicacion))

# Tambien se puede pasar una expresion generadora a una funcion (sin parentesis)
import math
suma = sum(valor*valor for valor in range(4))
print(f'Resultado de la suma: {suma}')