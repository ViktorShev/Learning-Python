from dataclasses import dataclass
from typing import ClassVar, Collection


@dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int = 0


@dataclass(eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str
    contador_personas: ClassVar[int] = 0 

    def __post_init__(self):
        if not self.nombre: 
            raise ValueError(f'Valor de nombre vacio: {self.nombre}')

    domicilio: Domicilio

domicilio1 = Domicilio('Saturno', 15)
p1 = Persona('Juan', 'Perez', domicilio1)
print(f'{p1!r}')

# Variable de clase
print(f'Variable de clase: {Persona.contador_personas}')
# Variables de instancia
print(f'Variables de instancia: {vars(p1)}')
# Variable con valores vacios
p_vacia = Persona('Karla', '', domicilio=None)
print(f'Persona vacia: {p_vacia}')

# Revisar igualdad entre objetos (__eq__)
#p2 = Persona('Juan', 'Perez', Domicilio('Venus', 27))
p2 = Persona('Juan', 'Perez', Domicilio('Saturno', 15))
print(f'Objetos iguales en CONTENIDO? - {p1 == p2}')

# Agregar esta clase a una collecion
coleccion = {p1, p2}
print(coleccion)

# frozen=True (inmutable)
#coleccion[0].nombre = 'Juan Carlos'
#p1.nombre = 'Juan Carlos'