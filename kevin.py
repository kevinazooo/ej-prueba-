total = 0
items = []


while True:
    print("    ***Tienda de Juegos***:    ")
    print("   |Juegos               precios|")
    print("1. |Catan                $29.990|")
    print("2. |Dixit                $19.990|")
    print("3. |Exploding Kittens    $19.990|")
    print("4. |Finalizar compra            |")
    print("5. |Salir                       |")
    op = int(input("Selecciona un juego: "))

    if op == 1:
        items.append(("Catan", 29990))
        total += 29990
    elif op == 2:
        items.append(("Dixit", 19990))
        total += 199902
    elif op == 3:
        items.append(("Exploding Kittens", 19990))
        total += 19990
    elif op == 4:
        nombre_cliente = input("Ingresa tu nombre: ")
        print("***BOLETA***")
        for item in items:
            print(f"{item[0]} ${item[1]}")
        print(f"-----------Total: ${total}")
        print(f"Gracias {nombre_cliente} por su compra")
        break
    elif op == 5:

        print("Hasta luego gracias")
        break
