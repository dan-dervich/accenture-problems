def Precondicion(check_func):
    def Decorador(func):
        def Wrapper(*args):
            if not check_func(*args):
                raise ValueError("Precondición no superada")
            return func(*args)
        return Wrapper
    return Decorador