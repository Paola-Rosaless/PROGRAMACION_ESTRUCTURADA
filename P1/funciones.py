
"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""
#procedimiento que borre pantalla 
def borrarPantalla():
    print(f"\033c")

#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
    nombre = input("Escribe el nombre: ").strip().upper()
    apellido = input("Escribe los apellido: ").strip().upper()
    print(f"El nombre completo del alumno es: {nombre} {apellido}")

funcion1()
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

#Invocar las funciones
funcion1()

nombre = input("Escribe el nombre: ").strip().upper()
apellido = input("Escribe los apellido: ").strip().upper()
funcion3(nombre, apellido)

nom, ape = funcion2()
print(f"El nombre completo del alumno es: {nom} {ape}")

nombre = input("Escribe el nombre: ").strip().upper()
apellido = input("Escribe los apellido: ").strip().upper()
nom, ape = funcion4(nombre, apellido)
print(f"El nombre completo del alumno es: {nom} {ape}")