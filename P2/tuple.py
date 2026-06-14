"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""
print("\033c")

paises = ("México", "Brasil", "España", "Canada", "Canada")
print(paises)
posicion = paises.index("España")
print(posicion)

varios = (True, "UTD", 33, 3, 3.14, 33)
print(varios)
print(varios[1])
cuantos = varios.count(33)

print(cuantos)