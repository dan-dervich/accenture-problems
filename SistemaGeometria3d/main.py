from __future__ import annotations
from abc import ABC, abstractmethod

class Punto3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
class Figura3d:
    def __init__(self, nombre: str, puntos: list[Punto3d]):
        self.nombre = nombre
        self.puntos = puntos
    @abstractmethod
    def calcular_area(self) -> int:
        pass
    def calcular_volumen(self) -> int:
        pass

class Cubo(Figura3d):
    def __init__(self, nombre: str, puntos: list[Punto3d]):
        super().__init__(nombre, puntos)
    # def calcular_area(self) -> int:
    #     return 6*self.puntos[0].x*self.puntos[0].y
    # def calcular_volumen(self) -> int:
    #     return self.puntos[0].x*self.puntos[0].y*self.puntos[0].z
class Esfera(Figura3d):
    def __init__(self, nombre: str, puntos: list[Punto3d]):
        super().__init__(nombre, puntos)
    # def calcular_area(self) -> int:
    #     return 4*3.14*self.puntos[0].x*self.puntos[0].x
    # def calcular_volumen(self) -> int:
    #     return 4/3*3.14*self.puntos[0].x*self.puntos[0].x*self.puntos[0].x
class Cilindro(Figura3d):
    def __init__(self, nombre: str, puntos: list[Punto3d]):
        super().__init__(nombre, puntos)
    # def calcular_area(self) -> int:
    #     return 2*3.14*self.puntos[0].x*self.puntos[0].x+2*3.14*self.puntos[0].x*self.puntos[0].y
    # def calcular_volumen(self) -> int:
    #     return 3.14*self.puntos[0].x*self.puntos[0].x*self.puntos[0].y