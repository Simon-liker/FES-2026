###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.

n1 = int(input("Introduzca un numero: "))
n2 = int(input("Introduzca un numero: "))

if(n1 > n2):
    print("El mayor es: ", n1)
elif(n1 == n2):
    print("El mayor es: ", n2)
else:
    print("Son iguales")

# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).

num1 = float(input("Introduzca un numero: "))
num2 = float(input("Introduzca otro numero: "))
op = input("Introduzca una operacion: ")

if(op == "+"):
    print("El resultado es: ", num1 + num2)
elif(op == "-"):
    print("El resultado es: ", num1 - num2)
elif(op == "/"):
    if (num2 != 0):
        print("El resultado es: ", num1 / num2)
    else:
        print("Error, esta tratando de dividir entre 0")
elif(op == "*"):
    print("El resultado es: ", num1 * num2)
else:
    print(f"{op} No es una operacion admitida")

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.

any = int(input("Introduzca un año: "))

if (any % 4 == 0 and (any % 100 != 0 or any % 400 == 0)):
    print("l'any es de trespas")
else:
    print("L'any no es de trespas")

# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)

edat = int(input("Introduzca su edad: "))

if(0 <= edat <= 0.2):
    print("Ets un nadó")
elif(3 <= edat <= 12):
    print("Ets un infant")
elif (13 <= edat <= 17):
    print("Ets un adolescent")
elif (18 <= edat <= 64):
    print("Ets un adult")
elif(65 <= edat):
    print("Ets una persona gran")
else:
    print("No pots tenir edat negativa")
    
# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

nivel = float(input("Introduzca el nivel de la señal"))

if (nivel >= -50):
    print("La qualitat es excellent")
elif (-67 <= nivel <= -50):
    print("La qualitat es bona")
elif (-75 <= nivel <= -67 ):
    print("La qualitat es feble")
elif (nivel <= -75):
    print("La qualitat es molt feble")

# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

potencia = float(input("Introduzca la potencia optica en dBm: "))

if (-27 <= potencia <= -8):
    print("El nivel es aceptable")
elif(potencia > -8):
    print("El nivel es muy alto")
else:
    print("El nivel es muy bajo")

# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

cost = float(input("Introduzca el costo total de los datos moviles"))

if(cost > 20):
    consum = cost - 20
    print(f"Se ha superado el limite en {consum}Gb")
else:
    print("No se ha superado el limite")

# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

ences_los = bool(input("Introduzca si el indicador LOS esta encendido (1) o no (0): "))
int_router = bool(input("Indique 1 si el router tiene internet y 0 si no: "))

if ences_los and int_router:
    print("Parece que funciona bien")
elif not ences_los:
    print("Compruebe el servicio del proveedor")
elif not int_router:
    print("Compruebe el cable de fibra")    

# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

perc_bateria = float(input("Introduzca el porcentaje de bateria en el SAI (entre 0 y 1): "))

if perc_bateria < .2:
    print("El nivel es crítico")
elif (0.2 <= perc_bateria <= .49):
    print("El nivel es bajo")
elif 50 <= perc_bateria:
    print("El nivel es suficiente")
else:
    print("El nivel esta fuera del rango")

# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.



# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.

# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.

# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.
