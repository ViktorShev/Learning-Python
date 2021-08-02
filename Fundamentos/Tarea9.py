def MultiplicarValores(*args):
    resultado = 1
    for valores in args:
        resultado *= valores
    return resultado

print(MultiplicarValores(1, 2, 3))
