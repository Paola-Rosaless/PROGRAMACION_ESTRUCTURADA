# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).

#procedimiento que borre pantalla 
def borrarPantalla():
    print(f"\033c")

#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
    nombre = input("Escribe el nombre: ").strip().upper()
    apellido = input("Escribe los apellido: ").strip().upper()
    print(f"El nombre completo del alumno es: {nombre} {apellido}")


 #3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nombre, apellidos):
    print(f"El nombre completo del alumno es: {nombre} {apellidos}")

 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
    nombre = input("Escribe el nombre: ").strip().upper()
    apellido = input("Escribe los apellido: ").strip().upper()
    return nombre, apellido

 #4.- Funcion que recibe parametros y regresa valor
def funcion4(nom, ape):
    nombre = nom.strip().upper()
    apellidos = ape.strip().upper()
    return nombre, apellidos