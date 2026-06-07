### Contador de caracteres ###

# Bienvenida
print("Bienvenido al contador de caracteres.")

# Ingresar una frase
frase = input("\nEscribe una frase: ")

# Contar caracteres
print(f"\nTu frase tiene en total {len(frase)} caracteres.")

# Contar espacios
print(f"Tu frase tiene en total {frase.count(" ")} espacios.")

# Contar vocales
vocales = 0
for letra in frase:
    if letra.lower() in "aeiou":
        vocales = vocales + 1
        
print(f"Tu frase tiene en total {vocales} vocales.")