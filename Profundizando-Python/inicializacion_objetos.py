# Orden de inicializacion de objetos

class Padre:
    
    def __init__(self):
        print('Inicializador Padre')

    def metodo(self):
        print('Metodo padre')


class Hijo(Padre):

    # Se manda a llamar el metodo __init__ de la clase padre
    # siempre y cuando la clase hija no defina su propio metodo __init__

    # Definimos el metodo __init__
    def __init__(self):
        # De manera opcional podemos llamar al metodo __init__ de la clase padre (super)
        print('Inicializador Hijo')
        super().__init__()

    # sobreescribimos el metodo heredado de clase padre
    def metodo(self):
        print('Metodo sobreescrito hijo')
        super().metodo()

#padre1 = Padre()
#padre1.metodo()

hijo1 = Hijo()
hijo1.metodo()