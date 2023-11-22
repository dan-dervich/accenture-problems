def sumar_digitos(numero):
    if numero % 2 == 0:
        digitos = [int(digito) for digito in str(numero)]
        return sum(digitos)
    else:
        resultado = numero - 3
        if resultado < 0:
            resultado += 1
        return resultado
# ejemplo de uso
num = 123456789
resultado = sumar_digitos(num)
print(f"La suma de los dígitos del número {num} es: {resultado}")