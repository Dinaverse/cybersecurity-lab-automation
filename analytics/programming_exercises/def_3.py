# 1. Fonction pour afficher les IP uniques
def afficher_ips_uniques(liste_ips):
    print("Adresses IP uniques détectées :")
    # Utiliser set() est le moyen le plus rapide de supprimer les doublons
    uniques = set(liste_ips)
    for ip in uniques:
        print(f"- {ip}")

# 2. Fonction pour compter les occurrences
def compter_occurrences(liste_ips, ip_cible):
    # La méthode .count() permet de compter facilement les éléments
    nombre = liste_ips.count(ip_cible)
    return nombre

# --- Programme principal ---

ips = [
    "<INTERNAL_IP>", "<INTERNAL_IP>", "<INTERNAL_IP>", "<INTERNAL_IP>",
    "<INTERNAL_IP>", "<INTERNAL_IP>", "<INTERNAL_IP>", "<INTERNAL_IP>",
    "<INTERNAL_IP>"
]

# Affichage des IP uniques
afficher_ips_uniques(ips)

# Interaction avec l'utilisateur
print("\n--- Vérification d'une adresse ---")
ip_a_tester = input("Saisissez une adresse IP à vérifier : ")

# Calcul du nombre d'apparitions
total = compter_occurrences(ips, ip_a_tester)

# Affichage du résultat final
if total == 0:
    print(f"👉 L’adresse IP {ip_a_tester} n’a pas été détectée.")
else:
    print(f"👉 L’adresse IP {ip_a_tester} apparaît {total} fois.")
