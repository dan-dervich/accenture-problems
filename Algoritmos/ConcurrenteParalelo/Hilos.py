import threading
import time

def funcion1():
    print("Inicio de la función 1")
    time.sleep(1)
    print("Fin de la función 1")

def funcion2():
    print("Inicio de la función 2")
    time.sleep(2)
    print("Fin de la función 2")

hilo1 = threading.Thread(target=funcion1)
hilo2 = threading.Thread(target=funcion2)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print("Ambos terminaron su ejecución")