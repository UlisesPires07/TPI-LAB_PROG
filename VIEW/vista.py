class Vista:
    def __init__(self):
        self.eventos = {}   
    
    def mostrar_menu(self):
        print("")
        print("\nSOCIALEVENT S.A. - ORGANIZACION DE EVENTOS")
        print("\nSISTEMA DE RESERVAS")
        print("1. Fechas disponibles")
        print("2. Lugares disponibles")
        print("3. Servicios disponibles")
        print("4. Realizar una reserva")
        print("5. Cancelar una reserva")
        print("6. Salir")
        print("")
        
    def obtener_opcion(self):
        return input("Ingrese una opción para continuar: ")
    
    #FECHAS DISPONIBLES
    def mensaje_fecha1(self):
        print("\nFECHAS DISPONIBLES:")
        
    #LUGARES DISPONIBLES
    def mensaje_lugar1(self):
        print("\nLUGARES DISPONIBLES:")
    
    #SERVICIOS DISPONIBLES
    def mensaje_servicio1(self):
        print("\nSERVICIOS DISPONIBLES:")
    
    #MENSAJES CLIENTE
    def mensaje_cliente1(self):
        return input("Ingrese el nombre del cliente: ")
        
    def mensaje_cliente2(self):
        return input("Ingrese el apellido del cliente: ")
        
    def mensaje_cliente3(self):
        return input("Ingrese el DNI del cliente: ")
        
    def mensaje_cliente4(self):
        return print("El DNI debe ser un número de 8 dígitos. Inténtelo nuevamente.")
        
    def mensaje_cliente5(self):
        return input("Ingrese el número de teléfono del cliente: ")
    
    def mensaje_cliente6(self):
        return print("El teléfono debe ser un número de 10 dígitos. Inténtelo nuevamente.")
        
    def mensaje_cliente7(self):
        return input("Ingrese el correo electrónico del cliente: ")
        
    def mensaje_cliente_guardar_reserva(self):
        print(f"Error al guardar la reserva: ")  
    
    #MOSTRAR MENSAJES REALIZAR RESERVA
    def mostrar_mensaje_reserva1(self):
        return print("La fecha ingresada no es válida.")
        
    def mostrar_mensaje_reserva2(self):
        return print(f"La fecha ingresada no está disponible. La próxima fecha disponible es ")
        
    def mostrar_mensaje_reserva3(self):
        return print(f"\nEl costo total de la reserva es: $ ")
    
    def mostrar_mensaje_reserva4(self):
        return print(f"\nEl monto de la seña es de: $ ")
         
    def mostrar_mensaje_reserva5(self):
        return input("\n¿Desea confirmar la reserva? (S/N): ")
    
    def mostrar_mensaje_reserva6(self):
        return print("\nRESERVA REALIZADA CON EXITO.")
        
    def mostrar_mensaje_reserva7(self):
        return print("\nRESERVA CANCELADA.")
        
        
    #MOSTRAR MENSAJES CANCELAR RESERVA
    def mostrar_mensaje_cancelar1(self):
        return print("La fecha ingresada no es válida.")
        
    def mostrar_mensaje_cancelar2(self):
        return print("No hay ninguna reserva para la fecha ingresada.")
    
    def mostrar_mensaje_cancelar3(self):
        return input("\n¿Está seguro de cancelar la reserva? (S/N): ")
    
    def mostrar_mensaje_cancelar4(self):
        return print("\nRESERVA CANCELADA CON EXITO.")
    
    def mostrar_mensaje_cancelar5(self):
        return print(f"\nEl reintegro correspondiente al 20% del valor de la seña es de: $")
    
    def mostrar_mensaje_cancelar6(self):
        return print("\nNo se realizará ningún reintegro, ya que la fecha de cancelación está dentro de los 15 días previos al evento.")
        
    def mostrar_mensaje_cancelar7(self):
        return print("Operación cancelada.")
        
    def mensaje_vacio(self):
        print("")
        
    
    #MENSAJES VALIDACIONES
    def mensaje_validacion(self):
        print("La opción escogida es inválida. Introduce un número válido entre ")
    
    # MOSTRAR MENSAJES MENÚ
    def mostrar_mensaje1(self):
        return print("\n¡Hagamos tu reserva!")
        
    def mostrar_mensaje2(self):
        return input("\nIngrese la fecha de la reserva (DD/MM/AAAA): ")
        
    def mostrar_mensaje3(self):
        return int(input("Ingrese el número del lugar deseado: "))

    def mostrar_mensaje3a(self):
        return print("Opción inválida. Por favor, ingrese un número del 1 al 4.")
    
    def mostrar_mensaje3b(self):
        return print("Entrada inválida. Por favor, ingrese un número del 1 al 4.")
    
    def mostrar_mensaje4(self):
        return input("Ingrese los números de los servicios deseados (separados por comas): ").split(",")
    
    def mostrar_mensaje4a(self):
        return print("Opción inválida. Por favor, ingrese números del 1 al 23 separados por comas.")
    
    def mostrar_mensaje4b(self):
        return print("Entrada inválida. Por favor, ingrese números del 1 al 23 separados por comas.")

    def mostrar_mensaje5(self):
        return print("\n¡Cancelemos tu reserva!")
        
    def mostrar_mensaje6(self):
        return input("\nIngrese la fecha de la reserva a cancelar (DD/MM/AAAA): ")
        
    def mostrar_mensaje7(self):
        return print("\nGracias por utilizar el sistema de reservas. ¡Hasta luego!")
        
    def mostrar_mensaje8(self):
        return print("Opción inválida. Por favor, ingrese una opción válida.")
        
    def mostrar_mensaje9(self):
        return print("Se produjo una excepción:")