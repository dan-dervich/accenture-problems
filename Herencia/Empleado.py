class Empleado():
    def __init__(self, nombre: str, salario: int, departamento: str):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

class Gerente(Empleado):
    def __init__(self, nombre: str, salario: int, departamento: str):
        super().__init__(nombre, salario, departamento)
    def __str__(self):
        return f'Nombre: {self.nombre}, Salario: {self.salario}, Departamento: {self.departamento}'
    
class Trajador(Empleado):
    def __init__(self, nombre: str, salario: int, departamento: str):
        super().__init__(nombre, salario, departamento)
    def __str__(self):
        return f'Nombre: {self.nombre}, Salario: {self.salario}, Departamento: {self.departamento}'