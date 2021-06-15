class Monitor:
    idMonitor = 0
    
    @classmethod
    def __generar_id_monitor(cls):
        cls.idMonitor += 1
        return cls.idMonitor
    
    def __init__(self, marca, tamaño):
        self.__id = Monitor.__generar_id_monitor()
        self._marca = marca
        self._tamaño = tamaño
        
    @property
    def monitor_id(self):
        return self.__id
        
    @property
    def tamaño(self):
        return self._tamaño
    
    @property
    def marca(self):
        return self._marca
        
    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    def __str__(self):
        return f'[ID: {self.__id}] Tamaño: {self._tamaño}, marca: {self._marca}'

    def mostrar_detalle(self):
        return self.__str__()