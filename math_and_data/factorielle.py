from math import factorial

while True:
  n = int(float(input("Entrez un nombre entier positif : ")))

  if n <= 0:
    print("Le nombre n'est pas valide, il faut saisir un nombre positif ou nulle")
  else:
    print("la factorielle de", n, "est", factorial(n))
    break

