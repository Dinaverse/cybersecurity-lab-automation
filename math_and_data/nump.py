import numpy as np

incidents = np.array([12, 9, 14, 7, 8, 11, 13, 6, 15, 10, 9, 12])

print("Incidents mensuels :",incidents)

print("Statistiques annuelles :")
print("Nombre total d'incidents :", np.sum(incidents))
print("Nombre moyen d'incidents :", np.mean(incidents))
print("Maximum d'incidents detectes :", np.max(incidents))
print("Minimum d'incidents detectes :", np.min(incidents))

nombre_moyen = np.mean(incidents)

for compteur in range(len(incidents)):
    if incidents[compteur] > nombre_moyen:
        print("⚠️Attention : Tendance elevee d'incidents.")
    else:
        print("✅ Niveau d’incidents sous contrôle.")

for i in range(len(incidents)):
    if incidents[i] > 12:
     print("Les valeurs des incidents superieurs a 12 :",incidents[i])

reduction = incidents - (0.2 * incidents)
reduction_sorted = np.sort(reduction)
print("Incidents apres reduction de 20 % :", reduction)
print("Incidents reduit tries :", reduction_sorted)