#!/usr/bin/python3
"""
    @file    interfaceJeu.py
    @brief   Contient les éléments de l'interface de jeu
    @author  Sylvain BRUNET & Matthieu CHARTON
    @version 0.2
    @date    2023-2024
"""

from fonctionGeneralInterface import *

###########################################################
#           FONCTIONS LIEES A L'AFFICHAGE                #
##########################################################

def creerPlateau(toplevelFenetre : tk.Toplevel, iHauteurChoisi : int, iLargeurChoisi : int):
    framePlateau = tk.Frame(toplevelFenetre)
    framePlateau.configure(height=50, width=350)
    framePlateau.place(anchor="nw", rely=0, relx=0)

        
        



"""
    @brief  Gère l'affichage de la page de jeu
"""
def gererInterfaceJeu(dictParametre : dict):
    toplevelInterfaceJeu = creerToplevelFenetre(768, 768, False, "Puissance N") 

    creerFrameHaut(toplevelInterfaceJeu)
    TplateauDeJeu: int & int = [[0 for i in range(dictParametre["hauteurPlateau"])] for i in range(dictParametre["largeurPlateau"])]
    TstatutJeu: int & int & int & int = [[TplateauDeJeu, 1, 1, 0]] # plateau, statut de l'atout du J1, statut de l'atout du J2, nombre de jeton dans la grille

    toplevelInterfaceJeu.mainloop()

dictTest  : dict = {"adversaire": True, "hauteurPlateau": 6,
                    "largeurPlateau": 7, "nombreJetonVicoire": 4,
                    "coupSpecial": True, "undoRedo": False}
gererInterfaceJeu(dictTest)