trafic_mo = [120, 130, 125, 110, 400, 118, 122, 119,420, 115, 117, 500, 113, 121, 600, 140,135, 128, 123, 127, 150, 112, 116, 132]

Moyenne = round(sum(trafic_mo)/len(trafic_mo),2)
Seuil = Moyenne * 1.5

pic_suspects = []

for i in trafic_mo:
    if i > Seuil:
        pic_suspects.append(i)

nombre_suspects = len(pic_suspects)


print("Moyenne du trafic :", Moyenne , "Mo")
print("Seuil pour pic suspect :", Seuil , "Mo")
print("Valeurs depassant le seuil :", pic_suspects)
print("Nombre total de pic suspects:", nombre_suspects)
print("Trafic maximum enregistre ;", max(trafic_mo) ,"Mo")