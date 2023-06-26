Universidad Tecnológica Nacional
Facultad Regional Villa María


Tecnicatura Universitaria en Programación


Laboratorio de Computación II | Programación II


Franco García, Ulises Jesse, Mateo Formoso, Ana Lucía Sola


21 de junio del 2023 


Enunciado del trabajo práctico integrador en conjunto

SocialEvent S.A. es una empresa que tiene como objetivo fundamental la organización de Congresos y Eventos, creando proyectos únicos y personales, asesorando al interesado, y teniendo en cuenta el cuidado de los detalles, adaptándose a un mundo en constante cambio. Cuando un cliente solicita el servicio de la empresa, los encargados de la organización verifican si el día no se encuentra reservado para otro evento. En caso de estar ocupado, se le propone la fecha libre más cercana. Al confirmar que la fecha de realización cuenta con disponibilidad, la empresa le ofrece al cliente sus diferentes servicios a contratar indicando el costo de cada uno. Por ejemplo: dj, decoración, cotillón, máquina de humo, maquillaje, música en vivo, etc. Luego de que el cliente seleccione los servicios deseados se calcula el importe total de la fiesta y se le suman los gastos administrativos, junto con el IVA. Para realizar la reserva del servicio el mismo debe señarse con un mínimo del 30% del total calculado. En caso de que el cliente desee cancelar su reserva solamente se le devolverá un 20% de lo señado, siempre y cuando la fecha de cancelación sea 15 días antes del evento, caso contrario no se le reintegrará el dinero. En los últimos años SocialEvent ha incrementado su cartera de clientes y se encontró con la problemática de que la demanda a sus eventos era demasiada.
Para poder tener una mejor organización, contrataron a un grupo de desarrolladores para la creación de su propio sistema de información, que les permita saber:
Si la fecha solicitada se encuentra disponible (en caso de estar ocupada, proponer la fecha más próxima libre) 
Cuál es el costo total del evento, detallando los servicios elegidos 
Cuanto es el monto de la seña 
Cancelar el evento, en ese caso informar el importe a devolver

Repositorio git-hub
https://github.com/UlisesPires07/TPI-LAB_PROG

Meistertask - Gestión de tareas:
https://www.meistertask.com/app/project/5aQcJmlS/lab-ii-prog-ii



DOCUMENTACIÓN:

Archivo main.py
Este archivo contiene el código principal que inicia el sistema de reservas.

1.Importar el módulo SistemaReservas del paquete CONTROLLER.controlador:


from CONTROLLER.controlador import SistemaReservas

Este paso permite utilizar la clase SistemaReservas definida en el archivo controlador.py dentro del paquete CONTROLLER.

2.Crear una instancia del objeto SistemaReservas:
controlador = SistemaReservas()

Aquí se crea un nuevo objeto controlador utilizando la clase SistemaReservas. Esto permitirá interactuar con el sistema de reservas y realizar diferentes acciones.
Ejecutar el sistema de reservas:
controlador.ejecutar_sistema()


En este paso se llama al método ejecutar_sistema() del objeto controlador. Este método se encarga de iniciar el sistema de reservas y permite al usuario interactuar con él.


Con estos pasos, se importa el módulo SistemaReservas, se crea una instancia del objeto controlador y se ejecuta el sistema de reservas.

Archivo vista.py

Esta clase representa la interfaz de usuario del sistema de reservas.
__init__(self): Constructor de la clase Vista que inicializa el atributo eventos como un diccionario vacío.
def __init__(self):
    self.eventos = {}
Este método se ejecuta al crear una instancia de la clase Vista.
mostrar_menu(self): Muestra el menú principal del sistema de reservas en la consola.
def mostrar_menu(self):
    # Imprime el encabezado del menú
    print("\nSOCIALEVENT S.A. - ORGANIZACION DE EVENTOS")
    print("\nSISTEMA DE RESERVAS")
    # Muestra las opciones disponibles
    print("1. Fechas disponibles")
    print("2. Lugares disponibles")
    print("3. Servicios disponibles")
    print("4. Realizar una reserva")
    print("5. Cancelar una reserva")
    print("6. Salir")
Luego se proporcionarán los métodos para imprimir los mensajes que indican: fechas disponibles, lugares disponibles, servicios disponibles, interacciones con el cliente, entre otros.

CLASES

cliente.py


