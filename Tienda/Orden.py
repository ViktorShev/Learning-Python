from Producto import Producto


class Orden:
    contador_ordenes = 0
   
    @classmethod
    def generar_id_orden(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes
    
    def __init__(self, *productos):
        self._id_orden = Orden.generar_id_orden()
        self._productos = list(productos)

    def agregar_producto(self, *productos):
        self._productos.extend(productos)
            
    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
            
        print(f'Total de la Orden #{self._id_orden}: {total}$')
    
    def __str__(self):
        productos_str = '' 
        for producto in self._productos:
            productos_str += producto.__str__() + '\n'
        return f'Orden #{self._id_orden}: \nProductos: {productos_str}'
        
    
if __name__ == '__main__':
    camisa = Producto('Camisa', 100.00)
    pantalon = Producto('Pantalon', 150.00)
    orden1 = Orden([camisa, pantalon])
    orden2 = Orden(pantalon)
    print(orden1)
    print(orden2)   