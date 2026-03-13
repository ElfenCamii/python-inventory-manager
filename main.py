inventario = {}

print('-----------------------------------')
print('---- Bienvenidos al inventario ----')
print('-----------------------------------')

def add_product(a, b):
    if inventario.get(a):
        print('No se puede agregar un producto existente')
    else:
        inventario[a] = b
        print(f'\nEl producto "{a}" a sido agregado con exito con una cantidad de "{b}" unidades')
def update_cantidad(a):
    if inventario.get(a):
        user_update_cantidad = int(input('Escriba la nueva cantidad del producto: '))
        inventario[a] = user_update_cantidad
        print(f'\nAl producto "{a}" se le a actualizado la cantidad de {user_update_cantidad} unidades')
    else:
        print('\nEl producto no se puede actualizar porque no existe!')
def del_product(a):
    if inventario.get(a):
        inventario.pop(a)
        print(f'\nEl producto "{a}" a sido eliminado exitosamente')
    else:
        print(f'El producto "{a}" no existe')
def salir():
    print('--------------------------')
    print('-------- Gracias! --------')
    print('--- Hasta la proxima!! ---')
    print('--------------------------')

while True:
    print('''
\nEscribe el número de la opción que desees:
          
    1. Abregar un producto
    2. Actualizar la cantidad de un producto
    3. Mostrar inventario
    4. Eliminar un producto
    5. Salir
''')
    try:
        user_action = int(input('Que desea hacer: '))
        if user_action == 5:
            salir()
            break
        elif user_action == 1:
            user_add_producto = input('\nEscriba el nombre del producto que desea agregar: ').lower()
            user_add_cantidad = int(input('Escriba la cantidad existente del producto: '))
            add_product(user_add_producto, user_add_cantidad)
        elif user_action == 2:
            user_update_product = input('\nIngrese el nombre del producto que desea actualizar: ').lower()
            update_cantidad(user_update_product)
        elif user_action == 3:
            print('\nProductos en el inventario:')
            for producto, cantidad in inventario.items():
                print(f'    {producto} → {cantidad}')
        elif user_action == 4:
            user_pop_product = input('\nEscriba el producto que desea eliminar: ')
            del_product(user_pop_product)

    except ValueError:
        print('El valor ingresado no es un número!')
        print('Intentelo de nuevo')
