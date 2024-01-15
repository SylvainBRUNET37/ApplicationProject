#!/usr/bin/python3
"""
    @file    interfaceJeu.py
    @brief   Contient les éléments de l'interface de jeu
    @author  Sylvain BRUNET & Matthieu CHARTON
    @version 0.2
    @date    2023-2024
"""

import copy
from interfaceGeneral import *
from jeu import identifierLigne
from verification import *

###########################################################
#                 VARIABLES GLOABALES                    #
##########################################################

iTourCourant: int = 0
iJoueurCourant: int = 1
iNbColonnePlateau: int = 7
iNbLignePlateau: int = 6
iNbJetonVictoire: int = 4
strCouleurJetonJ1: str = "yellow"
strCouleurJetonJ2: str = "red"
TstatutJeu: list = []
iCptUndo: int = 0
canvasFondPlateau: tk.Canvas = None

###########################################################
#           FONCTIONS LIEES AUX BOUTONS                  #
##########################################################

"""
    @brief  Reviens en arrière ou en avant dans la partie (dépendant de la valeur de iUndoRedo)
    @param  toplevelFenetre ou reafficher le plateau
    @param  iUndoRedo si True fait l'undo, si False fait le redo
"""
def gererUndoRedo(toplevelFenetre: tk.Toplevel, bUndoRedo: bool):
    global iTourCourant
    global iCptUndo

    # Si ce n'est pas le premier tour et que le joueur veut UNDO
    if (bUndoRedo == True and iTourCourant != 0):
        undoRedo(toplevelFenetre, 1)
    # Si ce n'est pas le dernier tour joué et que le joueur veut REDO
    elif (bUndoRedo == False and iTourCourant < iTourCourant+iCptUndo):
        undoRedo(toplevelFenetre, -1)


"""
    @brief  Reviens en arrière ou en avant dans la partie (dépendant de la valeur de iUndoRedo)
    @param  toplevelFenetre ou reafficher le plateau
    @param  iUndoRedo si 1 fait l'undo, si -1 fait le redo
"""
def undoRedo(toplevelFenetre: tk.Toplevel, iUndoRedo: int):
    global iTourCourant
    global iCptUndo
    global iJoueurCourant

    # Si UNDO, retire 1 au tour courant, si REDO ajoute 1 au tour courant (car iUndoRedo == -1)
    iTourCourant -= iUndoRedo
    # Si UNDO, ajoute 1 au nombre de undo, si REDO retire 1 au tour courant (car iUndoRedo == -1)
    iCptUndo += iUndoRedo
    
    # Change le joueur qui joue
    if (iJoueurCourant == 1):
        iJoueurCourant = 2
    else:
        iJoueurCourant = 1

    strCouleurJeton: str = "white"
    # Boucle autant de fois qu'il y a de case dans le plateau pour recréer chaque case
    for iLigne in range(iNbLignePlateau-1, -1, -1): # Part de la fin du plateau pour ne pas afficher le plateau à l'envers
        for iColonne in range(iNbColonnePlateau):

            # Si il n'y a pas de jeton, affiche une case vide
            if (TstatutJeu[iTourCourant][0][iColonne][iLigne] == 0):
                strCouleurJeton = "white"
            # Si c'est un jeton du joueur 1, affiche son jeton
            elif (TstatutJeu[iTourCourant][0][iColonne][iLigne] == 1):
                strCouleurJeton = strCouleurJetonJ1
            # Si c'est un jeton du joueur 2, affiche son jeton
            else:
                strCouleurJeton = strCouleurJetonJ2

            # Recréé et affiche les emplacements du plateau
            afficherJeton(iColonne, iLigne, strCouleurJeton)
        
