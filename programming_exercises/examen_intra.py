SCORE1 = 50

while True:
    Vulnerabilites = int(input("Nombre de vulnerabilites detectees : "))
    if Vulnerabilites <= 5 :
        SCORE1 = 40
    elif Vulnerabilites <= 10 :
        SCORE1 = 30
    else:
        SCORE1 = 10

    Retard = int(input("Nombre de mises a jour critiques en retard : "))
    if Retard == 0 :
        SCORE2 = 50
    elif Retard <= 3 :
        SCORE2 = 35
    else:
        SCORE2 = 15
    break

print("Points pour les vulnerabiltes :", SCORE1)
print("Points pour les mises a jours :", SCORE2)
print("Score final : ", SCORE1 + SCORE2, "/100")