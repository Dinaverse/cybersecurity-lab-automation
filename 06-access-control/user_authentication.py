utilisateurs_connectes = ["alice", "bob", "root", "hacker123", "admin", "carla", "test"]
liste_interdits = ["root", "hacker123", "admin", "test"]

utilisateurs_autorises = []

for utilisateur in utilisateurs_connectes:
    if utilisateur not in liste_interdits:
        utilisateurs_autorises.append(utilisateur)

print("Utilisateur autorises: ", utilisateurs_autorises)