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

"""
    @brief  Gère l'affichage et l'initialisation du plateau de jeu
    @param dictParametre contient les paramètres déjà choisis par le joueur
    @return le plateau de jeu initialisé à 0
"""
def creerPlateau(toplevelFenetre: tk.Toplevel, iHauteurChoisi: int, iLargeurChoisi: int) -> list:
    framePlateau = tk.Frame(toplevelFenetre)
    framePlateau.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=iLargeurChoisi*60, height=iHauteurChoisi*60)

    # Créé le plateau de jeu
    TplateauDeJeu = [[0 for iBoucleI in range(iLargeurChoisi)] for iBoucleJ in range(iHauteurChoisi)]

    # Créé le fond du plateau
    canva = tk.Canvas(framePlateau, width=iLargeurChoisi*60, height=iHauteurChoisi*60, background="blue", cursor="hand2")
    canva.pack()

    # Boucle autant de fois qu'il y a de case dans le plateau pour créer chaque case graphiquement
    for iBoucleI in range(iHauteurChoisi):
        for iBoucleJ in range(iLargeurChoisi):
            x1, y1 = iBoucleJ * 60, iBoucleI * 60
            x2, y2 = x1 + 60, y1 + 60
            # Créé un rectangle pour faire une case de la grille
            canva.create_rectangle(x1, y1, x2, y2, outline="black", fill="blue")
            # Créé le cercle qui sert a afficher les emplacement pour les jetons dans les cases de la grille
            canva.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="white")

    return TplateauDeJeu
        



"""
    @brief  Gère l'affichage de la page de jeu
    @param dictParametre contient les paramètres déjà choisis par le joueur
"""
def gererInterfaceJeu(dictParametre : dict):
    toplevelInterfaceJeu = creerToplevelFenetre(768, 768, False, "Puissance N") 
    creerFrameHaut(toplevelInterfaceJeu)
    
    # plateau de jeu, nombre d'atouts restant pour le J1, nombre d'atouts restant pour le J2, nombre de jeton dans la grille
    TstatutJeu: int & int & int & int = [[creerPlateau(toplevelInterfaceJeu, dictParametre["hauteurPlateau"], dictParametre["largeurPlateau"]), 
                                          dictParametre["nombreJetonVicoire"], dictParametre["nombreJetonVicoire"], 0]] 

    toplevelInterfaceJeu.mainloop()

dictTest  : dict = {"adversaire": True, "hauteurPlateau": 6,
                    "largeurPlateau": 7, "nombreJetonVicoire": 4,
                    "coupSpecial": True, "undoRedo": False}
gererInterfaceJeu(dictTest)