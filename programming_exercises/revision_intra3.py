# Analyse du temps moyen de réponse d’un serveur

import math

while True:
 temps_moyen = int(float(input("Entrez le temps moyen de reponse attendu :")))
 if temps_moyen >= 0:
     break
 else:
    print("Erreur : la valeur doit etre positive ou nulle")

while True:
 temps_moyen_observe = int(float(input("Entrez le temps moyen de reponse reellement observe :")))
 if temps_moyen_observe >= 0:
     break
 else:
    print("Erreur : la valeur doit etre positive ou nulle")

print("Ecart absolu :", round(abs(temps_moyen - temps_moyen_observe),2))
print("Total des deux temps :", round(temps_moyen + temps_moyen_observe,2))
print("Moyenne des deux temps :", round((temps_moyen + temps_moyen_observe)/2,2))
print("Arrondi superieur du temps observe :", math.ceil(temps_moyen_observe))
print("Arrondi inferieur du temps observe :", math.floor(temps_moyen_observe))
print("Temps observe tronque :", math.trunc(temps_moyen_observe))