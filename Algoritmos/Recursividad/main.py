def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(n):
    if n <= 1:
        return 0
    if is_prime(n):
        return n + sum_primes(n - 1)
    else:
        return sum_primes(n - 1)

# Ejemplo de uso
num = 10
result = sum_primes(num)
print(f"La suma de todos los números primos desde 1 hasta {num} es: {result}")


def MCD(a, b):
    if b == 0:
        return a
    else:
        return MCD(b, a % b)
    
# Ejemplo de uso
a = 48
b = 18
result = MCD(a, b)
print(f"El máximo común divisor entre {a} y {b} es: {result}")

def invert_cadena(cadena):
    if len(cadena) == 1:
        return cadena
    else:
        return cadena[-1] + invert_cadena(cadena[:-1])

# Ejemplo de uso
cadena = "Hello World!"
result = invert_cadena(cadena)
print(f"La cadena invertida de '{cadena}' es: '{result}'")