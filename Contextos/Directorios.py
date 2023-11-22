import os

class ContextoCambiarDirectorio:
    def _init_(self, nuevaRuta: str):
        self.nuevaRuta = nuevaRuta
        self.rutaOrigen = None

    def _enter_(self):
        self.rutaOrigen = os.getcwd()
        os.chdir(self.newPath)
    
    def _exit_(self, exc_type, exc_value, traceback):
        os.chdir(self.rutaOrigen)