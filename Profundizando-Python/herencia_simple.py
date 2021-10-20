# Ejemplo de herencia simple

class ListaSimple:
    def __init__(self, elemetos):
        self._elementos = list(elemetos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, i):
        return self._elementos[i]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r})'

class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
        # Ordenamos siempre los elementos una vez inicializados
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        # Ordenamos el nuevo elemento
        self.ordenar()

class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        # una vez validados los elementos los agregamos
        super().__init__(elementos)

    def _validar(self, elemento):
        if not isinstance(elemento, int):
            raise ValueError(f'El elemento no es un entero: {elemento}')

    # Sobreescribimos el elemento agregar de la clase padre
    def agregar(self, elemento):
        self._validar(elemento)
        super().agregar(elemento)

# Lista simple
lista_simple = ListaSimple([5,3,6,8])
print(lista_simple)

# Lista ordenada
lista_ordenada = ListaOrdenada([4,3,6,9,10,-1])
print(lista_ordenada)
lista_ordenada.agregar(-14)
print(lista_ordenada)
print(len(lista_ordenada))

# Lista enteros
lista_enteros = ListaEnteros([0, 3, 1, 2])
print(lista_enteros)