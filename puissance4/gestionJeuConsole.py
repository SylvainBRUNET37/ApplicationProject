#!/usr/bin/python3
"""
    @file    gestionJeuConsole.py
    @brief   Contient la boucle principale pour le jeu en mode console
    @author  Matthieu CHARTON
    @version 1.0
    @date    2023-2024
"""

from jeu.affichage import *
from jeu.minMax import *

def main() -> None:
    """
        @brief Contient la boucle principale du jeu (en mode console) et l'initialisation des données
    """

    iNbColonne: int = 7
    iNbLigne: int = 6
    TplateauDeJeu: list = [[0 for i in range(iNbLigne)] for i in range(iNbColonne)]
    TstatutJeu: list = [[TplateauDeJeu, 1, 1, 0]] # plateau, statut de l'atout du J1, statut de l'atout du J2, nombre de jeton dans la grille
    iNbJetonVictoire: int = 4
    iJoueurCourant: int = 1
    iNbTour: int = 0
    bVictoire: bool = True
    while bVictoire :
        afficherPlateau(TstatutJeu[iNbTour][0], iNbColonne, iNbLigne)
        TstatutJeu.append(TstatutJeu[iNbTour]) # Met les données du tour précédent dans le tour actuelle

        # Si le joueur courant a encore son coup spécial, lui demande si il veut l'utiliser
        if TstatutJeu[iNbTour][3] != 0 and TstatutJeu[iNbTour][iJoueurCourant] != 0 and iJoueurCourant == 1:
            bAtout = int(input("Saisissez si vous 0 souhaitez utiliser votre coup special sinon 1 :")) # 0 = oui, 1 = non
            if bAtout == 0 :
                TstatutJeu[iNbTour][0] = inverserCouleur(TstatutJeu[iNbTour][0], iNbColonne, iNbLigne)
                TstatutJeu[iNbTour][iJoueurCourant] -= 1 # Retire une utilisation du coup spécial              
            else:
                # Place un jeton normalement et met à jour le plateau
                TstatutJeu[iNbTour][0] = placerJetonJoueur(TstatutJeu[iNbTour][0], iJoueurCourant, iNbColonne, iNbLigne)
                TstatutJeu[iNbTour][3] += 1
                # Vérifie s'il y a une victoire
                iVerif = verifierFinJeu(TstatutJeu[iNbTour][0], iNbColonne, iNbLigne, iNbJetonVictoire)
                if iVerif == 1 or iVerif == 2:
                    bVictoire = False
                    afficherPlateau(TstatutJeu[iNbTour][0], iNbColonne, iNbLigne)
                    print("\n GG Joueur ", iVerif, " tu as gagné !\n")
                elif iVerif == 3:
                    bVictoire = False
                    afficherPlateau(TstatutJeu[iNbTour][0], iNbColonne, iNbLigne)
                    print("\n Egalité dommage\n'")
        else:
            # Tour de l'IA ou du joueur 2
            if iJoueurCourant == 1:
                # Place un jeton normalement et met à jour le plateau
                TstatutJeu[iNbTour][0] = placerJetonJoueur(TstatutJeu[iNbTour][0], iJoueurCourant, iNbColonne, iNbLigne)
                TstatutJeu[iNbTour][3] += 1
            else:
                # L'IA détermine le meilleur coup et joue
                colonne_ia = trouverMeilleurCoup(TstatutJeu[iNbTour][0], iNbColonne, iNbLigne, iNbJetonVictoire, 4)
                placerJetonIA(TstatutJeu[iNbTour][0], colonne_ia, iJoueurCourant)

            # Vérifie s'il y a une victoire
            iVerif = verifierFinJeu(TstatutJeu[iNbTour][0], iNbColonne, iNbLigne, iNbJetonVictoire)
            if iVerif == 1 or iVerif == 2:
                bVictoire = False
                afficherPlateau(TstatutJeu[iNbTour][0], iNbColonne, iNbLigne)
                print("\n GG Joueur ", iVerif, " tu as gagné !\n")
            elif iVerif == 3:
                bVictoire = False
                afficherPlateau(TstatutJeu[iNbTour][0], iNbColonne, iNbLigne)
                print("\n Egalité dommage\n")

        # Passe au joueur suivant
        if iJoueurCourant == 1:
            iJoueurCourant = 2
        else:
            iJoueurCourant = 1
        iNbTour += 1

main()