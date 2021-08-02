from DE import DispositivoEntrada
from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor
from Computadora import Computadora


class Orden:
    idOrden = 0
    
    @classmethod
    def __generar_id_orden(cls):
        cls.idOrden += 1
        return cls.idOrden
    
    def __init__(self, *computadoras):
        self.__id = Orden.__generar_id_orden()
        self._lista_orden = list(computadoras)
        
    @property
    def orden_id(self):
        return self.__id
    
    def agregar_computadora(self, *computadoras):
        self._lista_orden.extend(computadoras)
    
    def __str__(self):
        orden_str = ''
        for computadora in self._lista_orden:
            orden_str += computadora.__str__()
            
        return f'Orden #{self.__id}: \n{orden_str}'
