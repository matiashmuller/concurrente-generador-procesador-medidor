# Programación Concurrente - UNAHUR

## Ejercicios

### Ejercicio 1: Generadores - Medidor

En este tipo de problemas hay varios hilos Generadores qué van incrementando aleatoriamente un recurso en común y varios hilos Medidores que pueden tomar muestras temporales del valor del recurso común y  realizar operaciones .

Por ejemplo, los hilos generadores podrían simular un conjunto de generadores eléctricos y el recurso común ser una variable que cuente la energía total generada por el conjunto. Los medidores pueden calcular la potencia (energía/tiempo) generada por el conjunto de generadores, calculando la diferencia del valor de la variable al comienzo y al final de un lapso de tiempo determinado.

Ejercicio:

Implemente un programa que ejecute dos hilos llamados generador y 10 hilos llamados medidor que acceden todos a una variable global energia.

Generador:

Los hilos generador debe ejecutar un loop infinito en el que incrementan en 1 la variable energia y esperan un retardo aleatorio entre 0.01 (1/100) y y 0.02 (2/100) antes de la siguiente iteración.
Ejemplo del loop Generador (operación básica, no incluye el código necesario para funcionar tal como lo piden los requerimientos):
```
while True:

    energia += 1

    time.sleep(random.randint(1,2)/100)
```
Nota: El uso de este ejemplo en la solución es opcional, puede modificarlo o incluso utilizar uno completamente diferente si lo consideran necesario.

Medidor:

Los hilos medidor deben deben ejecutar un loop infinito en el que se calcule en cuanto se incrementó la variable energía en el lapso de 1 segundo.  
Para esto debe tomar un valor inicial de la variable energía (valor0), esperar 1 segundo y luego tomar el valor final (valor1) y calcular la diferencia. Nota: debe asegurarse que los generadores continúen incrementando la variable energia entre las tomas del valor0 y valor1.
Deberá luego generar un mensaje indicando la diferencia como valor de potencia. Por ejemplo: Energía generada = 58kw, 
y esperar luego un retardo fijo de 2 segundos antes de volver a realizar una nueva medición.
No debe haber más de dos medidores tomando mediciones en forma simultánea.

Ejemplo del loop Generador (operación básica, no incluye el código necesario para funcionar tal como lo piden los requerimientos):
```
while True:

    valor0 = energia

    time.sleep(1)

    valor1 = energía

    logging.info(f'Potencia generada = {valor1 - valor0}kw')

    time.sleep(2)
```
Nota: El uso de este ejemplo en la solución es opcional, puede modificarlo o incluso utilizar uno completamente diferente si lo consideran necesario.


El programa debe funcionar para cualquier número de generadores y medidores


Debe colocarse el código suficiente para evitar condiciones de carrera, asegurar la condición de sincronización y evitar deadlocks.
Ejemplo de Salida:
```
17:33:31.267 [Thread-12] - Potencia generada = 60kw

17:33:32.270 [Thread-10] - Potencia generada = 54kw

17:33:32.271 [Thread-17] - Potencia generada = 54kw

17:33:33.275 [Thread-9] - Potencia generada = 62kw

17:33:33.275 [Thread-14] - Potencia generada = 62kw
```
Solución:
```
generador-medidor.py
```

### Ejercicio 2: Generadores - Procesadores

En este tipo de problemas varios hilos Generadores y Procesadores que acceden a un número finito de objetos modificándolos o realizando operaciones con información contenida en los mismos. Cada vez que un Generador o Procesador toma un objeto este deja de estar disponible para los demás procesos hasta que termine de utilizarlo y lo devuelva. Si un proceso no encuentra objetos disponibles debe esperar a que otro proceso devuelva alguno.

Ejercicio:

El siguiente fragmento de código implementa una clase mensajero y luego instancia una lista mensajeros con dos objetos de esta clase 
```
class mensajero():

   def __init__(self, id):

       self.id = id


   def crear_mensaje(self, msg):

       self.msg = msg


   def obtener_mensaje(self):

       return self.msg


mensajeros = []

for i in range(2):

   mensajeros.append(mensajero(i))
```
Implemente un programa que ejecute 3 hilos llamados generador y 5 hilos llamados procesador todos utilizando la lista global mensajeros definida e instanciada más arriba.

