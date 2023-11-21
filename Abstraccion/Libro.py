class Libro():
    def __init__(self, titulo: str, autor: str, precio: int):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def __str__(self):
        return f'Titulo: {self.titulo}, Autor: {self.autor}, Precio: {self.precio}'

class Libreria():
    def __init__(self):
        self.libros: list[Libro] = []

    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)
    def precio_total(self):
        total = 0
        for libro in self.libros:
            total += libro.precio
        return total
    def buscar_libro(self, titulo: str):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None