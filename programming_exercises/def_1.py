# 1. Définition de la fonction
def detecter_fichiers_dangereux(liste):
    extensions_critiques = (".exe", ".js")
    for fichier in liste:
        if fichier.endswith(extensions_critiques):
            print(f"ALERTE : Le fichier '{fichier}' est potentiellement dangereux !")

# 2. Programme principal
fichiers = ["rapport.pdf", "install.exe", "vacances.jpg", "script.js", "notes.txt"]

detecter_fichiers_dangereux(fichiers)
