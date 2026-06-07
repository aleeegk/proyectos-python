### Lista de compra ###

lista_compra = []

while True:
    print("\n¿Qué quieres hacer?")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Ver lista")
    print("4. Salir")

    opcion = input("\nElige una opción: ")

    # Añadir producto
    if opcion == "1":
        while True:
            agregar_producto = input("\n¿Qué producto quieres añadir?: ")
            lista_compra.append(agregar_producto)
            print(f"✅ '{agregar_producto}' ha sido añadido.")
            
            otro = input("\n¿Quieres añadir otro? (si/no): ")
            if otro.lower() == "no":
                break

    # Eliminar producto
    elif opcion == "2":
        if not lista_compra:
            print("\n❌ La lista está vacía.")
        else:
            while True:
                print(f"\nLa lista actual es esta: {', '.join(lista_compra)}.")
                eliminar_producto = input("¿Qué producto quieres eliminar? (o escribe 'cancelar'): ")
                if eliminar_producto.lower() == "cancelar":
                    break
                eliminar_producto: str = input("¿Qué producto de la lista quieres eliminar?: ")
                if eliminar_producto in lista_compra:
                            lista_compra.remove(eliminar_producto)
                            break
                else:
                    print("\n❌ No existe ese producto en la lista, por favor escribir uno existente.")

    # Ver lista
    elif opcion == "3":
        if not lista_compra:
            print("\n❌ La lista está vacía.")
        else:
            print("\nAquí está tu lista actual:")
            for producto in lista_compra:
                print(f"- {producto}")

    # Salir
    elif opcion.lower() == "4" or opcion.lower() == "salir":
        break

    # Opcion no válida
    else:
        print("\nOpción no válida, intenta de nuevo.")