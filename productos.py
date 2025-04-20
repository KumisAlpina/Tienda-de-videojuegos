class Producto:
    def __init__(self,nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"
    
class Videojuego(Producto):
    def __init__(self, nombre: str, precio: float, cantidad: int, genero: str, plataforma: str):
        super().__init__(nombre, precio, cantidad)
        self.genero = genero
        self.plataforma = plataforma

    def __str__(self):
        return f"{super().__str__()}, Genero: {self.genero}, Plataforma: {self.plataforma}"
    
class Consola(Producto):
    def __init__(self, nombre: str, precio: float, cantidad: int, modelo: str, almacenamiento: int):
        super().__init__(nombre, precio, cantidad)
        self.modelo = modelo
        self.almacenamiento = almacenamiento

    def __str__(self):
        return f"{super().__str__()}, Modelo: {self.modelo}, Almacenamiento: {self.almacenamiento}GB"

class tienda:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def listar_productos(self):
        for producto in self.productos:
            print(producto)

    def vender_producto(self, nombre: str, cantidad: int):
        for producto in self.productos:
            if producto.nombre == nombre and producto.cantidad >= cantidad:
                producto.cantidad -= cantidad
                print(f"Se ha vendido {cantidad} de {nombre}.")
                return
        print(f"No hay suficiente stock de {nombre} o no existe.")


         