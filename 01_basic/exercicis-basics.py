###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

nom = input("Escribe tu nombre: ")
ciudad = input("Escribe tu ciudad: ")

### Completa aquí

print(f"{nom}, \n {ciudad}")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola món"
d = True
e = None

### Completa aquí

print(f"{type(a)}, {type(b)}, {type(c)}, {type(c)}, {type(d)}, {type(e)}")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí

cadena = float(int("12345"))
num = int(3.99)

print(f"Se ve que, al pasar de variable, los decimales de {num} se eliminan y se redondea al 3")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 40 anys i faig 1.75 metres"
#name = "Marc"
#age = 40

### Completa aquí

nom = "Simon"
edat = 20

print(f"Soy {nom} y tengo {edat} años")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

var = 3.14

print("El resultat es: ", int(var / round(var)))

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí

temp = float(input("Introduzca una temperatura en celsius: "))
temp_f = (temp * 9/5) + 32

print(f"La temperatura en celsius es {temp} y en fahrenheit es { temp_f}")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

### Completa aquí

compte = float(input("Introduzca el total de la cuenta: "))
perc_prop = float(input("Introduzca el porcentaje de propina "))

print(f"El total de propina es {compte*perc_prop:.2f}")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

### Completa aquí

cont = input("Introduzca la contraseña: ")

if (len(cont) >= 8):
    print("Contrasenya valida")
else:
    print("Contrasenya no valida")