

nombre = input("Hola, ¿Como te llamas?\n")
print(f"Hola {nombre} ¿Como estas?")

age = input("¿Cuantos años tienes?\n")
print(f"dentro de 20 años tendraas {int(age) + 20} años")

print("Obtener multiples valores")
country, city = input("¿De que pais y ciudad eres?\n").split(",")
print(f"Tu pais es {country} y tu ciudad es {city}")
