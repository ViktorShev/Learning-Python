list = ["juan", "carlos"]
while "juan" in list:
    print(list)
    list.insert(1, "viktor")
    if "viktor" in list:
        break

print(list)