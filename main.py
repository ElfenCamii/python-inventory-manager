import inventory_manager
import os
os.system('cls')

inventario = inventory_manager.load_inventory()

# inventory_manager.add_product(inventario, "arroz", 10)
# inventory_manager.update_cantidad(inventario, "arroz")
# inventory_manager.del_product(inventario, "arroz")

# print(inventario)

print('-----------------------------------')
print('---- Bienvenidos al inventario ----')
print('-----------------------------------')



while True:
    print('''
\nEscribe el número de la opción que desees:
          
    1. Abregar un producto
    2. Actualizar cantidad producto
    3. Mostrar inventario
    4. Eliminar un producto
    5. Salir
''')
    try:
        user_action = int(input('Que desea hacer: '))
        if user_action == 5:
            inventory_manager.salir()
            break
        elif user_action == 1:
            user_add_producto = input('\nEscriba el nombre del producto que desea agregar: ').strip().lower()
            user_add_cantidad = int(input('Escriba la cantidad existente del producto: '))
            inventory_manager.add_product(inventario, user_add_producto, user_add_cantidad)
        elif user_action == 2:
            user_update_product = input('\nIngrese el nombre del producto que desea actualizar: ').strip().lower()
            inventory_manager.update_cantidad(inventario, user_update_product)
        elif user_action == 3:
            if not inventario:
                print("\nEl inventario está vacío")
            else:
                print('\n-------- INVENTARIO --------')
                for producto, cantidad in sorted(inventario.items()):
                    print(f'    {producto:<15} → {cantidad}')
        elif user_action == 4:
            user_pop_product = input('\nEscriba el producto que desea eliminar: ')
            inventory_manager.del_product(inventario, user_pop_product)

    except ValueError:
        print('El valor ingresado no es un número!')
        print('Intentelo de nuevo')
