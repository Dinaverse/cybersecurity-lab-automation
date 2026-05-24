courriels_suspects = [21, 5, 13, 8, 17, 2, 9, 14, 6, 11]

courriels_suspects.sort()
print("Liste triee : ", courriels_suspects)
print("Valeur minimale : ", min(courriels_suspects))
print("Valeur maximale : ", max(courriels_suspects))
print("Nombre total de courriels suspects : ", sum(courriels_suspects))
print("Moyenne par employe : ", sum(courriels_suspects)/len(courriels_suspects))