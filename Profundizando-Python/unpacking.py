#x, y = 5, 12
# x = 5 ; y = 12
#print(f'x = {x}, y = {y}')
#x, y = y, x
#print(f'x = {x}, y = {y}')

#x, y, z = 77, 88, 99
#z, x, y = x, y, z
#print(x, y, z)

#a, b, c = '4 5 6'.split()
#print(a)
#print(b)
#print(c)

#my_list = [8, 9, 10]
#a, b, c = my_list
#print(a)
#print(b)
#print(c)

#tup = (25, 26, 27)
#a, b, c = tup
#print(a, b, c)


# Al asignar un conjunto de variables a una variable Python regresa una tupla. En caso de querer una lista se deben poner las variables en [] 
a, b, c = 8, 9, 10
var = a, b, c
print(var)
print(type(var))

def pack_it(*args):
    print(args)
    print(type(args))
    
x, y, z = 'Forest', 'Hill', 'High'
pack_it(x, y, z)
#
#def unpack_it(x, y):
#    print(x)
#    print(y)
#    
#args = ['Cullen', 'McDonough']
#unpack_it(*args)
#
def func(**losers): #**kwargs
    print(losers)
    print(losers['a'])
    print(type(losers))
#
#func(a='Edsel', b='Betamax', c='mGaetz')
#
#def func1(a, b, c):
#    print(a)
#    
losers = {
   'a': 'Edsel',
   'b': 'Betamax',
   'c': 'mGaetz'
}
func(**losers)


#def regresa_varios_datos():
#    return (1, 2, 3)
#
#valor1, valor2, valor3 = regresa_varios_datos()
#print(valor1, valor2, valor3)
#
#valor1, *valores_restantes = regresa_varios_datos()
#print(valor1, valores_restantes)

#help(str.partition)
hora, _, min = '17:20'.partition(':')
print(hora, min)