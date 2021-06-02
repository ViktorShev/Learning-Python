from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
        
    def calcular_area(self):
        print(f'Area: {self._alto * self._ancho}')
    
    def __str__(self):
        return f'Longitud de los lados: {self._alto}, Color: {self._color}'
    
if __name__ == '__main__':
    t2 = Cuadrado(5, 'Rojo')
    t2.calcular_area()
    print(t2)