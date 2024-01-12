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
#                 VARIABLES GLOABALES                    #
##########################################################

iJoueurCourant: int = 1
iNbColonnePlateau: int = 7
iNbLignePlateau: int = 6
strCouleurJetonJ1: str = "yellow"
strCouleurJetonJ2: str = "red"
TplateauDeJeu : list = []
TstatutJeu: list = []

###########################################################
#           FONCTIONS LIEES AUX BOUTONS                  #
##########################################################

"""
    @brief  Identifie la ligne où devra être posé le jeton à partir de la colonne que le joueur a choisi
    @param  iTabColonne colonne où le joueur veut placer son jeton
    @param  iNbLigne    nombre de ligne du plateau de jeu
    @return 'None' si la colonne est pleine, l'indice de la ligne où le jeton doit être posé si ce n'est pas le cas
"""
def identifierColonneChoisi(iTabColonne: list) -> int:
    global iNbLignePlateau
    # Parcours la colonne de bas en haut
    for iBoucleL in range(iNbLignePlateau) :
        # Si une ligne vide est trouvée, renvoie son indice
        if iTabColonne[iBoucleL] == 0 :
            return iBoucleL
    return None

"""
    @brief  Demande au joueur la colonne où il veut placer son jeton puis le place
    @param  iTabPlateauJeu plateau de jeu dans lequel le jeton doit être placé
    @param  iJoueur        joueur qui veut placer le jeton
    @param  iNbColonne     nombre de colonne du plateau de jeu
    @param  iNbLigne       nombre de ligne du plateau de jeu
"""
def placerJeton(iColonneChoisi: int, test: int):
    global iNbLignePlateau
    global TplateauDeJeu
    bColonneValide: bool = True
    print(iColonneChoisi)
    print(test)
    while bColonneValide == True :
        # Si l'indice de colonne saisi correspond bien a une ligne bien dans le plateau, verifie si la colonne associée est pleine
        iLigneJouer = identifierColonneChoisi(TplateauDeJeu[iColonneChoisi])
        # Si la colonne n'est pas pleine, sort de la boucle (sinon, repart au début)
        if iLigneJouer != None :
            bColonneValide = False

    TplateauDeJeu[iColonneChoisi][iLigneJouer] = iJoueurCourant
        
###########################################################
#           FONCTIONS LIEES A L'AFFICHAGE                #
##########################################################

"""
    @brief  Gère l'affichage du plateau de jeu
    @param dictParametre contient les paramètres déjà choisis par le joueur
    @return le plateau de jeu initialisé à 0
"""
def afficherPlateau(toplevelFenetre: tk.Toplevel) -> list:
    framePlateau = tk.Frame(toplevelFenetre)
    framePlateau.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=iNbColonnePlateau*60, height=iNbLignePlateau*60)
    
    # Créé le fond du plateau
    canvaFondPlateau : tk.Canvas = tk.Canvas(framePlateau, width=iNbColonnePlateau*60, height=iNbLignePlateau*60, background="blue", cursor="hand2")
    canvaFondPlateau.pack()

    global strCouleurJetonJ1
    global strCouleurJetonJ2
    strCouleur:str = "white"
    # Boucle autant de fois qu'il y a de case dans le plateau pour créer chaque case graphiquement
    for iBoucleI in range(iNbLignePlateau-1, -1, -1):
        for iBoucleJ in range(iNbColonnePlateau):
            # Si il n'y a pas de jeton dans la case, défini la couleur du jeton à afficher à blanc
            if(TplateauDeJeu[iBoucleJ][iBoucleI] == 0):
                strCouleur = "white"
            # Si il n'y a pas de jeton dans la case, défini la couleur du jeton à celle du joueur 1
            elif(TplateauDeJeu[iBoucleJ][iBoucleI] == 1):
                strCouleur = strCouleurJetonJ1
            # Sinon, défini la couleur du jeton à afficher à celle du joueur 2
            else:
                strCouleur = strCouleurJetonJ2

            # Défini les coordonnées où placer la case
            x1, y1 = iBoucleJ * 60, (iNbLignePlateau - 1 - iBoucleI) * 60
            x2, y2 = x1 + 60, y1 + 60
            
            # Créé un rectangle pour faire une case de la grille
            canvaFondPlateau.create_rectangle(x1, y1, x2, y2, outline="black", fill="blue")
            # Créé le cercle qui sert a afficher les emplacement pour les jetons dans les cases de la grille
            iCasePlateau : int = canvaFondPlateau.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=strCouleur)
            # Lorsque le joueur cliquera sur une case, la position de la case sera envoyé à la fonction pour placer le pion
            canvaFondPlateau.tag_bind(iCasePlateau, '<Button-1>', lambda event,
                                       iColonneChoisi=iBoucleJ, test=iBoucleI: placerJeton(iColonneChoisi, test))

"""
    @brief  Gère l'affichage de la page de jeu
    @param dictParametre contient les paramètres déjà choisis par le joueur
"""
def gererInterfaceJeu(dictParametre: dict):
    toplevelInterfaceJeu = creerToplevelFenetre(768, 768, False, "Puissance N") 
    creerFrameHaut(toplevelInterfaceJeu)

    global iJoueurCourant
    global iNbColonnePlateau
    global iNbLignePlateau
    global strCouleurJetonJ1
    global strCouleurJetonJ2
    global TplateauDeJeu
    global TstatutJeu

    strCouleurJetonJ1 = dictParametre["couleurJetonJ1"]
    strCouleurJetonJ2 = dictParametre["couleurJetonJ2"]
    iJoueurCourant = dictParametre["joueurCommence"]
    iNbColonnePlateau = dictParametre["nbColonnePlateau"]
    iNbLignePlateau = dictParametre["nbLignePlateau"]

    # Initialise la plateau avec des cases vides
    for iBoucleI in range(iNbColonnePlateau):
        TplateauDeJeu.append([])
        for iBoucleJ in range(iNbLignePlateau):
            TplateauDeJeu[iBoucleI].append(0)

    TplateauDeJeu[0][0] = 1
    # Liste qui contient : plateau de jeu, nombre d'atouts restant pour le J1, nombre d'atouts restant pour le J2, nombre de jeton dans la grille
    TstatutJeu.append([TplateauDeJeu, dictParametre["nombreCoupSpecial"], dictParametre["nombreCoupSpecial"], 0])

    print(TplateauDeJeu)

    afficherPlateau(toplevelInterfaceJeu)

    toplevelInterfaceJeu.mainloop()






dictTest  : dict = {"adversaire": True, "nbLignePlateau": 6,
                    "nbColonnePlateau": 7, "nombreJetonVicoire": 4,
                    "coupSpecial": True, "undoRedo": False, "nombreCoupSpecial": 3, "joueurCommence": 1,
                    "couleurJetonJ1": "yellow", "couleurJetonJ2": "red"}
gererInterfaceJeu(dictTest)