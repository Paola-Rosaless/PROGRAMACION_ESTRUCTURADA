def limpiar_pantalla():
    print("\033c")

#El porcentaje se pone como decimal, por ejemplo el 20% se pone como 0.2
def calcular_sueldo(horas_trabajadas, sueldo_hora, porcentaje):
    sueldo = (horas_trabajadas * sueldo_hora) + (porcentaje * horas_trabajadas * sueldo_hora)
    return sueldo

salir = "S"
trabajadores = 0
monto_total = 0

while salir == "S":
    limpiar_pantalla()

    nombre_trabajador = input("Ingrese el nombre del trabajador: ")
    horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
    sueldo_hora = float(input("Ingrese el sueldo por hora: "))

    if horas_trabajadas == 10:
        sueldo = calcular_sueldo(horas_trabajadas, sueldo_hora, 0.2)
    elif horas_trabajadas == 15:
        sueldo = calcular_sueldo(horas_trabajadas, sueldo_hora, 0.3)
    elif horas_trabajadas == 20:
        sueldo = calcular_sueldo(horas_trabajadas, sueldo_hora, 0.15)
    elif horas_trabajadas > 25:
        sueldo = calcular_sueldo(horas_trabajadas, sueldo_hora, 0.08)
    else:
        sueldo = calcular_sueldo(horas_trabajadas, sueldo_hora, 0)
    
    monto_total += sueldo
    trabajadores += 1
    print(f"El aumento a pagar es ${sueldo - (horas_trabajadas * sueldo_hora)} y el sueldo total a pagar es ${sueldo}")

    salir = input("Desea ingresar un nuevo trabajador? (s/n): ").upper().strip()


limpiar_pantalla()
print(f"El monto total a pagar por los ${monto_total}, los trabajadores son {trabajadores}")