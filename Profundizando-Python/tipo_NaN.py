# NaN = Not a Number (no es un numero)
# NaN no es sensible a mayusculas/minusculas (puede ser float('NaN', 'nan', 'nAn', 'NAN', 'Nan', 'naN'))
# NaN es un tipo de dato numerico indefinido
import math
from decimal import Decimal


a = float('NaN')
# print(f'a: {a}')
# print(f'Es NaN?: {math.isnan(a)}')

a = Decimal('NaN')
print(f'a: {a}')
print(f'Es NaN?: {math.isnan(a)}')
