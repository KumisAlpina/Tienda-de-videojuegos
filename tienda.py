from productos import tienda, Videojuego, Consola


tienda = tienda('Tienda de videojuegos')

while True:
    print('\n ============Tienda de videojuegos===========')
    print('1. Agregar producto')
    print('2. Ver productos')
    print('3. Vender producto')
    print('4. Salir')

    opcion = input('Seleccione una opción: ')

    if opcion == '1':
        nombre = input('Ingrese el nombre del producto: ')
        precio = float(input('Ingrese el precio del producto: '))
        cantidad = int(input('Ingrese la cantidad del producto: '))
        tipo = input('Ingrese el tipo de producto (videojuego/consola): ').lower()

        if tipo == 'videojuego':
            genero = input('Ingrese el género del videojuego: ')
            plataforma = input('Ingrese la plataforma del videojuego: ')
            tienda.agregar_producto(Videojuego(nombre, precio, cantidad, genero, plataforma))
        elif tipo == 'consola':
            modelo = input('Ingrese el modelo de la consola: ')
            almacenamiento = int(input('Ingrese el almacenamiento de la consola (GB): '))
            tienda.agregar_producto(Consola(nombre, precio, cantidad, modelo, almacenamiento))
        else:
            print('Tipo de producto no válido.')
    
    elif opcion == '2':
        print('\nLista de productos:')
        tienda.listar_productos()

    elif opcion == '3':
        nombre = input('Ingrese el nombre del producto a vender: ')
        cantidad = int(input('Ingrese la cantidad a vender: '))
        tienda.vender_producto(nombre, cantidad)

    elif opcion == '4':
        print('Saliendo de la tienda...')
        break

    else:
        print('Opción no válida. Intente de nuevo.')