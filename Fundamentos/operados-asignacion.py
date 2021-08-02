x = int(input("Introduzca un numero: "))
print(x)

# x = x + 2
x += 2 
print(x)

# x = x - 1
x -= 1
print(x)

# x = x * 3
x *= 3
print(x)

y = x

x **= x
print(x)

x **= (1/x)
print(x)

x *= y

print(x)

x /= 3
print(x)