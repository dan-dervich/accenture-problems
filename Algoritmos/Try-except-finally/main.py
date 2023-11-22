try:
#     # Abrir el archivo
    archivo = open("archivo.txt", "r")
    
    # Leer el contenido del archivo
    contenido = archivo.read()
    
    # Imprimir el contenido
    print(contenido)
    
    archivo.close()
except FileNotFoundError:
    print("El archivo no existe.")
    
except Exception as e:
    print("Ocurrió un error:", str(e))
    
finally:
    # Cerrar el archivo
    print("final programa")

try:
    numero1 = float(input("Ingrese un número: "))
    numero2 = float(input("Ingrese otro número: "))
    operacion = input("Ingrese una operación matemática (+, -, *, /): ")
    
    if operacion == "+":
        resultado = numero1 + numero2
    elif operacion == "-":
        resultado = numero1 - numero2
    elif operacion == "*":
        resultado = numero1 * numero2
    elif operacion == "/":
        resultado = numero1 / numero2
    else:
        raise Exception("Opción inválida.")
    
    print("El resultado de la operación", numero1, operacion, numero2, "es:", resultado)
    
except ValueError:
    print("Error: Los números ingresados no son válidos.")
    
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
    
except Exception as e:
    print("Error:", str(e))
    
finally:
    print("Fin del programa.")



try:
    archivo_entrada = open(input("Ingrese el nombre del archivo de entrada: "), "r")
    
    contenido = archivo_entrada.read()
    
    archivo_entrada.close()
    
    archivo_salida = open(input("Ingrese el nombre del archivo de salida: "), "w")
    
    archivo_salida.write(contenido)
    
    archivo_salida.close()
    
except FileNotFoundError:
    print("Error: El archivo no existe.")
    
except Exception as e:
    print("Error:", str(e))
    
finally:
    print("Fin del programa.")
