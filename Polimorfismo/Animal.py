import sys
sys.path.insert(0, '..')
from Herencia import Gato, Perro, Pajaro

animales = [Perro("tini", 3, "caniche"), Gato("asoka", 3, "Abisinio"), Pajaro("pepe", 3, "loro")]

for animal in animales:
    print(animal.emitirSonido())