Esta clase representa a un cliente del sistema de reservas.
__init__(self): Constructor de la clase Cliente que inicializa los atributos nombre, apellido, dni, telefono y correo como cadenas vacías.
def __init__(self):
    self.nombre = ""
    self.apellido = ""
    self.dni = ""
    self.telefono = ""
    self.correo = ""


Este método se ejecuta al crear una instancia de la clase Cliente.

Los atributos nombre, apellido, dni, telefono y correo representan los datos del cliente y se inicializan como cadenas vacías.

Con esta clase, puedes crear objetos Cliente que almacenarán los datos de un cliente específico del sistema de reservas.

lugar.py


Esta clase representa un lugar disponible para reservar en el sistema.
__init__(self, num, nombre, costo, disponibilidad): Constructor de la clase Lugar que recibe los parámetros num, nombre, costo y disponibilidad para inicializar los atributos correspondientes.
def __init__(self, num, nombre, costo, disponibilidad):
    self.num = num
    self.nombre = nombre
    self.costo = costo
    self.disponibilidad = disponibilidad

Este método se ejecuta al crear una instancia de la clase Lugar.

Los atributos num, nombre, costo y disponibilidad representan respectivamente el número del lugar, el nombre del lugar, el costo de reserva y la disponibilidad del lugar.
num: Número del lugar.
nombre: Nombre del lugar.
costo: Costo de reserva del lugar.
disponibilidad: Disponibilidad del lugar.
Con esta clase, puedes crear objetos Lugar que representan lugares disponibles para reservar en el sistema y que contienen información como el número, nombre, costo y disponibilidad del lugar.
servicio.py


Esta clase representa un servicio disponible para reservar en el sistema.

1. __init__(self, num, nombre, costo, disponibilidad): Constructor de la clase Servicio que recibe los parámetros num, nombre, costo y disponibilidad para inicializar los atributos correspondientes.
def __init__(self, num, nombre, costo, disponibilidad):
    self.num = int(num)
    self.nombre = nombre
    self.costo = costo
    self.disponibilidad = disponibilidad

Este método se ejecuta al crear una instancia de la clase Servicio.
Los atributos num, nombre, costo y disponibilidad representan respectivamente el número del servicio, el nombre del servicio, el costo del servicio y la disponibilidad del servicio.
num: Número del servicio.
nombre: Nombre del servicio.
costo: Costo del servicio.
disponibilidad: Disponibilidad del servicio.
El número del servicio se convierte en entero utilizando la función int() para asegurar que sea un valor numérico.

Con esta clase, puedes crear objetos Servicio que representan servicios disponibles para reservar en el sistema y que contienen información como el número, nombre, costo y disponibilidad del servicio.

Archivo controlador.py

El código importa las clases Calendario, Cliente, Lugar, Servicio y Vista desde los respectivos módulos en el paquete MODEL. También importa datetime y timedelta del módulo datetime.


La clase SistemaReservas es la clase principal que coordina todas las operaciones del sistema de reservas. Contiene métodos para cargar y mostrar el calendario, lugares y servicios disponibles, ingresar y guardar datos del cliente, realizar una reserva, cancelar una reserva y ejecutar el menú del sistema.
Además, la clase SistemaReservas representa el sistema de reservas y tiene un constructor __init__ que inicializa los atributos vista, lugares, servicios, calendario y eventos.


Se utilizan otras clases y módulos:
Calendario: Una clase que gestiona el calendario y la disponibilidad de eventos.
Cliente: Una clase que representa los datos de un cliente.
Lugar: Una clase que representa un lugar disponible para reservar.
Servicio: Una clase que representa un servicio disponible para reservar.
Vista: Un módulo que contiene métodos para mostrar mensajes y obtener la entrada del usuario.
El programa utiliza archivos de texto para almacenar y cargar datos como el calendario, los lugares y los servicios disponibles, así como las reservas realizadas por los clientes.


El programa ofrece opciones para cargar y mostrar el calendario, lugares y servicios disponibles, ingresar datos del cliente, realizar una reserva y cancelar una reserva. También se ejecuta un menú que permite al usuario interactuar con el sistema y seleccionar las diferentes opciones.

En el caso del calendario, las primeras acciones que se desarrollan son:

verificar_disponibilidad(self, fecha): Verifica la disponibilidad de un evento en la fecha especificada.
def verificar_disponibilidad(self, fecha):
    if fecha in self.eventos:
        return self.eventos[fecha]
Este método verifica si la fecha especificada se encuentra en el diccionario eventos y devuelve su estado de disponibilidad.


