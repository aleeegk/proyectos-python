### Calculadora ###

print("\nBienvenido a calculadora, ¿que quieres calcular hoy?")
while True:

    print("\nTeclea el número de lo que quieras calcular o escribe salir para cerrar el programa\n\t 1. Suma\n\t 2. Resta\n\t 3. División\n\t 4. Divisón Exacta\n\t 5. Multiplicación\n\t 6. Potencia\n\t 7. Modulo o resto")

    opcion = input("\nEscribe el numero de opción: ")

    if opcion == "1":                                   #Suma
        valor1 = input("\nIngresa el primer valor: ")
        valor2 = input("Ingresa el segundo valor: ")
        valor1 = float(valor1)
        valor2 = float(valor2)

        resultado = valor1 + valor2
        if resultado == int(resultado):
            print(f"\nEl resultado es: {int(resultado)}")
        else:
            print(f"\nEl resultado es: {resultado}")

    elif opcion == "2":                                   #Resta
        valor1 = input("\nIngresa el primer valor: ")
        valor2 = input("Ingresa el segundo valor: ")
        valor1 = float(valor1)
        valor2 = float(valor2)

        resultado = valor1 - valor2
        if resultado == int(resultado):
            print(f"\nEl resultado es: {int(resultado)}")
        else:
            print(f"\nEl resultado es: {resultado}")

    elif opcion == "3":                                   #División
        valor1 = input("\nIngresa el primer valor: ")
        valor2 = input("Ingresa el segundo valor: ")
        valor1 = float(valor1)
        valor2 = float(valor2)

        resultado = valor1 / valor2
        if resultado == int(resultado):
            print(f"\nEl resultado es: {int(resultado)}")
        else:
            print(f"\nEl resultado es: {resultado}")

    elif opcion == "4":                                   #División Exacta
        valor1 = input("\nIngresa el primer valor: ")
        valor2 = input("Ingresa el segundo valor: ")
        valor1 = float(valor1)
        valor2 = float(valor2)

        resultado = valor1 // valor2
        print(f"\nEl resultado es: {int(resultado)}")

    elif opcion == "5":                                   #Multiplicación
        valor1 = input("\nIngresa el primer valor: ")
        valor2 = input("Ingresa el segundo valor: ")
        valor1 = float(valor1)
        valor2 = float(valor2)

        resultado = valor1 * valor2
        if resultado == int(resultado):
            print(f"\nEl resultado es: {int(resultado)}")
        else:
            print(f"\nEl resultado es: {resultado}")

    elif opcion == "6":                                   #Potencia
        valor1 = input("\nIngresa el primer valor: ")
        valor2 = input("Ingresa el segundo valor: ")
        valor1 = float(valor1)
        valor2 = float(valor2)

        resultado = valor1 ** valor2
        if resultado == int(resultado):
            print(f"\nEl resultado es: {int(resultado)}")
        else:
            print(f"\nEl resultado es: {resultado}")

    elif opcion == "7":                                   #Modulo o Resto
        valor1 = input("\nIngresa el primer valor: ")
        valor2 = input("Ingresa el segundo valor: ")
        valor1 = float(valor1)
        valor2 = float(valor2)

        resultado = valor1 % valor2
        if resultado == int(resultado):
            print(f"\nEl resultado es: {int(resultado)}")
        else:
            print(f"\nEl resultado es: {resultado}")

    elif opcion.lower() == "salir":
        break
    
    continuar = input("\n¿Quieres continuar? (si/no): ")
    if continuar.lower() == "no":
        break