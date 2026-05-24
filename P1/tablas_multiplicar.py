'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''
def borrarPantalla():
    print("\033c")
borrarPantalla()

tabla = int(input("Ingresa un numero para mostrar su tabla de multiplicar: "))
num = 1

print(f"{tabla} x {num} = {tabla * num}")
num += 1
print(f"{tabla} x {num} = {tabla * num}")
num += 1
print(f"{tabla} x {num} = {tabla * num}")
num += 1
print(f"{tabla} x {num} = {tabla * num}")
num += 1
print(f"{tabla} x {num} = {tabla * num}")
num += 1
print(f"{tabla} x {num} = {tabla * num}")
num += 1
print(f"{tabla} x {num} = {tabla * num}")
num += 1
print(f"{tabla} x {num} = {tabla * num}")
num += 1
print(f"{tabla} x {num} = {tabla * num}")
num += 1
print(f"{tabla} x {num} = {tabla * num}")
num += 1
input("")
borrarPantalla()
'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control
  2.- Sin funciones

'''
tabla = int(input("Ingresa un numero para mostrar su tabla de multiplicar: "))

for i in range(1, 11):
    print(f"{tabla} x {i} = {tabla * i}")

input("")
borrarPantalla()

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control solo while
  2.- Sin funciones

'''

tabla = int(input("Ingresa un numero para mostrar su tabla de multiplicar: "))
num = 1

while num <= 11:
    print(f"{tabla} x {num} = {tabla * num}")
    num += 1

input("")
borrarPantalla()

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control solo while
  2.- Con funciones

'''
def mostrarTabla(n, num_tabla):
    print(f"{num_tabla} x {n} = {num_tabla * n}")
    n += 1
    return n

num = 1
tabla = int(input("Ingresa un numero para mostrar su tabla de multiplicar: "))

num = mostrarTabla(num, tabla)
num = mostrarTabla(num, tabla)
num = mostrarTabla(num, tabla)
num = mostrarTabla(num, tabla)
num = mostrarTabla(num, tabla)
num = mostrarTabla(num, tabla)
num = mostrarTabla(num, tabla)
num = mostrarTabla(num, tabla)
num = mostrarTabla(num, tabla)
num = mostrarTabla(num, tabla)

input("")
borrarPantalla()

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control
  2.- Con funciones

'''
def mostrarTabla(num_tabla, n):
    print(f"{num_tabla} x {n} = {num_tabla * n}")

tabla = int(input("Ingresa un numero para mostrar su tabla de multiplicar: "))

for i in range(1, 11):
    mostrarTabla(tabla, i)
