
from __future__ import annotations

class Persona():
    def _init_(self, nombre: str, edad: int, dni: str):
        self.nombre = nombre
        self.edad = edad
        self.__dni = dni

    def _str_(self):
        return "Nombre: " + self.nombre + " Edad: " + str(self.edad) + " DNI: " + self.__dni
    
class Empleado(Persona):
    def _init_(self, nombre: str, edad: int, dni: str, salario: int, cargo: str):
        super()._init_(nombre, edad, dni)
        self.salario = salario
        self.cargo = cargo

    def getSalario(self) -> int:
        return self.salario
    
    def _str_(self):
        return super()._str_() + " Salario: " + str(self.salario) + " Cargo: " + self.cargo
    
class Gerente(Empleado):
    def _init_(self, nombre: str, edad: int, dni: str, salario: int, departamento: str):
        super()._init_(nombre, edad, dni, salario, "Gerente")
        self.departamento = departamento

    def getDepartamento(self) -> str:
        return self.departamento
    
    def _str_(self):
        return super()._str_() + " Departamento: " + self.departamento
    
class Departamento():
    def _init_(self, nombre: str, gerente: Gerente):
        self.nombre = nombre
        self.gerente = gerente
        self.empleados: list[Empleado] = []

    def getGerente(self) -> Gerente:
        return self.gerente
    
    def addEmpleado(self, empleado: Empleado):
        self.empleados.append(empleado)
    
    def removeEmpleado(self, empleado: Empleado):
        self.empleados.remove(empleado)

    def getEmpleados(self) -> list[Empleado]:
        return self.empleados
    
    def getPersonal(self) -> list[Empleado and Gerente]:
        personal = []
        personal.append(self.gerente)
        for empleado in self.empleados:
            personal.append(empleado)
        return personal

#Instanciando objetos
fullStackDev = Empleado("Juan", 25, "47026765", 85000, "Full Stack Developer")
frontEndDev = Empleado("Pedro", 23, "29571094", 75000, "Front End Developer")
backEndDev = Empleado("Maria", 24, "59872647", 80000, "Back End Developer")
gerente = Gerente("Jose", 30, "12345678", 100000, "Desarrollo")

#Instanciando departamento y asignando gerente
departamento = Departamento("Desarrollo", gerente)

#Agregando empleados al departamento
departamento.addEmpleado(fullStackDev)
departamento.addEmpleado(frontEndDev)
departamento.addEmpleado(backEndDev)

#Armando situaciones donde se usan los objetos
print("Empleados del departamento de " + departamento.nombre + ": ")
for empleado in departamento.getEmpleados():
    print(" - " + empleado.nombre)

print("\nGerente del departamento de " + departamento.nombre + ": " + departamento.getGerente().nombre)
print("\n----------\n")

departamento.removeEmpleado(fullStackDev)
print("Se elimino al empleado " + fullStackDev.nombre + " del departamento de " + departamento.nombre)
print("\n----------\n")

print("Empleados del departamento de " + departamento.nombre + ": ")
for empleado in departamento.getEmpleados():
    print(" - " + empleado.nombre)

print("\n----------\n")
print("Información de cada empleado final del departamento de " + departamento.nombre + ":\n")

for empleado in departamento.getPersonal():
    print(empleado)