Generador: 
Cada hilo generador debe tomar un objeto mensajero de la lista mensajeros y un nombre al azar de la siguiente lista: 
nombres = ["Juan", "Mariana", "Daniel", "Ezequiel", "Gimena", "Emilce","Gabiel", "Gabriela","Lorena", "Agustin", "Julieta"]
Y componer un string con el nombre elegido y cargarlo en el atributo msg del objeto mensajero seleccionado. Por ejemplo: ” mensaje de Gabriel ”.
Luego imprimirá un mensaje indicando el mensaje que recibió, por ejemplo: 
mensaje de Gabriela recibido.
El objeto mensajero con el atributo msg modificado debe ser devuelto para que pueda ser utilizado por otro hilo.
Esto lo debe hacer en forma continua (loop infinito) esperando un tiempo aleatorio entre 2 y 5 segundos entre iteraciones.
Ejemplo del loop Generador (operación básica, no incluye el código necesario para funcionar tal como lo piden los requerimientos):
```
while True:

    mensaje = (f'mensaje de {nombres[random.randint(0,10)]}')

    mensajero = mensajeros.pop(0)

    mensajero.crear_mensaje(mensaje)

    mensajeros.append(mensajero)

    logging.info(f'{mensaje} recibido')

    time.sleep(random.randint(2,5))
```
Nota: El uso de este ejemplo en la solución es opcional, puede modificarlo o incluso utilizar uno completamente diferente si lo consideran necesario.

Procesador:

Cada hilo procesador debe tomar un objeto mensajero de la lista mensajeros y luego, utilizando métodos y atributos del objeto seleccionado imprimir un mensaje indicando la identidad del mensajero (id) y el mensaje recibido (msg). Por ejemplo:
Mensajero-1 recibió un mensaje de Gabriela
Esto lo debe hacer en forma continua (loop infinito) esperando un tiempo aleatorio entre 1 y 2 segundos entre iteraciones.
Ejemplo del loop Generador (operación básica, no incluye el código necesario para funcionar tal como lo piden los requerimientos):
```
while True:

    mensajero = mensajeros.pop(0)

    logging.info(f'Mensajero-{mensajero.id} recibió un {mensajero.obtener_mensaje()}')

    mensajeros.append(mensajero)

    time.sleep(random.randint(1,2))
```
Nota: El uso de este ejemplo en la solución es opcional, puede modificarlo o incluso utilizar uno completamente diferente si lo consideran necesario.

El programa debe funcionar para cualquier número de generadores y procesadores

Debe colocarse el código suficiente para evitar condiciones de carrera, asegurar la condición de sincronización y evitar deadlocks.

```
Ejemplo de salida:

21:24:30.701 [Thread-2] - mensaje de Daniel recibido

21:24:30.701 [Thread-3] - mensaje de Ezequiel recibido

21:24:30.701 [Thread-4] - Mensajero-1 recibió un mensaje de Daniel

21:24:30.701 [Thread-5] - Mensajero-0 recibió un mensaje de Ezequiel

21:24:30.702 [Thread-6] - Mensajero-1 recibió un mensaje de Daniel

21:24:30.702 [Thread-7] - Mensajero-0 recibió un mensaje de Ezequiel

21:24:30.702 [Thread-8] - Mensajero-1 recibió un mensaje de Daniel

21:24:31.706 [Thread-6] - Mensajero-0 recibió un mensaje de Ezequiel

21:24:32.706 [Thread-5] - Mensajero-1 recibió un mensaje de Daniel

21:24:32.706 [Thread-7] - Mensajero-0 recibió un mensaje de Ezequiel

21:24:32.706 [Thread-8] - Mensajero-1 recibió un mensaje de Daniel

21:24:32.706 [Thread-6] - Mensajero-0 recibió un mensaje de Ezequiel

21:24:32.706 [Thread-4] - Mensajero-1 recibió un mensaje de Daniel

21:24:33.711 [Thread-7] - Mensajero-0 recibió un mensaje de Ezequiel

21:24:34.702 [Thread-1] - mensaje de Gabriela recibido

21:24:34.706 [Thread-2] - mensaje de Daniel recibido

21:24:34.709 [Thread-5] - Mensajero-1 recibió un mensaje de Gabriela

21:24:34.709 [Thread-6] - Mensajero-0 recibió un mensaje de Daniel
```
Solución:
```
generador-procesador-medidor.py
```