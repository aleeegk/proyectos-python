### generador de contraseña basico ###

print("Bienvenido al generador de contraseñas basico")

print("\nPor favor no ingresar una palabra que contenga simbolos, emojis, numeros o caracteres especiales en general. Solo numeros")
palabra = input("\nIngresa una palabra por favor: ")

palabra = palabra.lower()

password = palabra.replace("a", "0").replace("b", "1").replace("c", "2").replace("d", "3").replace("e", "4").replace("f", "5").replace("g", "6").replace("h", "7").replace("i", "8").replace("j", "9").replace("k", "10").replace("l", "11").replace("m", "12").replace("n", "13").replace("ñ", "14").replace("o", "15").replace("p", "16").replace("q", "17").replace("r", "18").replace("s", "19").replace("t", "20").replace("u", "21").replace("v", "22").replace("w", "23").replace("x", "24").replace("y", "25").replace("z", "26")

print(f"\nTu nueva contraseña es: {password}")