import logging
import random
import threading
import time

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

energia = 0
cantMedidores = 0
lock = threading.Lock()

class Generador(threading.Thread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        while True:
            with lock:
                global energia
                energia += 1
            time.sleep(random.randint(1,2)/100)

class Medidor(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            global cantMedidores
            global energia
            estaMidiendo = False
            with lock:
                if cantMedidores <2:
                    valor0 = energia
                    cantMedidores +=1
                    estaMidiendo = True
            time.sleep(1)
            with lock:
                if estaMidiendo:
                    valor1 = energia
                    logging.info(f'Potencia generada = {valor1 - valor0} kw')
                    cantMedidores-=1
            time.sleep(2)


def lanzarGeneradores(cantidad):
    for i in range(cantidad):
        generador = Generador()
        generador.start()

def lanzarMedidores(cantidad):
    for i in range(cantidad):
        medidor = Medidor()
        medidor.start()

def main():
    lanzarGeneradores(2)
    lanzarMedidores(10)

main()