from DE import DispositivoEntrada as DE


class Teclado(DE):
    idTeclado = 0
    
    @classmethod
    def __generar_id_teclado(cls):
        cls.idTeclado += 1
        return cls.idTeclado  
    
    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        self.__id = Teclado.__generar_id_teclado()
        
    @property
    def id_teclado(self):
        return self.__id
        
    def __str__(self):
        return f'[ID: {self.__id}] {super().__str__()}'
