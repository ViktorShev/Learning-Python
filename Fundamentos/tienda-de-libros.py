print("Proporcione los siguentes datos del libro:")

nombre = input("Proporcione el nombre: ")
id = int(input("Proporcione el ID del libro: "))
precio = float(input("Proporcione el precio del libro: "))
envioGratuito = input("Indique si el envio es gratuito (y/n): ")

print("Nombre:", nombre)
print("ID:", id)
print("Precio:", precio)

if envioGratuito == "y":
    print("El envio es gratuito")
elif envioGratuito == "n":
    print("El envio no es gratuito")
else:
    print("Valor invalido, debe ser True/False")