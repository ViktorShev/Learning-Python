class Persona:
    contador_personas = 0
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Mostrar los atributos de un objeto
p1 = Persona('Juan', 'Perez')
print(p1.__dict__)

# Crear un atributo al vuelo
print(p1.contador_personas) # Accediendo al atributo de clase
# Pero no es posible modificarlo con el objeto, sino con la clase

p1.contador_personas = 10
print(p1.__dict__)

# El atributo anterior oculta al atributo de clase
print(Persona.contador_personas) # Accedemos al atributo de clase
print(p1.contador_personas) # Accedemos al atributo de p1

# Un segundo objeto
p2 = Persona('Karla', 'Gomez')
print(p2.__dict__)
print(p2.contador_personas)

# Asociar un atributo de clase al vuelo
Persona.contador2 = 20
print(Persona.contador2) 

# Tercer objeto
# Ahora se propaga a todos los objetos de clase Persona
p3 = Persona('Juan Caros', 'Nagera')
print(p3.contador2)
print(p2.contador2)
print(p1.contador2)