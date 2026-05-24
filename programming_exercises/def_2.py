# 1. Création de la fonction
def detecter_acces_nuit(liste):
    for heure_complete in liste:
        # Extraire les deux premiers caractères (HH)
        heure_seule = int(heure_complete[:2])

        # Vérifier si l'heure est comprise entre 0 et 5
        if 0 <= heure_seule <= 5:
            print(heure_complete)


# 2. Programme principal
acces = ["08:10", "03:20", "14:45", "00:15", "01:30", "09:00"]

# 3. Appel de la fonction
detecter_acces_nuit(acces)
