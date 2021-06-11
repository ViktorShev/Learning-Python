from Producto import Producto
from Orden import Orden


camisa = Producto('Camisa', 100.00)
pantalon = Producto('Pantalon', 150.00)
calcetines = Producto('Calcetines', 50.00)
blusa = Producto('Blusa', 70.00)

orden1 = Orden(camisa, pantalon)
orden1.agregar_producto(calcetines, blusa)

print(orden1)
orden1.calcular_total()

orden2 = Orden()
orden2.agregar_producto(blusa, camisa, pantalon)
print(orden2)
orden2.calcular_total()