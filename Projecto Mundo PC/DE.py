class DispositivoEntrada:
    def __init__(self, tipoEntrada, marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca
        
    @property
    def tipoEntrada(self):
        return self._tipoEntrada
        
    @property
    def marca(self):
        return self._marca
        
    @marca.setter
    def marca(self, marca):
        self._marca = marca
        
    @tipoEntrada.setter
    def tipoEntrada(self, entrada):
        self._tipoEntrada = entrada
    
    def __str__(self):
        return f'Tipo de entrada: {self._tipoEntrada}, marca: {self._marca}'
    
    def mostrar_detalle(self):
        return self.__str__()