"""
    @brief  Place le jeton dans la colonne choisi si elle n'est pas pleine
    @param  iColonneChoisi plateau de jeu dans lequel le jeton doit être placé
"""
def gererJeu(iColonneChoisi: int):
    global iTourCourant
    global iJoueurCourant
    global iNbLignePlateau
    global iNbColonnePlateau
    global iNbJetonVictoire
    global strCouleurJetonJ1
    global strCouleurJetonJ2
    global canvasFondPlateau
    global iCptUndo

    # Récupère la ligne où le jeton va tomber, ou "-1" si la colonne est pleine
    iLigneJouer: int = identifierLigne(TstatutJeu[iTourCourant][0][iColonneChoisi], iNbLignePlateau)

    # Si la colonne n'était pas pleine, place le jeton 
    if (iLigneJouer != -1):
        
        for i in range(iCptUndo):
            TstatutJeu.pop()

        # Passe au tour suivant et remet le compteur de undo à 0
        iCptUndo = 0
        iTourCourant += 1

        # Crée une copie du plateau de jeu actuel
        plateauCopie = [ligne.copy() for ligne in TstatutJeu[iTourCourant-1][0]]
        
        # Modifie le plateau de jeu copié
        plateauCopie[iColonneChoisi][iLigneJouer] = iJoueurCourant
        
        # Sauvegarde la copie dans TstatutJeu (pour l'undo/redo)
        TstatutJeu.append([plateauCopie, 0, 0])
        
        # Met la couleur du joueur courant à l'emplacement du jeton et passe le tour à l'autre joueur
        if (iJoueurCourant == 1):
            afficherJeton(iColonneChoisi, iLigneJouer, strCouleurJetonJ1)
            iJoueurCourant = 2
        else:
            afficherJeton(iColonneChoisi, iLigneJouer, strCouleurJetonJ2)
            iJoueurCourant = 1

        # Vérifie si un joueur a gagné
        bVerifGagner: bool = Verif(TstatutJeu[iTourCourant][0], iNbColonnePlateau, iNbLignePlateau, iNbJetonVictoire)
        
        # Affiche le message de victoire si un joueur a gagné
        if (bVerifGagner == 1):
            toplevelFenetrePrincipale = creerToplevelFenetre(300, 300, False, "GAGNEE")
            test = tk.Label(toplevelFenetrePrincipale, text="J1 GAGNE")
            test.pack()
        elif (bVerifGagner == 2):
            toplevelFenetrePrincipale = creerToplevelFenetre(300, 300, False, "GAGNEE")
            test = tk.Label(toplevelFenetrePrincipale, text="J2 GAGNE")
            test.pack()
        elif (bVerifGagner == 3):
            toplevelFenetrePrincipale = creerToplevelFenetre(300, 300, False, "GAGNEE")
            test = tk.Label(toplevelFenetrePrincipale, text="EGALITEE")
            test.pack()
            
        
###########################################################
#           FONCTIONS LIEES A L'AFFICHAGE                #
##########################################################

"""
    @brief  Place le jeton dans la colonne choisi si elle n'est pas pleine
    @param  iColonneChoisi plateau de jeu dans lequel le jeton doit être placé
"""
def creerBoutonUndoRedo(toplevelFenetre: tk.Toplevel):
    framUndoRedo: tk.Frame = tk.Frame(toplevelFenetre)
    framUndoRedo.place(relx=0.04, rely=0.83, width=125, height=125)
    
    # Créé le bouton undo
    buttonUndo : tk.Button = tk.Button(framUndoRedo)
    buttonUndo.configure(cursor="hand2", font="{Arial} 18", width=5, text='Undo', command= lambda: gererUndoRedo(toplevelFenetre, True))
    buttonUndo.place(anchor="nw", relx=0, rely=0)

    # Créé le bouton redo
    buttonRedo : tk.Button = tk.Button(framUndoRedo)
    buttonRedo.configure(cursor="hand2", font="{Arial} 18", width=5, text='Redo', command= lambda: gererUndoRedo(toplevelFenetre, False))
    buttonRedo.place(anchor="nw", relx=0, rely=0.5)

