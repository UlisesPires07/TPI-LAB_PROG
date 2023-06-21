from datetime import datetime, timedelta

import os

ruta_archivo = "reserva.txt"

if not os.path.exists(ruta_archivo):
    with open(ruta_archivo, "w") as file:
        file.write("")  # Crea el archivo vacío si no existe

class Calendario:
    def __init__(self):
        self.eventos = {}

    def cargar_calendario(self):
        with open("calendario.txt") as file:
            next(file)  # Omitir la primera línea de encabezado
            for line in file:
                fecha, disponibilidad = line.strip().split("|")
                self.eventos[fecha] = disponibilidad

    def verificar_disponibilidad(self, fecha):
        return self.eventos.get(fecha, "Fecha no encontrada")

    def buscar_fecha_disponible(self, fecha):
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        while True:
            fecha_obj += timedelta(days=1)
            fecha_nueva = fecha_obj.strftime("%d/%m/%Y")
            if self.verificar_disponibilidad(fecha_nueva) == "Disponible":
                return fecha_nueva
            
    def mostrar_fechas_disponibles(self):
        print("\nFECHAS DISPONIBLES:")
        for fecha, disponibilidad in self.eventos.items():
            if disponibilidad == "Disponible":
                print(fecha)

class Lugar:
    def __init__(self, num, nombre, costo, disponibilidad):
        self.num = num
        self.nombre = nombre
        self.costo = costo
        self.disponibilidad = disponibilidad

class Servicio:
    def __init__(self, num, nombre, costo, disponibilidad):
        self.num = int(num)
        self.nombre = nombre
        self.costo = costo
        self.disponibilidad = disponibilidad
        
class Cliente:
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.dni = ""
        self.telefono = ""
        self.correo = ""

    def ingresar_datos(self):
        self.nombre = input("Ingrese el nombre del cliente: ")
        while not self.nombre.isalpha():
            print("El nombre solo puede contener letras. Inténtelo nuevamente.")
            self.nombre = input("Ingrese el nombre del cliente: ")

        self.apellido = input("Ingrese el apellido del cliente: ")
        while not self.apellido.isalpha():
            print("El apellido solo puede contener letras. Inténtelo nuevamente.")
            self.apellido = input("Ingrese el apellido del cliente: ")

        self.dni = input("Ingrese el DNI del cliente: ")
        while not self.dni.isdigit() or len(self.dni) != 8:
            print("El DNI debe ser un número de 8 dígitos. Inténtelo nuevamente.")
            self.dni = input("Ingrese el DNI del cliente: ")
            
        self.telefono = input("Ingrese el número de teléfono del cliente: ")
        self.correo = input("Ingrese el correo electrónico del cliente: ")

    def guardar_datos(self):
        with open("clientes.txt", "a") as file:
            file.write(f"{self.nombre}|{self.apellido}|{self.dni}|{self.telefono}|{self.correo}\n")

                
    def guardar_reserva(self, fecha, lugar_num, servicios_elegidos):
        servicios_str = ','.join(map(str, servicios_elegidos))
        try:
            with open(ruta_archivo, "a") as file:
                file.write(f"Nombre|Apellido|Fecha|Lugar|Servicios\n")
                file.write(f"{self.nombre}|{self.apellido}|{fecha}|{lugar_num}|{servicios_str}\n")
        except IOError as e:
            print(f"Error al guardar la reserva: {e}")        

