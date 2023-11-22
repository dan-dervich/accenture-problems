# import sys
# sys.path.insert(0, '..')
from Exepciones.main import DivisionByZeroError, IndexOutOfRangeError, InvalidNumberError, FileNotFoundError, KeyNotFoundError
try:
    raise DivisionByZeroError("Division por cero")
except DivisionByZeroError as e:
    print(e)
try:
    raise IndexOutOfRangeError("Indice fuera de rango")
except IndexOutOfRangeError as e:
    print(e)
try:
    raise InvalidNumberError("Numero invalido")
except InvalidNumberError as e:
    print(e)
try:
    raise FileNotFoundError("Archivo no encontrado")
except FileNotFoundError as e:
    print(e)
try:
    raise KeyNotFoundError("Llave no encontrada")
except KeyNotFoundError as e:
    print(e)