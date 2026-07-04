SCORE = 100

while True:
    Pare_feu = input("Le pare-feu est-il active ? (oui/non) : ")
    if Pare_feu == "non":
        SCORE1 = -40
    elif Pare_feu == "oui":
        SCORE1 = 0

    Systeme = input("Le systeme est-il mis a jour regulierement ? (oui/non) : ")
    if Systeme == "non":
        SCORE2 = -20
    elif Systeme == "oui":
        SCORE2 = 0

    Antivirus = input("Un antivirus est-il actif ? (oui/non) : ")
    if Antivirus == "non":
        SCORE3 = -20
    elif Antivirus == "oui":
        SCORE3 = 0

    Ports = int(input("Combien de ports sont ouverts ? : "))
    if Ports < 20:
        SCORE4 = 0
    else:
        tranches = (Ports - 20) // 10
        SCORE4 = tranches * 10

    break

SCORE_TOTAL = SCORE + SCORE1 + SCORE2 + SCORE3 - SCORE4

print("Score de securite final : ", SCORE_TOTAL, "/ 100")