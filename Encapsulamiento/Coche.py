class Coche:
    def __init__(self):
        self.__velocidad = 0  # private attribute
        self.kilometraje = 0  # public attribute

    def acelerar(self, incremento: int) -> bool:
        self.__velocidad += incremento
        return True

    def registrar_kilometraje(self, distancia: int) -> bool:
        if distancia > 0:
            self.kilometraje += distancia
            return True
        # print("La distancia debe ser mayor que cero.")
        return False