2. buscar_fecha_disponible(self, fecha): Busca la próxima fecha disponible a partir de la fecha especificada.
def buscar_fecha_disponible (self, fecha):
    fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
    while True:
        fecha_obj += timedelta(days=1)
        fecha_nueva = fecha_obj.strftime("%d/%m/%Y")
        if self.verificar_disponibilidad(fecha_nueva) == "Disponible":
            return fecha_nueva
Este método se utiliza para buscar la siguiente fecha disponible a partir de una fecha dada. Toma un parámetro fecha y lo convierte en un objeto datetime utilizando el método strptime(). Luego, en un bucle infinito, incrementa la fecha en un día utilizando el objeto timedelta y lo formatea nuevamente como una cadena en el formato "%d/%m/%Y" utilizando el método strftime(). En cada iteración, se verifica la disponibilidad de la nueva fecha utilizando el método verificar_disponibilidad(). Si la disponibilidad es "Disponible", se devuelve la nueva fecha.


Además, este método toma una fecha en formato de cadena, la convierte en un objeto datetime y luego busca la próxima fecha disponible incrementando un día en cada iteración. Si encuentra una fecha disponible, la devuelve como una cadena en formato:
"DD/MM/AAAA"


Los próximos métodos componen el sistema de reservas:
1. `__init__(self)`: Constructor de la clase `SistemaReservas` que inicializa los atributos `vista`, `lugares`, `servicios`, `calendario` y `eventos`.


2. `cargar_calendario(self)`: Lee el archivo "calendario.txt" y carga los eventos en el diccionario `eventos` del calendario.


Este método de la clase Calendario se utiliza para cargar eventos y su disponibilidad desde un archivo llamado "calendario.txt". El método abre el archivo utilizando el comando open() en modo de lectura. Luego, itera sobre las líneas del archivo, omitiendo la primera línea de encabezado utilizando la función next (). Cada línea se divide en dos partes: fecha y disponibilidad, separadas por el carácter "|". Estos valores se almacenan en el diccionario eventos de la clase Calendario, utilizando fecha como clave y disponibilidad como valor.


3. `mostrar_fechas_disponibles(self)`: Muestra las fechas disponibles en el calendario.

Este método de la clase Calendario se utiliza para mostrar las fechas disponibles en el calendario. Imprime el encabezado "FECHAS DISPONIBLES:" y luego itera sobre los elementos del diccionario eventos. Si la disponibilidad es "Disponible", imprime la fecha.

4. `cargar_lugares(self)`: Lee el archivo "lugares.txt" y carga la información de los lugares en la lista `lugares`.

Esta sección define una clase llamada SistemaReservas. La clase tiene un método especial llamado __init__() que se utiliza para inicializar objetos de la clase. Los objetos de esta clase tienen tres atributos: calendario, lugares y servicios. calendario es una instancia de la clase Calendario y lugares y servicios son listas vacías.

5. `mostrar_lugares_disponibles(self)`: Muestra los lugares disponibles.

Este método de la clase SistemaReservas se utiliza para mostrar los lugares disponibles. Itera sobre la lista lugares y verifica la disponibilidad de cada lugar. Si el lugar está disponible, se imprime su número, nombre y costo.

6. `cargar_servicios(self)`: Lee el archivo "servicios.txt" y carga la información de los servicios en la lista `servicios`.

Este método de la clase SistemaReservas se utiliza para cargar los servicios disponibles desde un archivo llamado "servicios.txt". Utiliza el comando open() para abrir el archivo en modo de lectura ("r"). Luego, itera sobre cada línea del archivo, omite la primera línea de encabezado usando next(file), divide la línea en partes utilizando el carácter "|" como separador y crea objetos de la clase Servicio con los valores correspondientes. Estos objetos se agregan a la lista servicios del objeto SistemaReservas.

7. `mostrar_servicios_disponibles(self)`: Muestra los servicios disponibles.

Este método de la clase SistemaReservas se utiliza para mostrar los servicios disponibles. Itera sobre la lista servicios y verifica la disponibilidad de cada servicio. Si el servicio está disponible, se imprime su número, nombre y costo.

8. `ingresar_datos(self)`: Solicita al usuario que ingrese los datos del cliente y los guarda en el objeto `cliente`.

Este método de la clase Cliente se utiliza para ingresar los datos del cliente. Utiliza la función input() para solicitar al usuario que ingrese el nombre, apellido, DNI, número de teléfono y correo electrónico del cliente. Luego, realiza validaciones en bucles while para asegurarse de que los datos ingresados sean válidos. Por ejemplo, se verifica que el nombre y el apellido solo contengan letras, que el DNI sea un número de 8 dígitos y que los demás datos se ingresen sin restricciones adicionales.

