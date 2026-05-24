try:
    with open("rapport.txt", "r") as fichier:
        lignes = fichier.readlines()

    # Compter les lignes contenant "alerte"
    nb_alertes = sum(1 for ligne in lignes if "alerte" in ligne.lower())
    print("Nombre de lignes contenant 'alerte':", nb_alertes)

except FileNotFoundError:
    print("Le fichier 'rapport.txt' n'existe pas")