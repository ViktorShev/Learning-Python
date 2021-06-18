from NumerosIdenticosException import NumerosIdenticosException


resultado = None
try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if a == b:
        raise NumerosIdenticosException('Los numeros son iguales')
    resultado = a/b  
except ZeroDivisionError as zde:
    print(f'ZeroDivisionError - Ocurrio un error: {zde}, {type(zde)}')
    
except TypeError as te:
    print(f'TypeError - Ocurrio un error: {te}, {type(te)}')
       
except Exception as e:
    print(f'Exception - Ocurrio un error: {e}, {type(e)}')
else:
    print('No se arrojo ninguna excepcion')
finally:
    print('Ejecucion del bloque finally')
    
print(f'Resultado: {resultado}')
print('Continuamos...')