9. `guardar_datos(self)`: Guarda los datos del cliente en el archivo "clientes.txt".
Este método estático de la clase Cliente se utiliza para mostrar los datos de todos los clientes almacenados en el archivo "clientes.txt". Utiliza el comando open() en modo de lectura ("r") para abrir el archivo. Luego, itera sobre cada línea del archivo y divide la línea en partes utilizando el carácter "|" como separador. Estas partes corresponden a los campos nombre, apellido, dni, teléfono y correo. Luego, imprime los datos formateados en el formato "Nombre: valor", "Apellido: valor", etc., para cada cliente.

10. `guardar_reserva (self, fecha, lugar_num, servicios_elegidos)`: Guarda los detalles de la reserva en el archivo "reserva.txt".

Este método de la clase Cliente se utiliza para guardar una reserva realizada por el cliente en un archivo. Toma los parámetros fecha (fecha de la reserva), lugar_num (número del lugar reservado) y servicios_elegidos (una lista de servicios elegidos para la reserva). Convierte la lista servicios_elegidos en una cadena separada por comas utilizando ',’. join (map(str, servicios_elegidos)). Luego, utiliza el comando open () en modo de adjuntar ("a") para abrir el archivo especificado por ruta_archivo (que debe estar definido en otro lugar del código) y escribe una línea de encabezado seguida de una línea de datos de reserva que contiene el nombre del cliente, apellido, fecha, lugar y servicios elegidos. Si se produce un error de E/S, se captura la excepción IOError y se imprime un mensaje de error.

11. `calcular_costo_total (self, lugar_num, servicios_elegidos) `: Calcula el costo total de la reserva, considerando el lugar y los servicios elegidos.

Este método de la clase SistemaReservas se utiliza para calcular el costo total de una reserva. Toma dos parámetros: lugar_num (el número del lugar reservado) y servicios_elegidos (una lista de números de servicios elegidos para la reserva). Primero, inicializa costo_total en 0. Luego, busca el lugar con el número especificado en la lista lugares y verifica su disponibilidad. Si el lugar está disponible, se agrega su costo al costo_total. A continuación, itera sobre los números de servicios elegidos y busca cada servicio en la lista servicios, verificando su disponibilidad. Si un servicio está disponible, se agrega su costo al costo_total. Luego, se agrega un monto fijo de 6000 por gastos administrativos y se multiplica el costo_total por 1.21 para agregar el impuesto al valor agregado (IVA). Finalmente, se devuelve el costo_total.

12. `calcular_monto_sena (self, costo_total)`: Calcula el monto de la seña, que es el 30% del costo total.

Este método de la clase SistemaReservas se utiliza para calcular el monto de la seña (el adelanto) para una reserva. Toma el parámetro costo_total, que es el costo total de la reserva. Multiplica el costo_total por 0.3 (30%) y devuelve el resultado.

13. `realizar_reserva (self, fecha, lugar_num, servicios_elegidos) `: Realiza el proceso de reserva, solicitando datos al cliente, calculando el costo total y la seña, y guardando la reserva si el cliente confirma.

Este método de la clase SistemaReservas se utiliza para realizar una reserva. Toma tres parámetros: fecha (la fecha de la reserva), lugar_num (el número del lugar reservado) y servicios_elegidos (una lista de números de servicios elegidos para la reserva).

Primero, se crea una instancia de la clase Cliente y se llaman a los métodos ingresar_datos (), guardar_datos() y guardar_reserva() en ese objeto cliente.

Luego, se verifica la disponibilidad de la fecha utilizando el método verificar_disponibilidad () de la instancia de Calendario. Si la fecha no se encuentra en el calendario, se imprime un mensaje de error y se retorna. Si la fecha no está disponible, se busca la próxima fecha disponible utilizando el método buscar_fecha_disponible () de la instancia de Calendario. Se imprime un mensaje indicando la próxima fecha disponible y se retorna.

A continuación, se calcula el costo total de la reserva llamando al método calcular_costo_total () y se calcula el monto de la seña llamando al método calcular_monto_sena (), utilizando el lugar_num y servicios_elegidos como parámetros.

Se imprime el costo total de la reserva y el monto de la seña.

