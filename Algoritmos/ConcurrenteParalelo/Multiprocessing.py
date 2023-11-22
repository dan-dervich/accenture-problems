import multiprocessing
import time

def funcion1():
    print("Inicio de la función 1")
    time.sleep(2)
    print("Fin de la función 1")
# Hago la funcion 2
def funcion2():
    print("Inicio de la función 2")
    time.sleep(5)
    print("Fin de la función 2")

if __name__ == '__main__':
    proceso1 = multiprocessing.Process(target=funcion1)
    proceso2 = multiprocessing.Process(target=funcion2)

    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()

    print("Ambos terminaron su ejecución")