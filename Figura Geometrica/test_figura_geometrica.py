from Cuadrado import *
from Rectangulo import *
from FiguraGeometrica import FiguraGeometrica

#No se puede instanciar una clase abstracta
#figura = FiguraGeometrica()

print('Creacion Objeto Cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(lado=5, color='Rojo')
cuadrado1.alto = 9
cuadrado1.ancho = 9
cuadrado1.calcular_area()
print(cuadrado1)

print('Creacion Objeto Rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(alto=9, ancho=8, color='Verde')
rectangulo1.alto = 15
rectangulo1.calcular_area()
print(rectangulo1)

#Se modifica el Method resolution order
print(Cuadrado.mro())