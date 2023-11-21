class Coche:
    def __init__(self):
        self.__velocidad = 0  # private attribute
        self.kilometraje = 0  # public attribute

    def acelerar(self, incremento: int):
        self.__velocidad += incremento

    def registrar_kilometraje(self, distancia: int):
        if distancia > 0:
            self.kilometraje += distancia
        else:
            print("La distancia debe ser mayor que cero.")
