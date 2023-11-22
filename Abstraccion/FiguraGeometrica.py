from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho: int, alto: int):
        self.ancho = ancho
        self.alto = alto

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> int:
        pass
    def mostrarInfo(self) -> None:
        print(f"Alto: {self.alto}\nAncho: {self.ancho}\n")
class Circulo(FiguraGeometrica):
    def __init__(self, radio:int):
        super().__init__(radio, radio)
        self.radio = radio

    def area(self):
        return 3.1416 * (self.radio**2)

    def perimetro(self):
        return 2 * 3.1416 * self.radio
class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho: int, alto: int):
        super().__init__(ancho, alto)
    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

class Triangulo(FiguraGeometrica):
    def __init__(self, ancho: int, alto: int):
        super().__init__(ancho, alto)
    def area(self):
        return (self.ancho * self.alto) / 2

    def perimetro(self):
        return self.ancho + self.alto + self.alto