class MiClase:
    
    variable_clase = 'Valor variable clase'
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
        
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)
        
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)
        
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)
        
miObj1 = MiClase('variable_instancia')
miObj1.metodo_instancia()