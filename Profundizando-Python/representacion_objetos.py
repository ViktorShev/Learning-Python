# Representacion de objetos (str, repr, format)
#print(dir(object))

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # repr, mas enfocado a los programadores
    def __repr__(self):
        return f'{self.__class__.__name__}(nombre={self.nombre}, apellido={self.apellido})'

    # str, es mas para el usuario final o inclusive otros sistemas
    # la implementacion por default llama al metodo repr

    def __str__(self):
        return f'{self.__class__.__name__}: {self.nombre} {self.apellido}'

    # format (su implementacion por default es el metodo __str__ y se manda a llamar al usar f-string)
    # esta mas orientado al usuario final
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre {self.nombre} y apellido {self.apellido}'

p1 = Persona('Juan', 'Perez')
# repr (!r) (al llamar print sin tener el metodo str sobre escrito, print llama str, el cual implicitamente llama al metodo __repr__)
print(f'Mi objeto persona1: {p1!r}')

# str (de manera automatica el metodo print llama al metodo str)
print(p1.__str__()) # = print(p1)
print(p1.__repr__())

# format (si no esta sobre escrito, llama implicitamente al metodo __str__)
print(f'{p1}') # = print(f'{p1.__format__()}')