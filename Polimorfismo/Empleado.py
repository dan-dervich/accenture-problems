import sys
sys.path.insert(0, '..')
from Herencia import Empleado, Gerente, Trabajador

# Utilizar la clase Empleado del ejercicio de herencia y aplicar polimorfismo para calcular el salario de acuerdo con las reglas específicas de cada tipo de empleado. Luego, crear una lista de
# empleados de diferentes tipos y utilizar el polimorfismo para calcular sus salarios.

# Crear una lista de empleados de diferentes tipos
empleados = [
    Empleado("Juan", 1000, "Ventas"),
    Gerente("Pedro", 2000, "Ventas"),
    Trabajador("Maria", 1500, "Sistemas")
]

# Utilizar el polimorfismo para calcular los salarios de los empleados
for empleado in empleados:
    salario = empleado.calcular_salario()
    print(f"El salario de {empleado.nombre} es: {salario}")
