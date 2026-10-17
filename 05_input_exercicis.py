###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.

tecnic = input("Escriba el nombre del tecnico: ")
xarxa = input("Escriba el nombre de la red: ")

print(f"El tecnico es {tecnic} y la red es {xarxa}")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.

longitud = float(input("Escriba la longitud de la fibra en km: "))
velocidad = float(input("Escriba la velocidad de la transmision en km/s: "))

tiempo = longitud / velocidad
print(f"Tarda {tiempo} segundos en recorrer el enlace")


# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.

horas = float(input("Introduzca el numero de horas de trabajo: "))
precio_hora = float(input("Introduzca el precio por hora para instalar la red"))
precio_material = float(input("Introduzca el precio del material"))

costo_total = horas*precio_hora*precio_material
print("El precio total de la instalación es: ", costo_total)