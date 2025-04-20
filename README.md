# Tienda de Videojuegos

Este proyecto es una aplicación de consola escrita en Python que simula la gestión de una tienda de videojuegos. Permite al usuario realizar diversas operaciones como agregar productos (videojuegos y consolas), listar los productos disponibles, y vender productos. El programa utiliza un enfoque orientado a objetos para modelar los productos y la tienda.

## Estructura del Proyecto

El proyecto está compuesto por dos archivos principales:

1. **`productos.py`**: Contiene las clases que representan los productos (videojuegos y consolas) y la tienda.
2. **`tienda.py`**: Es el archivo principal que ejecuta la lógica de la aplicación y permite la interacción con el usuario.

### Archivo `productos.py`

Este archivo define las siguientes clases:

#### Clase `Producto`
- Es la clase base para todos los productos de la tienda.
- **Atributos**:
  - `nombre` (str): Nombre del producto.
  - `precio` (float): Precio del producto.
  - `cantidad` (int): Cantidad disponible en el inventario.
- **Métodos**:
  - `__init__`: Inicializa los atributos del producto.
  - `__str__`: Devuelve una representación en texto del producto.

#### Clase `Videojuego`
- Hereda de la clase `Producto` y representa un videojuego.
- **Atributos adicionales**:
  - `genero` (str): Género del videojuego (por ejemplo, acción, aventura, etc.).
  - `plataforma` (str): Plataforma en la que se puede jugar el videojuego (por ejemplo, PlayStation, Xbox, etc.).
- **Métodos**:
  - `__init__`: Inicializa los atributos específicos del videojuego.
  - `__str__`: Devuelve una representación en texto del videojuego, incluyendo los atributos heredados y los específicos.

#### Clase `Consola`
- Hereda de la clase `Producto` y representa una consola de videojuegos.
- **Atributos adicionales**:
  - `modelo` (str): Modelo de la consola.
  - `almacenamiento` (int): Capacidad de almacenamiento de la consola en GB.
- **Métodos**:
  - `__init__`: Inicializa los atributos específicos de la consola.
  - `__str__`: Devuelve una representación en texto de la consola, incluyendo los atributos heredados y los específicos.

#### Clase `tienda`
- Representa la tienda de videojuegos.
- **Atributos**:
  - `nombre` (str): Nombre de la tienda.
  - `productos` (list): Lista de productos disponibles en la tienda.
- **Métodos**:
  - `__init__`: Inicializa el nombre de la tienda y la lista de productos.
  - `agregar_producto`: Agrega un producto a la lista de productos.
  - `listar_productos`: Muestra todos los productos disponibles en la tienda.
  - `vender_producto`: Permite vender un producto, reduciendo su cantidad en el inventario. Si no hay suficiente stock o el producto no existe, muestra un mensaje de error.

### Archivo `tienda.py`

Este archivo implementa la lógica principal de la aplicación. Utiliza las clases definidas en `productos.py` para interactuar con el usuario y gestionar la tienda.

#### Flujo del Programa
1. **Inicialización**:
   - Se importa la clase `tienda` y las clases de productos (`Videojuego` y `Consola`) desde `productos.py`.
   - Se crea una instancia de la tienda con el nombre "Tienda de videojuegos".

2. **Menú Principal**:
   - El programa muestra un menú con las siguientes opciones:
     1. **Agregar producto**:
        - Permite al usuario agregar un nuevo producto a la tienda.
        - El usuario elige entre dos tipos de productos: `videojuego` o `consola`.
        - Según el tipo seleccionado, se solicitan los datos específicos del producto y se agrega a la tienda.
     2. **Lista de productos**:
        - Muestra todos los productos disponibles en la tienda, incluyendo sus detalles.
     3. **Vender producto**:
        - Permite al usuario vender un producto.
        - Se solicita el nombre del producto y la cantidad a vender.
        - Si el producto existe y hay suficiente stock, se reduce la cantidad en el inventario.
        - Si no hay suficiente stock o el producto no existe, se muestra un mensaje de error.
     4. **Salir**:
        - Finaliza la ejecución del programa.

3. **Interacción con el Usuario**:
   - El programa utiliza un bucle `while` para mantener el menú activo hasta que el usuario elija la opción de salir.
   - Se valida la entrada del usuario para asegurarse de que las opciones seleccionadas sean válidas.

## Ejecución del Programa

Para ejecutar el programa, simplemente ejecuta el archivo `tienda.py` en un entorno de Python. Asegúrate de que ambos archivos (`productos.py` y `tienda.py`) estén en el mismo directorio.
