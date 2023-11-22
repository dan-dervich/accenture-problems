class DivisionByZeroError(Exception):
    pass

try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    if num2 == 0:
        raise DivisionByZeroError("Error: No se puede dividir entre cero.")
    
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)
    
except DivisionByZeroError as e:
    print(e)

class IndexOutOfRangeError(Exception):
    pass

try:
    numeros = str.split(input("Ingrese una lista de números separados por espacios: "))
    indice = int(input("Ingrese el índice: "))
    
    if indice >= len(numeros):
        raise IndexOutOfRangeError("Error: El índice está fuera de rango.")
    
    elemento = numeros[indice]
    print("El elemento en el índice", indice, "es:", elemento)
    
except IndexOutOfRangeError as e:
    print(e)

class ValueError(Exception):
    pass

try:
    cadena = input("Ingrese una cadena que represente un número: ")
    numero = float(cadena)
    print("El número ingresado es:", numero)
    
except ValueError as e:
    print(e)

class FileNotFoundError(Exception):
    pass

try:
    archivo = open("archivo_no_existente.txt", "r")
    contenido = archivo.read()
    archivo.close()
    print(contenido)
except FileNotFoundError as e:
    print("Error: El archivo no existe.")
# except FileNotFoundError as e:
#     print(e)

class KeyNotFoundError(Exception):
    pass

try:
    diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}
    
    clave = "clave4"
    
    if clave not in diccionario:
        raise KeyNotFoundError("Error: La clave no existe en el diccionario.")
    
    valor = diccionario[clave]
    print("El valor correspondiente a la clave", clave, "es:", valor)
    
except KeyNotFoundError as e:
    print(e)
