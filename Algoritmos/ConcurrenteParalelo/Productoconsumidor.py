import threading
import time
import random

cola_compartida = [1, 2, 3]

def productor():
    while True:
        item = random.randint(1, 100)
        cola_compartida.append(item)
        print(f'Productor produjo: {item}')
        time.sleep(random.randint(1, 3)) 

def consumidor():
    while True:
        item = cola_compartida.pop(0)
        print(f'Consumidor consumió: {item}')
        time.sleep(random.randint(1, 3))

hilo_productor = threading.Thread(target=productor)
hilo_productor.daemon = True
hilo_productor.start()

hilo_consumidor = threading.Thread(target=consumidor)
hilo_consumidor.daemon = True
hilo_consumidor.start()

time.sleep(999)