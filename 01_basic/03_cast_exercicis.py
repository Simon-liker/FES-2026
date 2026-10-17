###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.

paquets = int(input("Introdueix quants paquets ha rebut l'encaminador: \n"))
print("El total de paquets rebuts es ", paquets + 1200)

# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.

vel_mbps = float(input("Introdueix la velocitat de la connexió en Mbps: \n"))
print("La velocitat en MB/s és ", vel_mbps / 8)