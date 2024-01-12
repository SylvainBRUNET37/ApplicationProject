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
iNbJetonVictoire: int = 4
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
    @return "-1" si la colonne est pleine, l'indice de la ligne où le jeton doit être posé si ce n'est pas le cas
"""
def identifierLigne(iTabColonne: list) -> int:
    global iNbLignePlateau

    iBoucleLigne: int = 0
    bCaseVideTrouve: bool = False

    # Parcours la colonne de bas en haut et s'arrête
    while (iBoucleLigne != iNbLignePlateau and bCaseVideTrouve != True):
        # Si une case vide est trouvée, renvoie met fin à la boucle
        if iTabColonne[iBoucleLigne] == 0 :
            bCaseVideTrouve = True
        iBoucleLigne += 1

    # Si une case vide a été trouvée, renvoie l'indice le ligne de celle-ci
    if (bCaseVideTrouve == True):
        return iBoucleLigne-1 # -1 car la variable est ittéré avant de sortir de la boucle
    # Sinon, la colonne est pleine et renvoie donc -1
    else:
        return -1

"""
    @brief  Demande au joueur la colonne où il veut placer son jeton puis le place
    @param  iColonneChoisi plateau de jeu dans lequel le jeton doit être placé
    @param  canvasFond     plateau de jeu dans lequel le jeton doit être placé
"""
def placerJeton(iColonneChoisi: int, canvasFond: tk.Canvas):
    global iJoueurCourant
    global strCouleurJetonJ1
    global strCouleurJetonJ2

    # Récupère la ligne où le jeton va tomber, ou "-1" si la colonne est pleine
    iLigneJouer: int = identifierLigne(TplateauDeJeu[iColonneChoisi])

    # Si la colonne n'était pas pleine, place le jeton 
    if (iLigneJouer != -1):
        # Place le jeton dans le tableau de jeu
        TplateauDeJeu[iColonneChoisi][iLigneJouer] = iJoueurCourant

        # iX1 et iY1 définissent les coordonnées du coin supérieur gauche du rectangle et du oval
        iX1: int = iColonneChoisi * 60
        iY1: int = (iNbLignePlateau-iLigneJouer-1) * 60
        # iX2 et iY2 définissent les coordonnées du coin inférieur droit du rectangle et du oval
        iX2: int = iX1 + 60
        iY2: int = iY1 + 60

        # Met la couleur du joueur courant à l'emplacement du jeton
        if (iJoueurCourant == 1):
            iCasePlateau : int = canvasFond.create_oval(iX1+5, iY1+5, iX2-5, iY2-5, fill=strCouleurJetonJ1)
            iJoueurCourant = 2
        else:
            iCasePlateau : int = canvasFond.create_oval(iX1+5, iY1+5, iX2-5, iY2-5, fill=strCouleurJetonJ2)
            iJoueurCourant = 1
        
        # Relie la fonction qui permet de placer un pion au canva, elle s'activera quand le joueur cliquera sur une case
        # Passe à la fonction la numéro de la colonne de la case cliqué ainsi que le canva qui affiche le fond du plateau
        # pour pouvoir ensuite actualiser le couleur du jeton
        canvasFond.tag_bind(iCasePlateau, '<Button-1>', lambda event,
                                   iColonneChoisi=iColonneChoisi, canvasFond=canvasFond: placerJeton(iColonneChoisi, canvasFond))
        
###########################################################
#           FONCTIONS LIEES A L'AFFICHAGE                #
##########################################################

"""
    @brief Initilaise le plateau de jeu et l'affiche
    @param toplevelFenetre fenêtre où afficher le plateau de jeu
"""
def initialiserPlateau(toplevelFenetre: tk.Toplevel):
    global iNbColonnePlateau
    global iNbLignePlateau

    framePlateau = tk.Frame(toplevelFenetre)
    framePlateau.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=iNbColonnePlateau*60, height=iNbLignePlateau*60)
    
    # Créé et affiche le fond du plateau
    canvasFondPlateau : tk.Canvas = tk.Canvas(framePlateau, width=iNbColonnePlateau*60, height=iNbLignePlateau*60, background="blue", cursor="hand2")
    canvasFondPlateau.pack()

    # Boucle autant de fois qu'il y a de case dans le plateau pour créer chaque case
    for iBoucleI in range(iNbLignePlateau-1, -1, -1): # Part de la fin du plateau pour ne pas afficher le plateau à l'envers
        for iBoucleJ in range(iNbColonnePlateau):
            # iX1 et iY1 définissent les coordonnées du coin supérieur gauche du rectangle et du oval
            iX1: int = iBoucleJ * 60
            iY1: int = (iNbLignePlateau-iBoucleI-1) * 60
            # iX2 et iY2 définissent les coordonnées du coin inférieur droit du rectangle et du oval
            iX2: int = iX1 + 60
            iY2: int = iY1 + 60
            
            # Créé un rectangle pour faire une case de la grille
            canvasFondPlateau.create_rectangle(iX1, iY1, iX2, iY2, outline="black", fill="blue")

            # Créé le cercle pour l'emplacement du jeton (les trous de la grille)
            iCasePlateau : int = canvasFondPlateau.create_oval(iX1+5, iY1+5, iX2-5, iY2-5, fill="white")

            # Lie la fonction qui permet de placer un pion au canva, elle s'activera quand le joueur cliquera sur une case
            # Passe à la fonction la numéro de la colonne de la case cliqué ainsi que le canva qui affiche le fond du plateau
            # pour pouvoir ensuite actualiser le couleur du jeton
            canvasFondPlateau.tag_bind(iCasePlateau, '<Button-1>', lambda event,
                                       iColonneChoisi=iBoucleJ, canvasFond=canvasFondPlateau: placerJeton(iColonneChoisi, canvasFond))

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
    global strCouleurJeton
    global TplateauDeJeu
    global TstatutJeu
    global iNbJetonVictoire

    strCouleurJetonJ1 = dictParametre["couleurJetonJ1"]
    strCouleurJetonJ2 = dictParametre["couleurJetonJ2"]
    iJoueurCourant = dictParametre["joueurCommence"]
    iNbColonnePlateau = dictParametre["nbColonnePlateau"]
    iNbLignePlateau = dictParametre["nbLignePlateau"]
    iNbJetonVictoire = dictParametre["nombreJetonVicoire"]

    # Initialise la plateau avec des cases vides
    for iBoucleI in range(iNbColonnePlateau):
        TplateauDeJeu.append([])
        for iBoucleJ in range(iNbLignePlateau):
            TplateauDeJeu[iBoucleI].append(0)

    # Liste qui contient : plateau de jeu, nombre d'atouts restant pour le J1, nombre d'atouts restant pour le J2, nombre de jeton dans la grille
    TstatutJeu.append([TplateauDeJeu, dictParametre["nombreCoupSpecial"], dictParametre["nombreCoupSpecial"], 0])

    initialiserPlateau(toplevelInterfaceJeu)

    toplevelInterfaceJeu.mainloop()






dictTest  : dict = {"adversaire": True, "nbLignePlateau": 6,
                    "nbColonnePlateau": 7, "nombreJetonVicoire": 4,
                    "coupSpecial": True, "undoRedo": False, "nombreCoupSpecial": 3, "joueurCommence": 1,
                    "couleurJetonJ1": "yellow", "couleurJetonJ2": "red"}
gererInterfaceJeu(dictTest)