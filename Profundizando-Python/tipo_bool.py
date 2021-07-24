# bool contiene los valores de True y False.
# Tipos numericos, False para 0 y True para los demas valores (se aplica a float)

#valor = 0.
#resultado = bool(valor)
#print(f'Valor: {valor}, RESULTADO: {resultado}')
#
#valor = 15
#resultado = bool(valor)
#print(f'Valor: {valor}, RESULTADO: {resultado}')


# Tipo str, False para '', True para los demas valores.
#valor = ''
#resultado = bool(valor)
#print(f'Valor: {valor}, RESULTADO: {resultado}')
#
#valor = 'Hola'
#resultado = bool(valor)
#print(f'Valor: {valor}, RESULATDO: {resultado}')


# Tipo colecciones, False para colecciones vacias, True para todas las demas colecciones.
#Lista
#valor = []
#resultado = bool(valor)
#print(f'Valor: {valor}, RESULTADO: {resultado}')
#
#valor = [2, 3, 4]
#resultado = bool(valor)
#print(f'Valor: {valor}, RESULTADO: {resultado}')

# Tupla
#valor = ()
#resultado = bool(valor)
#print(f'Valor: {valor}, RESULTADO: {resultado}')
#
#valor = (2, 3, 4)
#resultado = bool(valor)
#print(f'Valor: {valor}, RESULTADO: {resultado}')

#Diccionario
#valor = {
#    
#}
#resultado = bool(valor)
#print(f'Valor: {valor}, RESULTADO: {resultado}')
#
#valor = {
#    'DB': 'Database',
#    'PK': 'Primary Key'
#}
#resultado = bool(valor)
#print(f'Valor: {valor}, RESULTADO: {resultado}')


# Al utilizar if, implicitamente se llama el constructor bool.
variable = 0

#if bool(variable):
#    print('Regreso verdadero')
#else:
#    print('Regreso falso')
#    
#if variable:
#    print('Regreso verdadero')
#else:
#    print('Regreso falso')
    
# Al utilizar while, implicitamente se llama el constructor bool.
    
while variable:
    print('Ejecucion ciclo while')
    break
else:
    print('Fin del ciclo while')
    
while bool(variable):
    print('Ejecucion ciclo while')
    break
else:
    print('Fin del ciclo while')