from affichage import *
from jeu import *
from verification import *
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

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

    tabStatutJeu = [[iTabPlateauDeJeu, True, True]]
    iJoueurCourant = iJoueurCommence
    iBoucleJeu = 0
    
    while iBoucleJeu < 10 :
        afficherPlateau(tabStatutJeu[iBoucleJeu][0], iNbColonne, iNbLigne)
        tabStatutJeu.append(tabStatutJeu[iBoucleJeu]) # Met les données du tour précédent dans le tour actuelle

        # Si le joueur courant a encore son coup spécial, lui demande si il veut l'utiliser
        
        if iBoucleJeu != 0 and tabStatutJeu[iBoucleJeu][iJoueurCourant] == True :
            bRetirerJeton = int(input("Saisissez si vous 0 souhaitez utiliser votre coup special sinon 1 :")) # 0 = oui, 1 = non
            if bRetirerJeton == 0 :
                tabStatutJeu[iBoucleJeu][0] = retirerJeton(tabStatutJeu[iBoucleJeu][0], iJoueurCourant, iNbColonne, iNbLigne)
                tabStatutJeu[iBoucleJeu][iJoueurCourant] = False # Enleve la posibilité d'utiliser l'atout du joueur qui l'a utilisé
            else :
                tabStatutJeu[iBoucleJeu][0] = placerJeton(tabStatutJeu[iBoucleJeu][0], iJoueurCourant, iNbColonne, iNbLigne)
        else :
            
            tabStatutJeu[iBoucleJeu][0] = placerJeton(tabStatutJeu[iBoucleJeu][0], iJoueurCourant, iNbColonne, iNbLigne)

        if iJoueurCourant == 1 :
            iJoueurCourant = 2
        else :
            iJoueurCourant = 1
        iBoucleJeu += 1
        cls()
main()
