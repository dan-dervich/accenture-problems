
class Estudiante:
    def __init__(self, nombre: str, edad: int, calificaciones: str):
        self.__nombre = nombre
        self.__edad = edad
        self.__calificaciones = calificaciones

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_calificaciones(self):
        return self.__calificaciones
