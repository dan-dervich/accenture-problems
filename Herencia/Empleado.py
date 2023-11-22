from abc import ABC, abstractmethod
class Empleado(ABC):
    def __init__(self, nombre: str, salario: int, departamento: str):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento
    @abstractmethod
    def calcular_salario():
        pass

class Gerente(Empleado):
    def __init__(self, nombre: str, salario: int, departamento: str):
        super().__init__(nombre, salario, departamento)
    def __str__(self):
        return f'Nombre: {self.nombre}, Salario: {self.salario}, Departamento: {self.departamento}'
    def calcular_salario(self):
        # 1000 es el bono por ser gerente
        return self.salario + 1000
class Trabajador(Empleado):
    def __init__(self, nombre: str, salario: int, departamento: str):
        super().__init__(nombre, salario, departamento)
    def __str__(self):
        return f'Nombre: {self.nombre}, Salario: {self.salario}, Departamento: {self.departamento}'
    def calcular_salario(self):
        # 500 es el bono por ser trabajador
        return self.salario + 500