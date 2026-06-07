### detector de palíndromos ###

print("Bienvenido al detector de palíndromos.")

palindromo = input("Por favor ingresa una palabra: ")

if palindromo == palindromo[::-1]:
    print("Tu palabra es un palíndromo")
else:
    print("No es un palíndromo")