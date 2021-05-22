class Caja:
    def __init__(self, base, altura, ancho):
        self.base = base
        self.altura = altura
        self.ancho = ancho
    def CalcVolumen(self):
        return self.base * self.altura * self.ancho

base = int(input('Introduzca la base de la caja: '))
altura = int(input('Introduzca la altura de la caja: '))
ancho = int(input('Introduzca el ancho de la caja: '))

caja = Caja(base, altura, ancho)
print('El volumen de la caja es:', str((caja.CalcVolumen())) + 'cm2')