import os 

 bus = [
    ['A0', 'A1', 'A2', 'A3'],
    ['B0', 'B1', 'B2', 'B3'],
    ['C0', 'C1', 'C2', 'C3'],
    ['D0', 'D1', 'D2', 'D3'],
    ['E0', 'E1', 'E2', 'E3']
]

asientos dispomible = []
asientos ocupados = []
pasaje comprado = []

def mostrar_bus():
    dibujar_bus = "----- BUS ------\n"
    for fila in bus:
        for asiento in fila:
            asientos.disponibles.append(asiento)
            if asiento in asiento_ocupados:
                 dibujar_bus += f"**{asiento}**"
            else: 
                dibujar_bus += f"| {asiento} |"
        dibujar bus += "\n"
        print(dibujar_bus)

def registrar_viaje():
    asiento = input("Seleccione uno de los asientos disponibles >  ")
                input("Asiento existe y esta disponible")
                asientos_ocupados.appen(asiento)

                origen = validar_origen()
                destino = input("Destino:  ")
                rut =     input("Rut:       ")
                nombre = input("Nombre:     ")
                apellido = input("Apellido:     ")
                direccion = input("Dirección:   ")
                telefono_emergencia = validar_telefono()

                pasaje_comprado.append(
                    [asiento, origen, destino, rut, nombre, apellido, direccion, telefono_emergencia]

                )

                input(f" Pasaje con asiento ")



def menu_general():
    os.system("cls")
    print("------MENÚ------")
    print("1.- Registrar viaje")
    print("2.- Mostrar Asiento")
    print("3.- Mostrar información de un viaje")
    print("4.- Mostrar información de TODOS los viajes")
    print("5.- Salir ")

    try: 
        opcion = int(input("Ingrese una opcion > "))
        if opcion > 0 and opcion 6 <: 
            return opcion 
        else:
            input("Opción fuera de rango, presiones enter > ")

    except:
        input("Opción no válida, presione enrer > ")

menu = True
while menu:
    opcion = menu_general() 
    if opcion == 1;
    mostrar_bus()
    registrar_viaje()
    if opcion == 2;
    input("Opción 2")
    if opcion == 3;
    mostrar_bus()
    mostrar_viaje()
    if opcion == 4;
    mostrar_todos_viajes()
    if opcion == 5;
    print("Salió del sistema, ADIOS")
    menu = False 

import datetime

class Viaje:
    def _init_(self, origen, destino):
        self.origen = origen
        self.destino = destino
        self.asientos = [[None for j in range(4)] for i in range(10)]
        self.precios = [25000 if i < 3 else 20000 if i < 6 else 15000 for i in range(10)]

    def registrar_reserva(self, fila, columna, rut, nombre, apellido, telefono):
        if self.asientos[fila][columna] is None:
            self.asientos[fila][columna] = {
                'rut': rut,
                'nombre': nombre,
                'apellido': apellido,
                'telefono': telefono
            }
            print(f"Reserva registrada en la fila {fila+1}, columna {columna+1}")
        else:
            print("El asiento ya está ocupado")

    def visualizar_asientos(self):
        for i, fila in enumerate(self.asientos):
            for j, asiento in enumerate(fila):
                if asiento is None:
                    print(f"Asiento disponible en la fila {i+1}, columna {j+1}")
                else:
                    print(f"Asiento reservado en la fila {i+1}, columna {j+1}")

    def mostrar_informacion_viaje(self, fila, columna):
        print(f"Origen: {self.origen}")
        print(f"Destino: {self.destino}")
        asiento = self.asientos[fila][columna]
        if asiento is not None:
            print(f"RUT: {asiento['rut']}")
            print(f"Nombre: {asiento['nombre']}")
            print(f"Apellido: {asiento['apellido']}")
            print(f"Teléfono: {asiento['telefono']}")
        else:
            print("El asiento está disponible")

    def mostrar_informacion_todos_los_viajes(self):
        for i, fila in enumerate(self.asientos):
            for j, asiento in enumerate(fila):
                if asiento is not None:
                    print(f"Asiento en la fila {i+1}, columna {j+1}:")
                    print(f"\tNombre: {asiento['nombre']}")
                    print(f"\tApellido: {asiento['apellido']}")

    def mostrar_ganancias_totales(self):
        total = 0
        cantidad_filas_1_3 = 0
        cantidad_filas_4_6 = 0
        cantidad_filas_7_10 = 0
        for i, fila in enumerate(self.asientos):
            for j, asiento in enumerate(fila):
                if asiento is not None:
                    total += self.precios[i]
                    if i < 3:
                        cantidad_filas_1_3 += 1
                    elif i < 6:
                        cantidad_filas_4_6 += 1
                    else:
                        cantidad_filas_7_10 += 1
        print("Tipo\t\tCantidad\tTotal")
        print(f"Primeras 3 filas\t{cantidad_filas_1_3}\t\t{cantidad_filas_1_3 * 25000}")
        print(f"Filas 4 a la 6\t{cantidad_filas_4_6}\t\t{cantidad_filas_4_6 * 20000}")
        print(f"Filas 7 a la 10\t{cantidad_filas_7_10}\t\t{cantidad_filas_7_10 * 15000}")
        print(f"Total\t\t{cantidad_filas_1_3 + cantidad_filas_4_6 + cantidad_filas_7_10}\t\t{total}")

def validar_rut(rut):
    try:
        rut = int(rut)
    except ValueError:
        return False
    return True

def validar_fila_columna(fila, columna):
    try:
        fila = int(fila)
        columna = int(columna)
    except ValueError:
        return False
    if fila < 1 or fila > 10 or columna < 1 or columna > 4:
        return False
    return True

def menu():
    viaje = Viaje("Santiago", "Valparaíso")
    while True:
        print("1. Registrar un nuevo viaje")
        print("2. Mostrar asientos")
        print("3. Mostrar información de un viaje")
        print("4. Mostrar información de todos los viajes")
        print("5. Mostrar ganancias totales")
        print("6. Salir del sistema")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            fila = input("Ingrese la fila del asiento (1-10): ")
            columna = input("Ingrese la columna del asiento (1-4): ")
            if not validar_fila_columna(fila, columna):
                print("Fila o columna inválida")
                continue
            rut = input("Ingrese el RUT sin guion, puntos ni dígito verificador: ")
            if not validar_rut(rut):
                print("RUT inválido")
                continue
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            telefono = input("Ingrese el teléfono de emergencia: ")
            viaje.registrar_reserva(int(fila)-1, int(columna)-1, int(rut), nombre, apellido, telefono)
        elif opcion == "2":
            viaje.visualizar_asientos()
        elif opcion == "3":
            fila = input("Ingrese la fila del asiento (1-10): ")
            columna = input("Ingrese la columna del asiento (1-4): ")
            if not validar_fila_columna(fila, columna):
                print("Fila o columna inválida")
                continue
            viaje.mostrar_informacion_viaje(int(fila)-1, int(columna)-1)
        elif opcion == "4":
            viaje.mostrar_informacion_todos_los_viajes()
        elif opcion == "5":
            viaje.mostrar_ganancias_totales()
        elif opcion == "6":
            print(f"Gracias por utilizar el sistema. Fecha y hora de salida: {datetime.datetime.now()}")
            break
        else:
            print("Opción inválida")

