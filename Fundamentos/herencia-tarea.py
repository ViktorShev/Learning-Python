class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return 'Color: ' + self.color + ', ruedas: ' + str(self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        
    def __str__(self):
        return super().__str__() + ', velocidad: ' + str(self.velocidad)
        

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, velocidad, tipo):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.tipo = tipo
        
    def __str__(self):
        return super().__str__() + ', velocidad: ' + str(self.velocidad) + ', tipo: ' + self.tipo
    
vehiculo = Vehiculo('Azul', 4)
print(vehiculo)

coche = Coche('Azul', 4, 200)
print(coche)

bicicleta = Bicicleta('Negra', 2, 20, 'Montaña')
print(bicicleta)                                                   