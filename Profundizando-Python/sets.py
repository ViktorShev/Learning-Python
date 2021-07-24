# Profundizar en set
# Un set es una coleccion de elementos unicos y es mutable
# Los elementos de un set deben ser inmutables
#conjunto = {[1,2], [3,4]} #error
conjunto = {'Juan', True, 18.6}
print(conjunto)
 
# Set vacio
#conjunto = {} es un diccionario, no un set
#print(type(conjunto))

# set vacio correcto
conjunto = set()
print(conjunto)
print(type(conjunto))

# Mutable
conjunto.add('Juan')
print(conjunto)

# Contiene valores unicos
conjunto.add('Juan')
print(conjunto)

# Crear un set a partir de un iterable
conjunto = set([4,5,7,8,4])
print(conjunto)

# Podemos agregar mas elementos o incluso otro set
conjunto2 = {100,200,300,300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,40])
print(conjunto)

# Copiar un set (copia poco profunda)
conjunto_copia = conjunto.copy()
print(conjunto_copia)
print(f'Es la misma referencia en memoria: {conjunto_copia is conjunto}')
print(f'Es igual en contenido: {conjunto_copia == conjunto}')

# Operaciones de conjuntos con set
# Personas con distintas caracteristicas
pelo_negro = {'Juan', 'Karla', 'Pedro', 'Maria'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_cafe = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'Maria'}

# Todos los elementos con ojos_cafe y pelo_rubio (Union) (No se repiten los elementos)
print(ojos_cafe.union(pelo_rubio))
# Invertir el orden con el mismo resultado (conmutativa)
print(pelo_rubio.union(ojos_cafe))

# (intersection) (conmutativa) Solo las personas con ojos_cafe y pelo rubio
print(ojos_cafe.intersection(pelo_rubio))

# (difference) Pelo negro pero sin ojos cafe (no conmutativa)
# las personas que se encuentran en el primer set pero no en el segundo
print(pelo_negro.difference(ojos_cafe))

# (symmetric difference) Pelo negro u ojos cafe, pero NO ambos (conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))

# Preguntar si un set esta contenido en otro (subset)
# revisamos si los elementos del primer set estan contenidos en el segundo set
print(menores_30.issubset(pelo_negro))

# Preguntar si un set contiene a otro set (superset)
# revisar si los elementos del primer set estan contenidos en el primer set
print(menores_30.issuperset(pelo_negro))

# Preguntar si los de pelo negro no tienen pelo rubio (disjoint)
print(pelo_negro.isdisjoint(pelo_rubio))