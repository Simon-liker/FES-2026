###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

encaminador = 'Router-01'
ubicacio = 'Habitacion 3'
nombre_ports = 4
ences = True

print(f"El encaminador: {encaminador} situado en {ubicacio} y con" 
f"{nombre_ports} puertos está encendido: {ences}" )

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.

gb_inclosos = 8
gb_consumits = 3
print("Los GB que quedan son: ", gb_inclosos - gb_consumits)

gb_consumits = 4
gb_restants = gb_consumits - gb_inclosos