class SistemaReservas:
    def __init__(self):
        self.calendario = Calendario()
        self.lugares = []
        self.servicios = []

    def cargar_lugares(self):
        with open("lugares.txt") as file:
            next(file)  # Omitir la primera línea de encabezado
            for line in file:
                num, nombre, costo, disponibilidad = line.strip().split("|")
                lugar = Lugar(int(num), nombre, float(costo), disponibilidad)
                self.lugares.append(lugar)

    def mostrar_lugares_disponibles(self):
        print("\nLUGARES DISPONIBLES:")
        for lugar in self.lugares:
            if lugar.disponibilidad == "Disponible":
                print(f"{lugar.num}. Salon: {lugar.nombre} ~~ Precio: ${lugar.costo}")

    def cargar_servicios(self):
        with open("servicios.txt") as file:
            next(file)  # Omitir la primera línea de encabezado
            for line in file:
                num, nombre, costo, disponibilidad = line.strip().split("|")
                servicio = Servicio(int(num), nombre, float(costo), disponibilidad)
                self.servicios.append(servicio)

    def mostrar_servicios_disponibles(self):
        print("\nSERVICIOS DISPONIBLES:")
        for servicio in self.servicios:
            if servicio.disponibilidad == "Disponible":
                print(f"{servicio.num}. Servicio: {servicio.nombre} ~~ Precio: ${servicio.costo}")

    def calcular_costo_total(self, lugar_num, servicios_elegidos):
        costo_total = 0

        lugar_disponible = next((lugar for lugar in self.lugares if lugar.num == lugar_num and lugar.disponibilidad == "Disponible"), None)
        if lugar_disponible:
            costo_total += lugar_disponible.costo

        for servicio_num in servicios_elegidos:
            servicio = next((servicio for servicio in self.servicios if servicio.num == servicio_num and servicio.disponibilidad == "Disponible"), None)
            if servicio:
                costo_total += servicio.costo

        costo_total += 6000  # Agregar gastos administrativos
        costo_total *= 1.21  # Agregar IVA.
        return costo_total

    def calcular_monto_sena(self, costo_total):
        return costo_total * 0.3

    def realizar_reserva(self, fecha, lugar_num, servicios_elegidos):
        cliente = Cliente()
        cliente.ingresar_datos()
        cliente.guardar_datos()
        cliente.guardar_reserva(fecha, lugar_num, servicios_elegidos)
        disponibilidad_fecha = self.calendario.verificar_disponibilidad(fecha)
        disponibilidad_fecha = self.calendario.verificar_disponibilidad(fecha)

        if disponibilidad_fecha == "Fecha no encontrada":
            print("La fecha ingresada no es válida.")
            return

        if disponibilidad_fecha == "No disponible":
            fecha_disponible = self.calendario.buscar_fecha_disponible(fecha)
            print(f"La fecha ingresada no está disponible. La próxima fecha disponible es {fecha_disponible}.")
            return

        costo_total = self.calcular_costo_total(lugar_num, servicios_elegidos)
        monto_sena = self.calcular_monto_sena(costo_total)

        print(f"\nEl costo total de la reserva es: ${costo_total:.2f}")
        print(f"\nEl monto de la seña es de: ${monto_sena:.2f}")

        confirmacion = input("\n¿Desea confirmar la reserva? (S/N): ")
        if confirmacion.lower() == "s":
            # Realizar la reserva
            print("\nRESERVA REALIZADA CON EXITO.")
            # Actualizar la disponibilidad del lugar y servicios
            lugar = next((lugar for lugar in self.lugares if lugar.num == lugar_num), None)
            if lugar:
                lugar.disponibilidad = "No disponible"

            for servicio_num in servicios_elegidos:
                servicio = next((servicio for servicio in self.servicios if servicio.num == servicio_num), None)
                if servicio:
                    servicio.disponibilidad = "No disponible"

            # Actualizar la disponibilidad en el calendario
            self.calendario.eventos[fecha] = "No disponible"

        else:
            print("\nRESERVA CANCELADA.")

    def cancelar_reserva(self, fecha):
        disponibilidad_fecha = self.calendario.verificar_disponibilidad(fecha)

        if disponibilidad_fecha == "Fecha no encontrada":
            print("La fecha ingresada no es válida.")
            return

        if disponibilidad_fecha == "Disponible":
            print("No hay ninguna reserva para la fecha ingresada.")
            return

        confirmacion = input("\n¿Está seguro de cancelar la reserva? (S/N): ")
        if confirmacion.lower() == "s":
            # Cancelar la reserva
            print("\nRESERVA CANCELADA CON EXITO.")
            # Actualizar la disponibilidad del lugar y servicios
            lugar_num = next((lugar.num for lugar in self.lugares if lugar.disponibilidad == "No disponible"), None)
            if lugar_num:
                lugar = next((lugar for lugar in self.lugares if lugar.num == lugar_num), None)
                if lugar:
                    lugar.disponibilidad = "Disponible"

            servicios_num = [servicio.num for servicio in self.servicios if servicio.disponibilidad == "No disponible"]
            if servicios_num:
                for servicio_num in servicios_num:
                    servicio = next((servicio for servicio in self.servicios if servicio.num == servicio_num), None)
                    if servicio:
                        servicio.disponibilidad = "Disponible"

            # Actualizar la disponibilidad en el calendario
            self.calendario.eventos[fecha] = "Disponible"

            # Calcular y mostrar el reintegro (20% del valor de la seña)
            costo_total = self.calcular_costo_total(lugar_num, servicios_num)
            monto_sena = self.calcular_monto_sena(costo_total)

            # Verificar la fecha de cancelación
            fecha_actual = datetime.now().date()
            fecha_reserva = datetime.strptime(fecha, "%d/%m/%Y").date()
            fecha_limite = fecha_reserva - timedelta(days=15)

            if fecha_actual <= fecha_limite:
                reintegro = monto_sena * 0.2
                print(f"\nEl reintegro correspondiente al 20% del valor de la seña es de: ${reintegro:.2f}")
            else:
                print("\nNo se realizará ningún reintegro, ya que la fecha de cancelación está dentro de los 15 días previos al evento.")

        else:
            print("Operación cancelada.")

    def ejecutar_sistema(self):
        try:
            self.calendario.cargar_calendario()
            self.cargar_lugares()
            self.cargar_servicios()

            while True:
                print("\nSOCIALEVENT S.A. - ORGANIZACION DE EVENTOS")
                print("\nSISTEMA DE RESERVAS")
                print("1. Fechas disponibles")
                print("2. Lugares disponibles")
                print("3. Servicios disponibles")
                print("4. Realizar una reserva")
                print("5. Cancelar una reserva")
                print("6. Salir")

                opcion = input("\nIngrese el número de la opción deseada: ")

                if opcion == "1":
                    self.calendario.mostrar_fechas_disponibles()

                elif opcion == "2":
                    self.mostrar_lugares_disponibles()

                elif opcion == "3":
                    self.mostrar_servicios_disponibles()

                elif opcion == "4":
                    print("\n¡Hagamos tu reserva!")
                    fecha = input("\nIngrese la fecha de la reserva (DD/MM/AAAA): ")
                    lugar_num = int(input("Ingrese el número del lugar deseado: "))
                    servicios_elegidos = input("Ingrese los números de los servicios deseados (separados por comas): ").split(",")
                    servicios_elegidos = [int(servicio_num) for servicio_num in servicios_elegidos]

                    self.realizar_reserva(fecha, lugar_num, servicios_elegidos)

                elif opcion == "5":
                    print("\n¡Cancelemos tu reserva!")
                    fecha = input("\nIngrese la fecha de la reserva a cancelar (DD/MM/AAAA): ")
                    self.cancelar_reserva(fecha)

                elif opcion == "6":
                    print("\nGracias por utilizar el sistema de reservas. ¡Hasta luego!")
                    break

                else:
                    print("Opción inválida. Por favor, ingrese una opción válida.")

        except Exception as e:
            print("Se produjo una excepción:", str(e))

sistema_reservas = SistemaReservas()
sistema_reservas.ejecutar_sistema()