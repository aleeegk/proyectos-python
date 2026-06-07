### tarjeta de presentacion ###

"""El programa pide tu nombre, edad y ciudad, y luego imprime una tarjeta formateada con toda tu info."""

name = input("¿Cual es tu nombre?: ")

age = input("¿Cual es tu edad?: ")

city = input("¿Cual es tu ciudad?: ")

print(f"\nTu nombre es: {name}\nTu edad es: {age}\nTu ciudad es: {city}\n") #la f al inicio formatea el codigo y le agrega las variable que entre los {}

### tarjeta de presentacion mejorada ###

name = input("¿Cual es tu nombre?: ")

age = input("¿Cual es tu edad?: ")

city = input("¿Cual es tu ciudad?: ")

print("Tu nombre es: " + name.capitalize()) # Capitalize hace que cualquier texto ingresado la primera letra sea mayúscula y las de más minusculas
print("Tu edad es: " + age)
print("Tu ciudad es: " + city.capitalize())