import json

def load_inventory():

    try:
        with open("inventory.json", "r") as file:
            inventario = json.load(file)
            return inventario

    except FileNotFoundError:
        return {}
    
    
def save_inventory(inventario):

    with open("inventory.json", "w") as file:
        json.dump(inventario, file, indent=4)
    

def add_product(inventario, producto, cantidad):

    if inventario.get(producto):
        print('No se puede agregar un producto existente')

    else:
        inventario[producto] = cantidad
        print(f'\nEl producto "{producto}" ha sido agregado con éxito con una cantidad de "{cantidad}" unidades')
        save_inventory(inventario)


def update_cantidad(inventario, producto):

    if producto in inventario:
        nueva_cantidad = int(input('Escriba la nueva cantidad del producto: '))
        inventario[producto] = nueva_cantidad
        print(f'\nAl producto "{producto}" se le ha actualizado la cantidad a {nueva_cantidad} unidades')
        save_inventory(inventario)

    else:
        print('\nEl producto no se puede actualizar porque no existe!')


def view_inventory(inventario):

    if not inventario:
        print("\nEl inventario está vacío")
        return

    print('\n-------- INVENTARIO --------')

    for producto, cantidad in sorted(inventario.items()):
        print(f'    {producto:<15} → {cantidad}')


def del_product(inventario, producto):

    if producto in inventario:
        inventario.pop(producto)
        print(f'\nEl producto "{producto}" ha sido eliminado exitosamente')
        save_inventory(inventario)

    else:
        print(f'El producto "{producto}" no existe')


def search_product(inventario, producto):

    if producto in inventario:
        cantidad = inventario[producto]
        print("\nProducto encontrado:")
        print(f"{producto:<15} | {cantidad}")

    else:
        print("\nEl producto no existe en el inventario.")


def salir():
    print('--------------------------')
    print('-------- Gracias! --------')
    print('--- Hasta la proxima!! ---')
    print('--------------------------')