def Checkear_Tipos(tipos_correctos):
    def Decorador(func):
        def Wrapper(*args):
            if any(not isinstance(arg, typ) for arg, typ in zip(args, tipos_correctos)):
                raise ValueError("Tipos de argumentos incorrectos")
            return func(*args)
        return Wrapper
    return Decorador