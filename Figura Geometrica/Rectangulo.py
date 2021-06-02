from FiguraGeometrica import *
from Color import *

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
        
    def calcular_area(self):
        print(f'Area: {self._alto * self._ancho}')
        
    def __str__(self):
        return f'Alto: {self._alto}, Ancho: {self._ancho}, Color: {self._color}'
 
if __name__ == '__main__':   
    t1 = Rectangulo(10, 2, 'Verde')
    t1.calcular_area()
    print(t1)