"""
    @brief  Affiche le jeton placé par le joueur
    @param  iColonneChoisi  colonne dans laquel le jeton doit être placé
    @param  iLigneJouer     ligne dans laquel le jeton doit être placé
    @param  strCouleurJeton couleur du jeton à placer
"""
def afficherJeton(iColonneChoisi: int, iLigneJouer: int, strCouleurJeton: str):
    global iNbLignePlateau
    global canvasFondPlateau

    # iX1 et iY1 définissent les coordonnées du coin supérieur gauche du rectangle et du oval
    iX1: int = iColonneChoisi * 60
    iY1: int = (iNbLignePlateau-iLigneJouer-1) * 60
    # iX2 et iY2 définissent les coordonnées du coin inférieur droit du rectangle et du oval
    iX2: int = iX1 + 60
    iY2: int = iY1 + 60

    # Créé un rectangle pour faire une case de la grille
    canvasFondPlateau.create_rectangle(iX1, iY1, iX2, iY2, outline="black", fill="blue")

    # Met la couleur du joueur courant à l'emplacement du jeton
    iCasePlateau : int = canvasFondPlateau.create_oval(iX1+5, iY1+5, iX2-5, iY2-5, fill=strCouleurJeton)
        
    # Relie la fonction qui permet de placer un pion au canva, elle s'activera quand le joueur cliquera sur une case
    # Passe à la fonction la numéro de la colonne de la case cliqué ainsi que le canva qui affiche le fond du plateau
    # pour pouvoir ensuite actualiser le couleur du jeton
    canvasFondPlateau.tag_bind(iCasePlateau, '<Button-1>', lambda event,
                        iColonneChoisi=iColonneChoisi: gererJeu(iColonneChoisi))

"""
    @brief Initilaise le plateau de jeu et l'affiche
    @param toplevelFenetre fenêtre où afficher le plateau de jeu
"""
def initialiserPlateau(toplevelFenetre: tk.Toplevel):
    global iNbColonnePlateau
    global iNbLignePlateau
    global canvasFondPlateau

    framePlateau = tk.Frame(toplevelFenetre)
    framePlateau.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=iNbColonnePlateau*60, height=iNbLignePlateau*60)
    
    # Créé et affiche le fond du plateau
    canvasFondPlateau = tk.Canvas(framePlateau, width=iNbColonnePlateau*60, height=iNbLignePlateau*60, background="blue", cursor="hand2")
    canvasFondPlateau.pack()

    # Boucle autant de fois qu'il y a de case dans le plateau pour créer chaque case
    for iLigne in range(iNbLignePlateau-1, -1, -1): # Part de la fin du plateau pour ne pas afficher le plateau à l'envers
        for iColonne in range(iNbColonnePlateau):
            # Créé et affiche les emplacements du plateau
            afficherJeton(iColonne, iLigne, "white")

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
    global TstatutJeu
    global iNbJetonVictoire

    strCouleurJetonJ1 = dictParametre["couleurJetonJ1"]
    strCouleurJetonJ2 = dictParametre["couleurJetonJ2"]
    iJoueurCourant = dictParametre["joueurCommence"]
    iNbColonnePlateau = dictParametre["nbColonnePlateau"]
    iNbLignePlateau = dictParametre["nbLignePlateau"]
    iNbJetonVictoire = dictParametre["nombreJetonVicoire"]

    TplateauDeJeu = []

    # Initialise la plateau avec des cases vides
    for iColonne in range(iNbColonnePlateau):
        TplateauDeJeu.append([])
        for iLigne in range(iNbLignePlateau):
            TplateauDeJeu[iColonne].append(0)

    # Liste qui contient : plateau de jeu, nombre d'atouts restant pour le J1, nombre d'atouts restant pour le J2, nombre de jeton dans la grille
    TstatutJeu.append([TplateauDeJeu, dictParametre["nombreCoupSpecial"], dictParametre["nombreCoupSpecial"]])

    initialiserPlateau(toplevelInterfaceJeu)
    creerBoutonUndoRedo(toplevelInterfaceJeu)

    toplevelInterfaceJeu.mainloop()


dictTest  : dict = {"adversaire": True, "nbLignePlateau": 6,
                    "nbColonnePlateau": 7, "nombreJetonVicoire": 4,
                    "coupSpecial": True, "undoRedo": False, "nombreCoupSpecial": 25, "joueurCommence": 2,
                    "couleurJetonJ1": "yellow", "couleurJetonJ2": "red"}
gererInterfaceJeu(dictTest)