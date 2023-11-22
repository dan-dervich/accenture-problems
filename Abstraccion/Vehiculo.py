class Vehiculo():
    def __init__(self, marca: str, modelo: str, velocidad_maxima: int):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Velocidad Maxima: {self.velocidad_maxima}'
class Coche(Vehiculo):
    def __init__(self, marca: str, modelo: str, velocidad_maxima: int):
        super().__init__(marca, modelo, velocidad_maxima)

    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Velocidad Maxima: {self.velocidad_maxima}'
class Motocicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, velocidad_maxima: int):
        super().__init__(marca, modelo, velocidad_maxima)

    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Velocidad Maxima: {self.velocidad_maxima}'
class Bicicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, velocidad_maxima: int):
        super().__init__(marca, modelo, velocidad_maxima)

    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Velocidad Maxima: {self.velocidad_maxima}'