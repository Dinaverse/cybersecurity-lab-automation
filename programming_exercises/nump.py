import numpy as np

connexions = np.array([5, 4, 3, 2, 1, 1, 2, 3, 8, 12, 20, 30, 25, 28, 27, 24, 22, 20, 18, 15, 10, 8, 6, 32])

print("Total des connections :", np.sum(connexions))
print("Moyenne horaire :",round(np.mean(connexions),2))
print("Ecart-type :", round(np.std(connexions),2))
print("Moyenne + ecart-type= :", np.mean(connexions) + np.std(connexions))

print("Heures suspectes (connection > moyenne + ecart-type) :")

connexions_suspectes = np.mean(connexions) + np.std(connexions)

for compteur in range(len(connexions)):
    c=connexions[compteur]
    if c > connexions_suspectes:
        print("Heure",compteur, ":",c, "connexions (suspect)")

print("Systeme de detection automatique :")
for compteur in range(len(connexions)):
    c=connexions[compteur]
    if c > 30:
        print("Tentative d'attaque detecte a l'heure ", compteur, ":",c, "connexions")


