import sys
sys.path.insert(0, '..')
from Abstraccion import Circulo, Rectangulo, Triangulo


    
figuras = [Circulo(5), Rectangulo(3, 4), Triangulo(4, 5)]

for figura in figuras:
    print(figura.area())
    print(figura.perimetro())
    figura.mostrarInfo()