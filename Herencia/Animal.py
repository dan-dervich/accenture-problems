from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
    @abstractmethod
    def anos_pajaro(self):
        pass
    @abstractmethod
    def anos_perro(self):
        pass
    @abstractmethod
    def anos_gato(self):
        pass
    @abstractmethod
    def emitirSonido(self):
        pass
class Perro(Animal):
    def __init__(self, nombre: str, edad: int, raza: str):
        super().__init__(nombre, edad)
        self.raza = raza
    def anos_gato(self):
        pass
    def anos_pajaro(self):
        pass
    def anos_perro(self):
        return self.edad * 7
    def emitirSonido(self):
        return 'guau guau'
    def __str__(self):
        return f'nombre: {self.nombre}, edad: {self.edad}, raza: {self.raza}'
class Gato(Animal):
    def __init__(self, nombre: str, edad: int, raza: str):
        super().__init__(nombre, edad)
        self.raza = raza
    def anos_gato(self):
        return self.edad * 5
    def anos_pajaro(self):
        pass
    def anos_perro(self):
        pass
    def emitirSonido(self):
        return 'miau miau'
    def __str__(self):
        return f'nombre: {self.nombre}, edad: {self.edad}, raza: {self.raza}'
class Pajaro(Animal):
    def __init__(self, nombre: str, edad: int, raza: str):
        super().__init__(nombre, edad)
        self.raza = raza
    def anos_gato(self):
        pass
    def anos_pajaro(self):
        return self.edad * 3
    def anos_perro(self):
        pass
    def emitirSonido(self):
        return 'pio pio'
    def __str__(self):
        return f'nombre: {self.nombre}, edad: {self.edad}, raza: {self.raza}'