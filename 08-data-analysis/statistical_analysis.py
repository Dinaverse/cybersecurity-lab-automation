from math import sqrt

x1 = int(input("Entrez le nombre de la position x1 : "))
y1 = int(input("Entrez le nombre de la position y1 : "))

x2 = int(input("Entrez le nombre de la position x2 : "))
y2 = int(input("Entrez le nombre de la position y2 : "))

distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("la distance entre les deux points est : ", round(distance,2))
