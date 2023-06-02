import logging
import random
import threading
import time

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

energia = 0
cantMedidores = 0
lock = threading.Lock()

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

nombres = ["Juan", "Mariana", "Daniel", "Ezequiel", "Gimena", "Emilce","Gabriel", "Gabriela","Lorena", "Agustin", "Julieta"]


class Generador(threading.Thread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        while True:
            with lock:
                global mensajeros
                global nombres
                mensajero = mensajeros.pop(0)
                nombre = random.choice(nombres)
                mensajero.crear_mensaje(f'mensaje de {nombre}')
                logging.info(f'El {mensajero.obtener_mensaje()} ha sido recibido.')
                mensajeros.append(mensajero)
            time.sleep(random.randint(2,5))

class Procesador(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            with lock:
                global mensajeros
                mensajero = mensajeros.pop(0)
                logging.info(f'El mensajero id: {mensajero.id} recibio un {mensajero.obtener_mensaje()}')
                mensajeros.append(mensajero)
            time.sleep(random.randint(1,2))


def lanzarGeneradores(cantidad):
    for i in range(cantidad):
        generador = Generador()
        generador.start()

def lanzarProcesadores(cantidad):
    for i in range(cantidad):
        procesador = Procesador()
        procesador.start()

def main():
    lanzarGeneradores(3)
    lanzarProcesadores(5)

main()