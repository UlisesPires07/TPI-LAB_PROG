from datetime import datetime, timedelta

class Calendario:
    def __init__(self):
        self.eventos = {}

    def verificar_disponibilidad(self, fecha):
        if fecha in self.eventos:
            return self.eventos[fecha]  # Devolver la disponibilidad del evento en la fecha especificada


    def buscar_fecha_disponible(self, fecha):
            fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
            while True:
                fecha_obj += timedelta(days=1)
                fecha_nueva = fecha_obj.strftime("%d/%m/%Y")
                if self.verificar_disponibilidad(fecha_nueva) == "Disponible":
                    return fecha_nueva