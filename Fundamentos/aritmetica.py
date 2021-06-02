class Aritmetica:
    """Clase Aritmetica para realizar las operaciones de suma, resta, etc"""
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
    def sumar(self):
        """Se realiza la operacion con los atributos de la clase"""
        return self.operando1 + self.operando2
    
    def restar(self):
        return self.operando1 - self.operando2
    
    def multip(self):
        return self.operando1 * self.operando2
    
    def div(self):
        return self.operando1 // self.operando2
    
    def pow(self):
        return self.operando1 ** self.operando2
   
#Creamos un objeto

suma = Aritmetica(4, 2)
print('Resultado de la suma es:', suma.sumar())

resta = Aritmetica(4, 2)
print('El resultado de la resta es:', resta.restar())

multiplicacion = Aritmetica(4, 2)
print('El resultado de la multiplicacion es:', multiplicacion.multip())

division = Aritmetica(4, 2)
print('El resultado de la division es:', division.div())

poder = Aritmetica(4, 2)
print('El resultado del poder es:', poder.pow())