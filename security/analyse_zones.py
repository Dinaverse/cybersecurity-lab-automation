from math import pi

rayons_zones = [3.5, 7.2, 5.0, 2.8, 6.1]

Perimetres = []

for i in range(0,len(rayons_zones)):
    Perimetre = 2 * pi * rayons_zones[i]
    Perimetres.append(Perimetre)

Perimetres.sort()
print("Perimetres des zones securisees : ")

for i in range(0,len(Perimetres)):
    print(round(Perimetres[i],2))

print("Plus petit perimetre : ", round(Perimetres[0],2))
print("Plus grand perimetre : ", round(Perimetres[-1],2))
print("Moyenne des perimetres : ", round(sum(Perimetres)/len(Perimetres),2))
print("Perimetres tries en ordre croissant : ", [round(i, 2) for i in Perimetres])

