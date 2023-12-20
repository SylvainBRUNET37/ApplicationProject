from affichage import *
from jeu import *
from verification import *

def main():
    #iNbColonne = int(input("Saisissez le nombre de colonne que vous souhaitez :"))
    #iNbLigne = int(input("Saisissez le nombre de ligne que vous souhaitez :"))
    #iNbJetonVictoire = int(input("Saisissez le nombre de jeton qu'il faut alligner pour gagner :"))
    #iJoueurCommence = int(input("Choisissez le joueur qui commence :"))
    iNbColonne = 7
    iNbLigne = 6
    iNbJetonVictoire = 4
    iJoueurCommence = 1

    iTabPlateauDeJeu = [[0 for i in range(iNbLigne)] for i in range(iNbColonne)]
    sCouleurJetonJ1 = "yellow"
    sCouleurJetonJ2 = "red"
    bStatutCoupSpecialJ1 = True
    bStatutCoupSpecialJ2 = True


    tabStatutJeu = [[iTabPlateauDeJeu, bStatutCoupSpecialJ1, bStatutCoupSpecialJ2]]
    tabStatutJeu.append([iTabPlateauDeJeu, bStatutCoupSpecialJ1, bStatutCoupSpecialJ2])
    iJoueurCourant = iJoueurCommence
    boucleJeu = 0
    while boucleJeu < 10 :
        afficherPlateau(tabStatutJeu[boucleJeu][0], iNbColonne, iNbLigne)
        tabStatutJeu.append([placerJeton(tabStatutJeu[boucleJeu][0], iJoueurCourant, iNbColonne, iNbLigne), True, True])

        if iJoueurCourant == 1 :
            iJoueurCourant = 2
        else :
            iJoueurCourant = 1
        boucleJeu += 1
main()
