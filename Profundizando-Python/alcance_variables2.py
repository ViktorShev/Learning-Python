# Mas de funciones anidadas y alcance de variables

def funcion_externa():
    variable_local_externa = 'Variable local externa'
    
    def nested():
        variable_local_anidada = 'Variable local anidada'

        nonlocal variable_local_externa # Se utiliza para trabajar con variables locales mas externas a la funcion anidada, esto es para que no se cree otra variable
        # local dentro de la funcion anidada, esto es parecido a "global" pero a un nivel local
        variable_local_externa = 'Nuevo valor variable local externa definida desde una funcion anidada'
    
    nested()

    print(f'Valor variable local externa: {variable_local_externa}')
    #print(f'Valor variable local a la funcion anidada: {variable_local_anidada}') No es posible acceder a una variable local mas interna

funcion_externa()
        