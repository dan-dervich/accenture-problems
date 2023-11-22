class ContextoNotificadorEventos:
    def _enter_(self):
        print("Entrando al bloque de código.")
    
    def _exit_(self, exc_type, exc_value, traceback):
        print("Saliendo del bloque de código.")