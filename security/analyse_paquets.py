import numpy as np

paquets = np.array([120, 85, 300, 150, 90, 450, 200, 175, 500, 130, 95, 400])

print("")
print(f"Tableau des paquets suspects:\n{paquets}")
print("")
print("="*5,"Statistiques","="*5)
print(f"Total:{np.sum(paquets)}")
print(f"Moyenne:{np.mean(paquets)}")
print(f"Maximum:{np.max(paquets)}")
print(f"Minimum:{np.min(paquets)}")
print(f"Ecart-type:{np.std(paquets)}")
print("")

if np.any(paquets > 250):
    print(f"⚠️ Activité réseau anormale détectée.\n")
    print(f"Paquets supérieurs à 250:")
    print(f"{paquets[paquets > 250]}")
else:
    print(f"✅ Activité réseau stable.")

reduction = paquets - paquets * 0.15
print("")
print(f"Tableau après réduction de 15%:\n{reduction}")
# Fixed: Sort descending with [::-1]
print(f"Tableau trié par ordre décroissant:\n{np.sort(reduction)[::-1]}")
print("")
print("="*5,"Analyse du trafic","="*5)

for paquet in paquets:
    if paquet < 150:
        print(f"{paquet}: ✅ Trafic faible")
    elif paquet >= 150 and paquet <= 300:
        print(f"{paquet}: ⚠️ Trafic moyen")
    else:  # paquet > 300
        print(f"{paquet}:  Trafic élevé")