class CompteBancaire:

    # Definition des attributs de la CompteBancaire
    __numero_compte : str
    __nom_titulaire : str
    __solde : float
    __actif : bool

    # Constructeur qui initialise les quatres attributs numero_compte, nom_titulaire, solde et actif
    def __init__(self, numero_compte, nom_titulaire, solde, actif):
        self.__numero_compte = numero_compte
        self.__nom_titulaire = nom_titulaire
        self.__solde = float(solde)
        self.__actif = actif

    # Getters
    def get_numero_compte(self):
        return self.__numero_compte
    def get_nom_titulaire(self):
        return self.__nom_titulaire
    def get_solde(self):
        return self.__solde
    def is_actif(self):
        return self.__actif
    # Setters
    def set_titulaire(self,nom_titulaire):
        self.__nom_titulaire = nouveau_nom

    def set_actif(self,etat):
        self.__actif = etat

    # Methodes

    def deposer(self,montant:float):
        if montant <= 0:
            print("Erreur : le montant doit etre positif.")
            return False

        if not self.__actif:
            print("Erreur : impossible de deposer, le compte est bloque.")
            return False

        self.__solde += montant
        print(f"Confirmation : {montant} depose. Nouveau solde : {self.__solde:.2f}$")
        return True

    def retirer(self,montant:float):
        if montant <= 0:
            print("Erreur : le montant doit etre positif.")
            return False

        if montant > self.__solde:
            print("Erreur: Solde insuffisant pour le retrait!")
            return False

        if not self.__actif:
            print("Erreur : impossible de deposer, le compte est bloque.")
            return False

        self.__solde -= montant
        print(f"Confirmation : {montant} retire. Nouveau solde : {self.__solde:.2f}$")
        return True

    def afficher_compte(self):
        print(f"Numero de compte :{self.__numero_compte}\nNom titulaire :{self.__nom_titulaire}\nSolde :{self.__solde:.2f}$\nActif :{self.__actif}")

    #----------------programme principale-----------------------
nouveau_nom = "Martine"
TestCompte = CompteBancaire("101","Alice","200",False)
TestCompte1 = CompteBancaire("102","Bob","2000",True)

TestCompte.afficher_compte()
print("-"*25)
print("")
TestCompte.deposer(100)
TestCompte.retirer(202)
print("-"*25)
print("")
TestCompte.set_titulaire(nouveau_nom)
TestCompte.afficher_compte()
print("")
print("-"*25)
TestCompte1.afficher_compte()
print("-"*25)
print("")
TestCompte1.deposer(150)
TestCompte1.retirer(22001)
print("-"*25)
print("")
TestCompte1.afficher_compte()