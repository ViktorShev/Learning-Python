class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo
        
    def CalcVolumen(self):
        return self.ancho * self.alto * self.profundo
    
ancho = int(input('Proporcione el ancho del cubo: '))
alto = int(input('Proporcione el alto del cubo: '))
profundo = int(input('Proporcione la profundidad del cubo: '))

cubo = Cubo(ancho, alto, profundo)
print('El volumen del cubo es:', str(cubo.CalcVolumen()) + 'cm2')