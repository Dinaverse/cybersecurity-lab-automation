Liste = [12, 3, 7, 0, 25, 4, 9, 17, 6, 10]

Liste.sort(reverse=False)
print("Tentatives echouees triees : ", Liste)

print("Nombre nombre minimum de tentatives echoues : ", Liste[0])
print("Nombre maximum de tentatives echoues : ", Liste[-1])
print("Nombre total de tentatives echoues : ", sum(Liste))
print("Moyenne de tentatives echouees par serveur : ", sum(Liste)/len(Liste))