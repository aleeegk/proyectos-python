### conversor de nombre ###

### Toma un nombre y lo muestra en mayúsculas, minúsculas, con la primera letra en mayúscula y al revés.

name = input("Ingresa tu nombre: ")

print(f"\nTu nombre en mayúsculas: {name.upper()}\n")
print(f"Tu nombre en minuscúlas: {name.lower()}\n")
print(f"Tu nombre con la primera letra mayúscula y luego todo minúscula: {name.capitalize()}\n")
print(f"Tu nombre al revés: {name[::-1]}\n")

