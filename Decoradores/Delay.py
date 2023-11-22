import time

def Delay(seconds):
    def Decorador(func):
        def Wrapper(*args):
            print(f'Esperando {seconds} segundos antes de ejecutar la función')
            time.sleep(seconds)
            return func(*args)
        return Wrapper
    return Decorador