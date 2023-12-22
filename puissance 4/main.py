from affichage import *
from jeu import *
from verification import *
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    iNbColonne = 7
    iNbLigne = 6
    iTabPlateauDeJeu = [[0 for i in range(iNbLigne)] for i in range(iNbColonne)]
    tabStatutJeu = [[iTabPlateauDeJeu, True, True, 0]] # plateau, statut de l'atout du J1, statut de l'atout du J2, nombre de jeton dans la grille
    
    iJoueurCourant = 1
    iBoucleJeu = 0
    while iBoucleJeu < 10 :
        afficherPlateau(tabStatutJeu[iBoucleJeu][0], iNbColonne, iNbLigne)
        tabStatutJeu.append(tabStatutJeu[iBoucleJeu]) # Met les données du tour précédent dans le tour actuelle

        # Si le joueur courant a encore son coup spécial, lui demande si il veut l'utiliser
        if tabStatutJeu[iBoucleJeu][3] != 0 and tabStatutJeu[iBoucleJeu][iJoueurCourant] == True :
            bRetirerJeton = int(input("Saisissez si vous 0 souhaitez utiliser votre coup special sinon 1 :")) # 0 = oui, 1 = non
            if bRetirerJeton == 0 :
                tabStatutJeu[iBoucleJeu][0] = retirerJeton(tabStatutJeu[iBoucleJeu][0], iNbColonne, iNbLigne)
                tabStatutJeu[iBoucleJeu][iJoueurCourant] = False # Enleve la posibilité d'utiliser l'atout du joueur qui l'a utilisé
                tabStatutJeu[iBoucleJeu][3] -= 1
            else :
                tabStatutJeu[iBoucleJeu][0] = placerJeton(tabStatutJeu[iBoucleJeu][0], iJoueurCourant, iNbColonne, iNbLigne)
                tabStatutJeu[iBoucleJeu][3] += 1
        else :
            tabStatutJeu[iBoucleJeu][0] = placerJeton(tabStatutJeu[iBoucleJeu][0], iJoueurCourant, iNbColonne, iNbLigne)
            tabStatutJeu[iBoucleJeu][3] += 1

        if iJoueurCourant == 1 :
            iJoueurCourant = 2
        else :
            iJoueurCourant = 1
        iBoucleJeu += 1
        cls()
main()
