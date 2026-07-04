# Calcul de la Prime Cybersecurite

# lectures des donnees
salaire_annuel_base = int(float(input("Entrez le salaire annuel de base : ")))
nombre_incident_resolus = int(input("Entrez le nombre de incident resolus : "))
nombre_annee_anciennete = int(input("Entrez le nombre de annees d'anciennete : "))

# Calcul de la Prime de performance
if nombre_incident_resolus < 30:
        Prime_perfomance = salaire_annuel_base * 0.05 + nombre_annee_anciennete
elif nombre_incident_resolus <= 70:
        Prime_perfomance = salaire_annuel_base * 0.10 + nombre_annee_anciennete
else:
        Prime_perfomance = salaire_annuel_base * 0.15 + nombre_annee_anciennete

# Calcul de la Prime d'anciennete
if nombre_annee_anciennete <= 2:
        Prime_annee_anciennete = 500
elif nombre_annee_anciennete <= 5:
        Prime_annee_anciennete = 1500
else:
        Prime_annee_anciennete = 3000

# Affiche les resultats d'execution
print("Prime de performance :" , Prime_perfomance,"$")
print("Prime d'anciennete :", Prime_annee_anciennete, "$")
print("Salaire annuel total :", salaire_annuel_base + Prime_perfomance + Prime_annee_anciennete,"$")