Luego, se solicita al usuario que confirme la reserva. Si la confirmación es "s" (Sí), se realiza la reserva:
Se imprime un mensaje indicando que la reserva se realizó con éxito.
Se busca el lugar correspondiente al lugar_num en la lista lugares y se actualiza su disponibilidad a "No disponible".
Se busca cada servicio correspondiente a los servicios_elegidos en la lista servicios y se actualiza su disponibilidad a "No disponible".
Se actualiza la disponibilidad de la fecha en el calendario estableciendo el valor correspondiente en el diccionario eventos.
Si la confirmación es "n" (No), se imprime un mensaje indicando que la reserva se canceló.

14. `cancelar_reserva (self, fecha) `: Cancela una reserva existente, actualizando la disponibilidad del lugar y servicios, y mostrando el reintegro en caso de cancelación dentro del plazo.

Este método de la clase SistemaReservas se utiliza para cancelar una reserva. Toma el parámetro fecha (la fecha de la reserva a cancelar).

Se verifica la disponibilidad de la fecha utilizando el método verificar_disponibilidad () de la instancia de Calendario. Si la fecha no se encuentra en el calendario, se imprime un mensaje de error y se retorna. Si la fecha está disponible, se imprime un mensaje indicando que no hay ninguna reserva para la fecha ingresada y se retorna.

Luego, se solicita al usuario que confirme la cancelación de la reserva. Si la confirmación es "s" (Sí), se cancela la reserva:
Se imprime un mensaje indicando que la reserva se canceló con éxito.
Se busca el número del lugar reservado (lugar_num) en la lista lugares que tenga su disponibilidad establecida como "No disponible" y se actualiza su disponibilidad a "Disponible".
Se crea una lista servicios_num con los números de los servicios que tengan su disponibilidad establecida como "No disponible".
Para cada número de servicio en servicios_num, se busca el servicio correspondiente en la lista servicios y se actualiza su disponibilidad a "Disponible".
Se actualiza la disponibilidad de la fecha en el calendario estableciendo el valor correspondiente en el diccionario eventos.
Luego, se calcula el costo total de la reserva llamando al método calcular_costo_total () utilizando el lugar_num y servicios_num como parámetros, y se calcula el monto de la seña llamando al método calcular_monto_sena() con el costo total como parámetro.

Se verifica la fecha de cancelación comparando la fecha actual con la fecha de la reserva y se calcula el reintegro correspondiente al 20% del valor de la seña si la fecha de cancelación está dentro de los 15 días previos al evento. En caso contrario, se imprime un mensaje indicando que no se realizará ningún reintegro.

Si la confirmación es "n" (No), se imprime un mensaje indicando que la operación se canceló.

15. `ejecutar_sistema(self)`: Ejecuta el sistema de reservas mostrando el menú principal y gestionando las opciones seleccionadas por el usuario.

La función ejecutar_sistema(self) es un método de la clase SistemaReservas. Este método se encarga de ejecutar el sistema de reservas y proporcionar una interfaz interactiva para que los usuarios interactúen con las diferentes funcionalidades del sistema.

Este método utiliza un bucle while True para mantenerse en ejecución hasta que el usuario decida salir del sistema (seleccionando la opción "6" en el menú). Dentro del bucle, muestra el menú de opciones y solicita al usuario que ingrese el número correspondiente a la opción deseada.
Si la opción es "1", se llama al método mostrar_fechas_disponibles () del objeto calendario para mostrar las fechas disponibles.
Si la opción es "2", se llama al método mostrar_lugares_disponibles () de la clase SistemaReservas para mostrar los lugares disponibles.
Si la opción es "3", se llama al método mostrar_servicios_disponibles () de la clase SistemaReservas para mostrar los servicios disponibles.
Si la opción es "4", se solicita al usuario los detalles de la reserva (fecha, número de lugar y números de servicios) y se llama al método realizar_reserva () de la clase SistemaReservas para realizar la reserva.
Si la opción es "5", se solicita al usuario la fecha de la reserva a cancelar y se llama al método cancelar_reserva () de la clase SistemaReservas para cancelar la reserva.
Si la opción es "6", se muestra un mensaje de despedida y se rompe el bucle while.
Si la opción ingresada no es válida, se muestra un mensaje de error.
Si ocurre una excepción durante la ejecución del sistema, se captura y se muestra un mensaje de excepción.
Cada método realiza diferentes tareas relacionadas con la carga y visualización de información, ingreso de datos de clientes, gestión de reservas y cancelación de reservas. El código sigue un flujo lógico para administrar un sistema de reservas.
