from DE import DispositivoEntrada as DE


class Raton(DE):
    idRaton = 0
    
    @classmethod
    def __generar_id_raton(cls):
        cls.idRaton += 1
        return cls.idRaton
    
    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        self.__id = Raton.__generar_id_raton()
        
    @property
    def raton_id(self):
        return self.__id
        
    def __str__(self):
        return f'[ID: {self.__id}] {super().__str__()}'
    