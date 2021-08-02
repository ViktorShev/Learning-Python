class Producto:
    contador_productos = 0
    
    @classmethod
    def generar_id_producto(cls):
        cls.contador_productos += 1
        return cls.contador_productos
    
    def __init__(self, nombre, precio):
        self._id_producto = Producto.generar_id_producto()
        self._nombre = nombre
        self._precio = precio
      
    @property  
    def precio(self):
        return self._precio
        
    def __str__(self):
        return f'ID del producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'

if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    print(producto1)
    producto2 = Producto('Pantalon', 150.00)
    print(producto2)