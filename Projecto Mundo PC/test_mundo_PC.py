from DE import DispositivoEntrada
from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor
from Computadora import Computadora
from Orden import Orden


monitor1 = Monitor('AOC', '24')
teclado1 = Teclado('USB', 'Razer')
raton1 = Raton('Wireless', 'Logitech')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

monitor2 = Monitor('Acer', '27')
teclado2 = Teclado('Wireless', 'Hyperx')
raton2 = Raton('USB', 'ZET')
computadora2 = Computadora('ThermalTake', monitor2, teclado2, raton2)

monitor3 = Monitor('ASUS', '27')
teclado3 = Teclado('USB', 'ZET')
raton3 = Raton('Wireless', 'Razer')
computadora3 = Computadora('ASUS', monitor3, teclado3, raton3)

monitor4 = Monitor('HP', '21')
teclado4 = Teclado('Wireless', 'Ducky')
raton4 = Raton('Wireless', 'Razer')
computadora4 = Computadora('Acer', monitor4, teclado4, raton4)

orden1 = Orden(computadora1, computadora2)
orden1.agregar_computadora(computadora3, computadora4)
print(orden1)