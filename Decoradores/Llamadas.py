def Decorador(func):
    def Wrapper(*args):
        res = func(*args)
        print(f'Llamada a {func._name_} con argumentos {args}. Resultado: {res}')
        return res
    return Wrapper