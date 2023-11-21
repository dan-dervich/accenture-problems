from abc import ABC, abstractmethod
from abc import ABC, abstractmethod
from typing import List

class Forma(ABC):
    def __init__(self, dimensiones: List[int], color: str):
        self.dimensiones = dimensiones
        self.color = color
    @abstractmethod
    def area(self):
        pass
    def perimetro(self):
        pass

class Rectangulo(Forma):
    def __init__(self, dimensiones: List[int], color: str):
        super().__init__(dimensiones, color)
        self.ancho = dimensiones[0]
        self.alto = dimensiones[1]
    def area(self):
        return self.ancho * self.alto
    def perimetro(self):
        return 2 * (self.ancho + self.alto)
    def __str__(self):
        return f'Ancho: {self.ancho}, Alto: {self.alto}, Color: {self.color}'
class Circulo(Forma):
    def __init__(self, radio:int, color: str):
        super().__init__((radio, radio), color)
        self.radio = radio
    def area(self):
        return 3.1416 * self.radio ** 2
    def perimetro(self):
        return 2 * 3.1416 * self.radio
    def __str__(self):
        return f'Radio: {self.radio}, Color: {self.color}'