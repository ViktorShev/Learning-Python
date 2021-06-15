from DE import DispositivoEntrada
from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor


class Computadora:
    idComputadora = 0
    
    @classmethod
    def __generar_id_computadora(cls):
        cls.idComputadora += 1
        return cls.idComputadora
    
    def __init__(self, nombre, monitor, teclado, raton):
        self.__id = Computadora.__generar_id_computadora()
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
        
    @property
    def computadora_id(self):
        return self.__id

    @property
    def monitor(self):
        return self._monitor
    
    @property
    def teclado(self):
        return self._teclado
    
    @property
    def raton(self):
        return self._raton
    
    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor
        
    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado
    
    @raton.setter
    def raton(self, raton):
        self._raton = raton
        
    def __str__(self):
        return f'\nNombre de la computadora: {self._nombre}\n    [ID de la computadora: {self.__id}] \n    Monitor: {self._monitor.mostrar_detalle()} \n    Teclado: {self._teclado.mostrar_detalle()} \n    Raton: {self._raton.mostrar_detalle()}\n'