import numpy as np

connexions = np.array([102, 98, 115, 120, 90, 87, 130, 125, 95, 100, 105, 110])
mois = np.array(["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"])

print("Connexions mensuelles :")
for i in range(len(connexions)):
    print(mois[i],":",connexions[i],"connexions")

print("")
print("Statistiques annuelles:")
print("Total :", np.sum(connexions))
print("Moyenne :", round(np.mean(connexions),2))
print("Max :", np.max(connexions))
print("Min :", np.min(connexions))

print("")
while True:
 connexion = (len(connexions))
 if connexion > 110:
    print("⚠️ Risque de surcharge : Trop de connexions détectées.")
 else:
    print("✅ Activité normale.")
 break

print("")
print("Mois ou les connexions depassent 120 :")
for i in range(len(connexions)):
    if connexions[i] > 120:
     print(mois[i],":",connexions[i],"connexions")

print("")
print("Connexions apres filtrage (-10%):")
for i in range(len(connexions)):
    print(mois[i], ":", connexions[i] - (0.1 * connexions[i]), "connexions")

print("")
print("Connexions triees (decroissant) :")
print(np.sort(connexions*0.9)[::-1])
