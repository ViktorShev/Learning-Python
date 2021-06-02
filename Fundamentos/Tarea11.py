def imprimir_numeros(numero):
    if numero >= 1:
        print(numero)
        imprimir_numeros(numero-1)
        
imprimir_numeros(7)