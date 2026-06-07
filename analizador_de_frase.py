### Analizador de frase ###

# Bienevenida
print("Bienvenido al analizador de frases.")

print("\nPor favor ingresa tu frase.")

# Ingresar una frase
frase = input("\nIngresa una frase: ")

# Contador de palabras
if len(frase.split()) == 1:
    print(f"\nTu frase tiene {len(frase.split())} palabra.")
else:
    print(f"\nTu frase tiene {len(frase.split())} palabras.")

# Contador de espacios
print(f"Tu frase tiene en total {frase.count(" ")} espacios.")

# Contador de vocales
vocales = 0
for letra1 in frase:
    if letra1.lower() in "aeiou":
        vocales = vocales + 1

print(f"Tu frase tiene en total {vocales} vocales.")

# Contador de letras del abecedario
letras = 0
for letra2 in frase:
    if letra2.lower() in "abcdefghijklmnñopqrstuvwxyz":
        letras = letras + 1

print(f"Tu frase tiene en total {letras} letras.")

# Contador de caracteres especiales
caracteres_especiales = 0
for letra3 in frase:
    if letra3.lower() not in "abcdefghijklmnñopqrstuvwxyz ":
        caracteres_especiales = caracteres_especiales + 1
        
print(f"Tu frase tiene en total {caracteres_especiales} caracteres especiales.")

# Contador de caracteres en general
caracteres = len(frase)
print(f"Tu frase tiene en total {caracteres} caracteres.")