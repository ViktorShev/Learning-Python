class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def CalcArea(self):
        return self.base * self.altura
    
base = int(input('Introduzca la base del rectangulo: '))
altura = int(input('Introduzca la altura del rectangulo: '))
areaRectangulo = Rectangulo(base, altura)
print('El area del rectangulo es:', str(areaRectangulo.CalcArea()) + 'cm2')