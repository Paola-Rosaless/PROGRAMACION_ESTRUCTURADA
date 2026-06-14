"""
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""


#Funciones más comunes en las listas
print("\033c")
paises = ["México", "Canada", "EUA", "México", "Brasil",]
numeros = [23, 45, 8, 24]
varios = [33, 3.1416, "hola", True]
vacio = []


#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)
print(vacio)
print(paises[1])

#Recorrer la lista
#1er forma
for i in paises:
    print(i)

#2do forma
for i in range(0, 5):
    print(paises[i])


#ordenar elementos de una lista
paises = ["México", "Canada", "EUA", "México", "Brasil",]
print(paises)
paises.sort()
print(paises)

#dar la vuelta a una lista
paises.reverse()
print(paises)


paises = ["México", "Canada", "EUA", "México", "Brasil",]
print(paises)
#Agregar, insertar, Añadir un elemento a una lista
#1er forma
paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1, "Argentina")
print(paises)
paises.insert(100, "Panama")
print(paises)

#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
paises.pop(4)
print(paises)

#2da forma
paises.remove("EUA")
print(paises)

#Buscar un elemento dentro de la lista
buscar = "Brasil" in paises
print(buscar)

#Contar el numeros de veces que aparece un elemento dentro de una lista
numeros = [23, 45, 24, 8, 23, 50,23]
num = int(input("Ingrese el numero a contar: "))
print(f"El numero {num} aparece: {numeros.count(num)} veces")

#Conocer la posicion o indice en el que se encuentra un elemento de la lista
posicion = numeros.index(50)
print(f"Estoy en la posicion: {posicion}")

#Unir el contenido de una lista dentro de otra lista
numeros1 = [23, 45, 24, 8, 23, 50,23]
print(numeros1)
numeros2 = [100, -100]
print(numeros2)
numeros1.extend(numeros2)
print(numeros1)

#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente
print(numeros1)
print(numeros2)

numeros1.extend(numeros2)
numeros1.sort()
numeros1.reverse()
print(numeros1)