# Ejemplo atributos publicos, protegidos, privados

class MiClase:
    
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado

obj = MiClase('Valor publico', 'Valor protegido', 'Valor privado')

# Acceso al atributo publico
print(obj.publico)
# Modificar el atributo publico
obj.publico = 'Nuevo valor publico'
print(obj.publico)

print()

# Acceso al valor protegido
# Solo deberiamos accederlo dentro de la misma clase o clases hijas
print(obj._protegido)
# Modificar el atributo protegido
obj._protegido = 'Nuevo valor protegido'
print(obj._protegido)

print()

# Acceso al valor privado
# Solo deberiamos accederlo dentro de la misma clase
#print(obj.__privado) = AttributeError: 'MiClase' object has no attribute '__privado' es imposible de accederlo de forma directa
# pero, podemos accederlo de la siguente forma ya que a esto es a lo que lo convierte Python al definir un atributo privado
print(obj._MiClase__privado)
# Modificar el valor privado
obj._MiClase__privado = 'Nuevo valor privado'
print(obj._MiClase__privado)