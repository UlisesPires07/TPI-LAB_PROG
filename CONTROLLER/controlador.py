from MODEL.cliente import Cliente
from MODEL.lugar import Lugar
from MODEL.servicio import Servicio
from VIEW.vista import Vista
from datetime import datetime, timedelta

class SistemaReservas:
    def __init__(self):
        self.vista = Vista()
        self.lugares = []
        self.servicios = []
        self.eventos = {}
    
    #CARGAR, MOSTRAR CALENDARIO, BUSCAR  Y VERIFICAR CALENDARIO
    def cargar_calendario(self):
        with open("calendario.txt") as file:
            next(file)  # Omitir la primera línea de encabezado
            for line in file:
                fecha, disponibilidad = line.strip().split("|")
                self.eventos[fecha] = disponibilidad
                
    def mostrar_fechas_disponibles(self):
        self.vista.mensaje_fecha1()
        for fecha, disponibilidad in self.eventos.items():
            if disponibilidad == "Disponible":
                print(fecha)
                
    def verificar_disponibilidad(self, fecha):
        return self.eventos.get(fecha, "Fecha no encontrada")

    def buscar_fecha_disponible(self, fecha):
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        while True:
            fecha_obj += timedelta(days=1)
            fecha_nueva = fecha_obj.strftime("%d/%m/%Y")
            if self.verificar_disponibilidad(fecha_nueva) == "Disponible":
                return fecha_nueva
    
    #CARGAR Y MOSTRAR LUGARES
    def cargar_lugares(self):
        with open("lugares.txt") as file:
            next(file)  # Omitir la primera línea de encabezado
            for line in file:
                num, nombre, costo, disponibilidad = line.strip().split("|")
                lugar = Lugar(int(num), nombre, float(costo), disponibilidad)
                self.lugares.append(lugar)
                
    def mostrar_lugares_disponibles(self):
        self.vista.mensaje_lugar1()
        for lugar in self.lugares:
            if lugar.disponibilidad == "Disponible":
                print(f"{lugar.num}. Salón: {lugar.nombre} ~~ Precio: ${lugar.costo}")
        
    def validar_lugar(self):
        for i in range(1, 5):
            while True:
                try:
                    opcion = self.vista.mostrar_mensaje3()
                    if opcion in range(1, 5):
                        return opcion
                    else:
                        self.vista.mostrar_mensaje3a()
                except ValueError:
                    self.vista.mostrar_mensaje3b()
    
    #CARGAR Y MOSTRAR SERVICIOS    
    def cargar_servicios(self):
        with open("servicios.txt") as file:
            next(file)  # Omitir la primera línea de encabezado
            for line in file:
                num, nombre, costo, disponibilidad = line.strip().split("|")
                servicio = Servicio(int(num), nombre, float(costo), disponibilidad)
                self.servicios.append(servicio)
                
    def mostrar_servicios_disponibles(self):
        self.vista.mensaje_servicio1()
        for servicio in self.servicios:
            if servicio.disponibilidad == "Disponible":
                print(f"{servicio.num}. Servicio: {servicio.nombre} ~~ Precio: ${servicio.costo}")
                
    def validar_servicio(self):
        for i in range(1, 24):
            while True:
                try:
                    opciones = self.vista.mostrar_mensaje4()
                    servicios_elegidos = [int(opcion) for opcion in opciones]
                    for opcion in servicios_elegidos:
                        if opcion not in range(1, 24):
                            self.vista.mostrar_mensaje4a()
                            break
                    else:
                        return servicios_elegidos
                except ValueError:
                    self.vista.mostrar_mensaje4b()
        
    #CLIENTE: INGRESAR DATOS
    def ingresar_datos(self): 
        self.cliente.nombre = self.vista.mensaje_cliente1()

        self.cliente.apellido = self.vista.mensaje_cliente2()

        self.cliente.dni = self.vista.mensaje_cliente3()
        while not self.cliente.dni.isdigit() or len(self.cliente.dni) != 8:
            self.vista.mensaje_cliente4()
            self.cliente.dni = self.vista.mensaje_cliente3()
            
        self.cliente.telefono = self.vista.mensaje_cliente5()
        while not self.cliente.telefono.isdigit() or len(self.cliente.telefono) != 10:
            self.vista.mensaje_cliente6()
            self.vista.mensaje_cliente5()
        
        self.cliente.correo = self.vista.mensaje_cliente7()

    #CLIENTE: GUARDAR DATOS
    def guardar_datos(self):
        with open("clientes.txt", "a") as file:
            file.write(f"{self.cliente.nombre}|{self.cliente.apellido}|{self.cliente.dni}|{self.cliente.telefono}|{self.cliente.correo}\n")

    
    #CLIENTE: GUARDAR RESERVA
    def guardar_reserva(self, fecha, lugar_num, servicios_elegidos):  
        import os

        ruta_archivo = ("reserva.txt")

        if not os.path.exists(ruta_archivo):
            with open(ruta_archivo, "w") as file:
                file.write("")  # Crea el archivo vacío si no existe
        
        if servicios_elegidos is None:
            servicios_elegidos = []  # Valor predeterminado, una lista vacía
        servicios_str = ','.join(map(str, servicios_elegidos))
       
        try:
            with open(ruta_archivo, "a") as file:
                file.write(f"Nombre|Apellido|Fecha|Lugar|Servicios\n")
                file.write(f"{self.cliente.nombre}|{self.cliente.apellido}|{fecha}|{lugar_num}|{servicios_str}\n")
        except IOError as e:
            self.vista.mensaje_cliente_guardar_reserva() + ("{e}")     
    
    
    #MÉTODOS CALCULAR COSTO TOTAL
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

    #CALCULAR MONTO SEÑA
    def calcular_monto_sena(self, costo_total):
        return costo_total * 0.3
    
    #REALIZAR RESERVA    
    def realizar_reserva(self, fecha, lugar_num, servicios_elegidos):
        self.cliente = Cliente()
        self.ingresar_datos()
        
        disponibilidad = self.verificar_disponibilidad(fecha)
        
        if disponibilidad == "Fecha no encontrada":
            return self.vista.mostrar_mensaje_reserva2()

        if disponibilidad == "No disponible":
            fecha_disponible = self.buscar_fecha_disponible(fecha)
            self.vista.mostrar_mensaje_reserva2()
            print(f"{fecha_disponible}.")
            return

        self.guardar_datos()
        self.guardar_reserva(fecha, lugar_num, servicios_elegidos) 
        costo_total = self.calcular_costo_total(lugar_num, servicios_elegidos)
        monto_sena = self.calcular_monto_sena(costo_total)

        self.vista.mostrar_mensaje_reserva3(), print(f"${costo_total:.2f}")
        self.vista.mostrar_mensaje_reserva4(), print(f"${monto_sena:.2f}")

        confirmacion = self.vista.mostrar_mensaje_reserva5()
        if confirmacion.lower() == "s":
            # Realizar la reserva
            self.vista.mostrar_mensaje_reserva6()
            # Actualizar la disponibilidad del lugar y servicios
            lugar = next((lugar for lugar in self.lugares if lugar.num == lugar_num), None)
            if lugar:
                lugar.disponibilidad = "No disponible"

            for servicio_num in servicios_elegidos:
                servicio = next((servicio for servicio in self.servicios if servicio.num == servicio_num), None)
                if servicio:
                    servicio.disponibilidad = "No disponible"

            # Actualizar la disponibilidad en el calendario
            self.eventos[fecha] = "No disponible"

        else:
            self.vista.mostrar_mensaje_reserva7()
            
    
    #CANCELAR RESERVA
    def cancelar_reserva(self, fecha):
        disponibilidad = self.verificar_disponibilidad(fecha)

        if disponibilidad == "Fecha no encontrada":
            self.vista.mostrar_mensaje_cancelar1()
            return

        if disponibilidad == "Disponible":
            self.vista.mostrar_mensaje_cancelar2()
            return

        confirmacion = self.vista.mostrar_mensaje_cancelar3()
        if confirmacion.lower() == "s":
            # Cancelar la reserva
            self.vista.mostrar_mensaje_cancelar4()
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
            self.eventos[fecha] = "Disponible"

            # Calcular y mostrar el reintegro (20% del valor de la seña)
            costo_total = self.calcular_costo_total(lugar_num, servicios_num)
            monto_sena = self.calcular_monto_sena(costo_total)

            # Verificar la fecha de cancelación
            fecha_actual = datetime.now().date()
            fecha_reserva = datetime.strptime(fecha, "%d/%m/%Y").date()
            fecha_limite = fecha_reserva - timedelta(days=15)

            if fecha_actual <= fecha_limite:
                reintegro = monto_sena * 0.2
                self.vista.mostrar_mensaje_cancelar5(), print(f"{reintegro:.2f}")
            else:
                self.vista.mostrar_mensaje_cancelar6()

        else:
            self.vista.mostrar_mensaje_cancelar7()
    
    #EJECUTAR MENÚ
    def ejecutar_sistema(self):
        self.vista.mostrar_menu()
            
        try:
            
            while True:
                opcion = self.vista.obtener_opcion()

                if opcion == "1":
                    self.cargar_calendario()
                    self.mostrar_fechas_disponibles()
                    self.vista.mensaje_vacio()
                    self.vista.mostrar_menu()

                elif opcion == "2":
                    self.cargar_lugares()
                    self.mostrar_lugares_disponibles()
                    self.vista.mensaje_vacio()
                    self.vista.mostrar_menu()

                elif opcion == "3":
                    self.cargar_servicios()
                    self.mostrar_servicios_disponibles()
                    self.vista.mensaje_vacio()
                    self.vista.mostrar_menu()

                elif opcion == "4":
                    self.vista.mostrar_mensaje1()
                    fecha = self.vista.mostrar_mensaje2()
                    lugar_num = self.validar_lugar()
                    servicios_elegidos = self.validar_servicio()
                    if servicios_elegidos is not None:
                        servicios_elegidos = [int(servicio_num) for servicio_num in servicios_elegidos]

                    self.realizar_reserva(fecha, lugar_num, servicios_elegidos)
                    
                    self.vista.mensaje_vacio()
                    self.vista.mostrar_menu()

                elif opcion == "5":
                    self.vista.mostrar_mensaje5()
                    fecha = self.vista.mostrar_mensaje6()
                    self.cancelar_reserva(fecha)
                    
                    self.vista.mensaje_vacio()
                    self.vista.mostrar_menu()

                elif opcion == "6":
                    self.vista.mostrar_mensaje7()
                    break

                else:
                    self.vista.mostrar_mensaje8()

        except Exception as e:
            self.vista.mostrar_mensaje9() and str("{e}")