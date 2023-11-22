from __future__ import annotations

class Producto():
    def __init__(self, nombre: str, precio: int, stock: int, descripcion: str):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.descripcio = descripcion
class CarritoCompra():
    def __init__(self):
        self.productos: list[Producto] = []
    def agregar_producto(self, producto: Producto) -> bool:
        if producto:
            self.productos.append(producto)
            return True
        return False
    def mostrar_productos(self) -> None:
        for producto in self.productos:
            print(f'nombre: {producto.nombre}, stock: {producto.stock}, precio: {producto.precio}')
    def precio_total(self) -> int:
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total
    def buscar_producto(self, nombre: str) -> Producto or None:
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
    def eliminar_producto(self, nombre: str) -> bool:
        producto = self.buscar_producto(nombre)
        if producto:
            self.productos.remove(producto)
            return True
        return False
    def modificar_producto(self, nombre: str, precio: int, stock: int, descripcion: str) -> bool:
        producto = self.buscar_producto(nombre)
        if producto:
            producto.precio = precio
            producto.stock = stock
            producto.descripcion = descripcion
            return True
        return False
    def mostrar_carrito(self) -> None:
        for producto in self.productos:
            print(producto)
    def eliminar_carrito(self) -> bool:
        self.productos.clear()
        return True
    def modificar_carrito(self, nombre: str, precio: int, stock: int, descripcion: str) -> bool:
        producto = self.buscar_producto(nombre)
        if producto:
            producto.precio = precio
            producto.stock = stock
            producto.descripcion = descripcion
            return True
        return False
class Cliente():
    def __init__(self, nombre: str, apellido: str, dni: str, direccion: str, telefono: int, email: str):
        self.nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.carrito_compra = CarritoCompra()

cliente = Cliente("Juan", "Dela", "1452334", "Santa fe 2345", 1133333333, "juandela@hotmail.com")
cliente.carrito_compra.agregar_producto(Producto("Coca Cola", 100, 10, "Gaseosa"))
cliente.carrito_compra.agregar_producto(Producto("Sprite", 100, 10, "Gaseosa"))
cliente.carrito_compra.agregar_producto(Producto("Pepsi", 100, 10, "Gaseosa"))

cliente.carrito_compra.mostrar_productos()
print(cliente.carrito_compra.precio_total())
cliente.carrito_compra.eliminar_producto("Coca Cola")
cliente.carrito_compra.mostrar_productos()
print(cliente.carrito_compra.precio_total())
cliente.carrito_compra.eliminar_carrito()
cliente.carrito_compra.mostrar_productos()
print(int(cliente.carrito_compra.precio_total()))