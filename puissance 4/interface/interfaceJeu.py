#!/usr/bin/python3
"""
    @file    interfaceJeu.py
    @brief   Contient les éléments de l'interface de jeu et les fonctions pour gérer celle-ci
    @author  Sylvain BRUNET & Matthieu CHARTON
    @version 1.0
    @date    2023-2024
"""

import tkinter as tk

import copy
from jeu import *
from interfaceGeneral import creerToplevelFenetre

###########################################################
#                  VARIABLES GLOABALES                    #
###########################################################

canvasFondPlateau: tk.Canvas = None # Fond du plateau de jeu
toplevelFenetreJeu: tk.Tk = None # Fenêtre de jeu

iNbColonnePlateau: int = 0
iNbLignePlateau: int = 0
iNbJetonVictoire: int = 0 # Nombre de jeton à alligner pour gagner
strCouleurJetonJ1: str = ""
strCouleurJetonJ2: str = ""
iDifficulteIA: int = 0 # 0 si en JvsJ, 1 pour niveau 1, 2 pour niveau 2 et 4 pour niveau 3 (correspond à la profondeur de l'algorithme)
bStateUndoRedo: bool = False # False si l'UNDO/REDO est désactivé, True si activé

bFinJeu: bool = False # Indique si la partie est terminée ou non
iTourCourant: int = 0 # Tour en cours
iJoueurCourant: int = 0 # Joueur qui joue pour le tour en cours
iCptUndo: int = 0 # Nombre de fois que le joueur à utilisé le bouton UNDO avant d'avoir rejoué
TstatutJeu: list = [] # Contient le statut du jeu pour chaque tour (pour le UNDO/REDO) :
                      # le plateau de jeu et le nombre de coup spécial restant de chaque joueur pour chaque tour

###########################################################
#             FONCTIONS LIEES AUX BOUTONS                 #
###########################################################

"""
    @brief  Lance la fonction UNDO ou REDO (dépend de la valeur de bUndoOrRedo) et met à jour les boutons liés à cette fonction 
    @param  bUndoOrRedo si True fait l'UNDO, si False fait le REDO
"""
def gererUndoRedo(bUndoOrRedo: bool):
    global iTourCourant
    global iCptUndo
    global iJoueurCourant

    # Si c'est du joueur vs IA, ajoute un poid qui doublera le nombre de tours où revenir en arrière/avant
    if (iDifficulteIA == 0):
        intStateJvsIA: int = 1
    else:
        intStateJvsIA: int = 2

    # Si le joueur à cliqué sur UNDO, reviens au tour d'avant, incrémente le nombre de UNDO utilisé d'affilé et met à jour le plateau
    if (bUndoOrRedo == True):
        iTourCourant -= 1 * intStateJvsIA
        iCptUndo += 1 * intStateJvsIA
        updateAffichagePlateau()
    # Si le joueur à cliqué sur REDO, reviens au tour d'après, décrémente le nombre de UNDO utilisé d'affilé et met à jour le plateau
    elif (bUndoOrRedo == False):
        iTourCourant += 1 * intStateJvsIA
        iCptUndo -= 1 * intStateJvsIA
        updateAffichagePlateau()

    # Met à jour le joueur qui doit jouer
    if (iJoueurCourant == 1 and iDifficulteIA == 0):
        iJoueurCourant = 2
    else:
        iJoueurCourant = 1

    # Met à jour les boutons
    creerBoutonUndoRedo()
    afficherInfoJeu()
    creerBoutonCoupSpecial()

"""
    @brief Met à jour le plateau en mettant les bons jetons aux bons endroits
"""
def updateAffichagePlateau():
    # Supprime toutes les cases du plateau
    canvasFondPlateau.delete("all")

    strCouleurJeton: str = "white"
    # Boucle autant de fois qu'il y a de case dans le plateau pour mettre à jour chaque case
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

            # Affiche un emplacement du plateau
            afficherJeton(iColonne, iLigne, strCouleurJeton)
        
"""
    @brief  Gère le jeu : place le jeton, gère la sauvegarde des statuts de jeu...
    @param  iColonneChoisi colonne dans laquel le jeton doit être placé (colonne sur laquel le joueur a cliqué)
"""
def gererJeu(iColonneChoisi: int):
    global iTourCourant
    global iJoueurCourant
    global iNbLignePlateau
    global iNbColonnePlateau
    global iNbJetonVictoire
    global bFinJeu

    bCoupJouer: bool = False
    # Si la partie n'est pas terminée, fait jouer le joueur courant
    if (bFinJeu == False):
        # Si iColonneChoisi est NULL, joue le coup spécial
        if (iColonneChoisi == None):
            bCoupJouer = jouerCoupSpecial()
        # Sinon, place le pion dans la colonne choisi
        else: 
            bCoupJouer = placerJeton(iColonneChoisi)
        
        # Si le coup/l'atout a bien été joué, met à jour le jeu et l'affichage
        if (bCoupJouer == True):

            # Met à jour le joueur qui doit jouer
            if (iJoueurCourant == 1):
                iJoueurCourant = 2
            else:
                iJoueurCourant = 1
                
            # Met à jour l'affichage du plateau et actualise les boutons
            updateAffichagePlateau()
            creerBoutonUndoRedo()
            afficherInfoJeu()
            creerBoutonCoupSpecial()

            # Vérifie si c'est la fin du jeu (plateau plein ou joueur qui gagne) et affiche l'écran de fin de partie
            afficherFinJeu(Verif(TstatutJeu[iTourCourant][0], iNbColonnePlateau, iNbLignePlateau, iNbJetonVictoire))

            # Si le mode de jeu est JvsIA et que c'est au tour de l'IA,
            # relance la fonction en donnant en paramètre le coup qu'elle estime être le meilleur pour gagner
            if (iDifficulteIA != 0 and iJoueurCourant == 2):
                gererJeu(meilleur_coup(TstatutJeu[iTourCourant][0], iNbColonnePlateau, iNbLignePlateau, iNbJetonVictoire, iDifficulteIA))

"""
    @brief  Place le jeton dans la colonne choisi par le joueur
    @return False si la colonne est pleine, True si le jeton a été joué
"""
def placerJeton(iColonneChoisi: int) -> bool:
    global iCptUndo
    global iTourCourant
    global TstatutJeu

    # Récupère la ligne où le jeton va tomber, ou "-1" si la colonne est pleine. Si c'est -1, renvoie False
    iLigneJouer: int = identifierLigne(TstatutJeu[iTourCourant][0][iColonneChoisi], iNbLignePlateau)
    if (iLigneJouer == -1):
        return False
    # Sinon, place le pion
    else:
        # Supprime les plateaux sauvegardés après le tour jouer 
        # En supprime autant que de fois où le joueur a utilisé le bouton UNDO
        for iBoucle in range(iCptUndo):
            TstatutJeu.pop()

        # Passe au tour suivant et remet à 0 le compteur d'UNDO
        iTourCourant += 1
        iCptUndo = 0

        # Crée une copie du plateau de jeu actuel
        test: list = copy.deepcopy(TstatutJeu[iTourCourant-1])
        test[0]: list = [ligne.copy() for ligne in TstatutJeu[iTourCourant-1][0]]
            
        # Ajoute le jeton joué à la copie
        test[0][iColonneChoisi][iLigneJouer] = iJoueurCourant
            
        # Sauvegarde la copie
        TstatutJeu.append(test)
        
        return True

"""
    @brief  Joue le coup spécial
    @return False si le coup spécial ne peut pas être joué, True si il a été joué
"""
def jouerCoupSpecial() -> bool:
    global iCptUndo
    global iTourCourant
    global TstatutJeu
    global iNbColonnePlateau
    global iNbLignePlateau

    # Si c'est la fin du jeu, que le joueur n'a plus de coup spécial ou que c'est le premier tour, renvoie False
    if (bFinJeu == True or TstatutJeu[iTourCourant][iJoueurCourant] == 0 or iTourCourant == 0):
        return False
    # Sinon joue le coup spécial
    else:
        # Supprime les plateaux sauvegardés après le tour jouer 
        # En supprime autant que de fois où le joueur a utilisé le bouton UNDO
        for iBoucle in range(iCptUndo):
            TstatutJeu.pop()
    
        # Passe au tour suivant et remet à 0 le compteur d'UNDO
        iTourCourant += 1
        iCptUndo = 0
            
        # Crée une copie du plateau de jeu actuel
        test: list = copy.deepcopy(TstatutJeu[iTourCourant-1])
        test[0]: list = [ligne.copy() for ligne in TstatutJeu[iTourCourant-1][0]]
        test[iJoueurCourant] = (TstatutJeu[iTourCourant-1][iJoueurCourant])-1
        
        # Met le nouveau plateau dans la copie
        test[0] = atout(test[0], iNbColonnePlateau, iNbLignePlateau)

        # Sauvegarde la copie
        TstatutJeu.append(test)

        return True
       
###########################################################
#            FONCTIONS LIEES A L'AFFICHAGE                #
###########################################################

"""
    @brief Affiche le joueur qui doit jouer, le numéro du tour et le nombre de coup spécial de chaque joueur
"""
def afficherInfoJeu():
    global iTourCourant
    global TstatutJeu
    global iJoueurCourant
    
    if (iJoueurCourant == 1):
        strCouleur:str = strCouleurJetonJ1
    else:
        strCouleur: str = strCouleurJetonJ2

    frameInfoJeu: tk.Frame = tk.Frame(toplevelFenetreJeu)
    frameInfoJeu.place(relx=0.2, rely=0.83, width=400, height=200)

    labelTour: tk.Label = tk.Label(frameInfoJeu, text="Tour numéro :", font="{Helvetica} 16 {underline}")
    labelTour.place(anchor="nw", relx=0, rely=0)
    labelTourCourant: tk.Label = tk.Label(frameInfoJeu, text=str(iTourCourant+1), font="{Helvetica} 12")
    labelTourCourant.place(anchor="nw", relx=0.385, rely=0.025)

    labelTourJoueur: tk.Label = tk.Label(frameInfoJeu, text="Tour du joueur :", font="{Helvetica} 16 {underline}")
    labelTourJoueur.place(anchor="nw", relx=0, rely=0.2)
    canvaCouleur: tk.Canvas = tk.Canvas(frameInfoJeu)
    canvaCouleur.configure(height=75, width=75)
    canvaCouleur.create_oval(33, 33, 5, 5, outline="black", fill=strCouleur)
    canvaCouleur.place(anchor="nw", relx=0.4, rely=0.185)

    labelCoupSpecial: tk.Label = tk.Label(frameInfoJeu, text="Nombre de coup spécial :", font="{Helvetica} 16 {underline}")
    labelCoupSpecial.place(anchor="nw", relx=0, rely=0.4)
    labelCoupSpecialJ1: tk.Label = tk.Label(frameInfoJeu, text="J1 : "+str(TstatutJeu[iTourCourant][1]), font="{Helvetica} 12")
    labelCoupSpecialJ1.place(anchor="nw", relx=0.62, rely=0.425)
    labelCoupSpecialJ2: tk.Label = tk.Label(frameInfoJeu, text="J2 : "+str(TstatutJeu[iTourCourant][2]), font="{Helvetica} 12")
    labelCoupSpecialJ2.place(anchor="nw", relx=0.76, rely=0.425)


"""
    @brief Créé et affiche le bouton qui permet d'utiliser le coup spécial
"""
def creerBoutonCoupSpecial():
    global iTourCourant
    global iJoueurCourant
    global TstatutJeu
    global bFinJeu

    strStateBouton: str = ""
    # Si le joueur n'a plus de coup spécial, désactive le bouton
    if (TstatutJeu[iTourCourant][iJoueurCourant] == 0 or bFinJeu == True):
        strStateBouton = "disabled"
    else:
        strStateBouton = "active"

    frameBoutonCoupSpecial: tk.Frame = tk.Frame(toplevelFenetreJeu)
    frameBoutonCoupSpecial.place(relx=0.67, rely=0.85, width=300, height=125)

    # Créé le bouton UNDO et le lie à la fonction qui gère l'UNDO/REDO
    buttonCoupSpecial: tk.Button = tk.Button(frameBoutonCoupSpecial)
    buttonCoupSpecial.configure(cursor="hand2", font="{Arial} 18", width=15, text='Changer la couleur\n des pions', state=strStateBouton,
                                command= lambda: gererJeu(None))
    buttonCoupSpecial.place(anchor="nw", relx=0, rely=0)

"""
    @brief Affiche l'écran de fin de partie
    @param bVerifGagner 0 si ce n'est pas la fin de la partie, 1 si J1 a gagné, 2 si J2 a gagné 3 si plateau plein
"""
def afficherFinJeu(bVerifGagner: bool):
    global bFinJeu

    # Si c'est la fin de la partie
    if (bVerifGagner != 0):
        bFinJeu = True
        # Met à jour les boutons
        creerBoutonCoupSpecial()
        # Affiche la fenêtre de victoire du joueur 2
        if (bVerifGagner == 1):
            toplevelFenetreJeu = creerToplevelFenetre(300, 200, False, "Victoire J1")
            labelVictoireJ1: tk.Label = tk.Label(toplevelFenetreJeu, text="Le joueur 1 a gagné !", font=("Helvetica", 16))
            labelVictoireJ1.pack(pady=60)
        # Affiche la fenêtre de victoire du joueur 2
        elif (bVerifGagner == 2):
            toplevelFenetreJeu = creerToplevelFenetre(300, 300, False, "Victoire J2")
            labelVictoireJ2: tk.Label = tk.Label(toplevelFenetreJeu, text="Le joueur 2 a gagné !", font=("Helvetica", 16))
            labelVictoireJ2.pack(pady=60)
        # Affiche la fenêtre d'égalité
        elif (bVerifGagner == 3):
            toplevelFenetreJeu = creerToplevelFenetre(300, 300, False, "Égalité")
            labelEgalite: tk.Label = tk.Label(toplevelFenetreJeu, text="Égalité !", font=("Helvetica", 16))
            labelEgalite.pack(pady=60)

"""
    @brief Créé les boutons d'UNDO/REDO
"""
def creerBoutonUndoRedo():
    global iCptUndo
    global iTourCourant
    global toplevelFenetreJeu
    global iDifficulteIA
    global iJoueurCourant

    frameUndoRedo: tk.Frame = tk.Frame(toplevelFenetreJeu)
    frameUndoRedo.place(relx=0.04, rely=0.83, width=125, height=125)

    strStateUndo: str = ""
    strStateRedo: str = ""
    # Si le joueur à désactivé l'undo/redo, bloque les boutons liés à cette fonction (sinon active/désactive les boutons)
    if (bStateUndoRedo == False):
        strStateUndo = "disabled"
        strStateRedo = "disabled"
    else:
        # Si c'est le premier tour, bloque le bouton UNDO (sinon l'active)
        # Si l'IA joue en premier, le premier tour du joueur est le 1. Dans ce cas désactive aussi l'UNDO
        if (iTourCourant == 0 or (iTourCourant == 1 and iDifficulteIA != 0)):
            strStateUndo = "disabled"
        else:
            strStateUndo = "active"

        # Si l'UNDO n'a pas été utilisé, bloque le bouton de REDO (sinon l'active)
        if (iCptUndo == 0):
            strStateRedo = "disabled"
        else:
            strStateRedo = "active"

    # Créé le bouton UNDO et le lie à la fonction qui gère l'UNDO/REDO
    buttonUndo: tk.Button = tk.Button(frameUndoRedo)
    buttonUndo.configure(cursor="hand2", font="{Arial} 18", width=5, text='Undo', state=strStateUndo,
                         command= lambda: gererUndoRedo(True))
    buttonUndo.place(anchor="nw", relx=0, rely=0)

    # Créé le bouton REDO et le lie à la fonction qui gère l'UNDO/REDO
    buttonRedo: tk.Button = tk.Button(frameUndoRedo)
    buttonRedo.configure(cursor="hand2", font="{Arial} 18", width=5, text='Redo', state=strStateRedo,
                         command= lambda: gererUndoRedo(False))
    buttonRedo.place(anchor="nw", relx=0, rely=0.5)

"""
    @brief  Affiche un jeton de couleur donnée à la position donnée
    @param  iColonneChoisi  colonne dans laquel le jeton doit être placé
    @param  iLigneJouer     ligne dans laquel le jeton doit être placé
    @param  strCouleurJeton couleur du jeton à placer
"""
def afficherJeton(iColonneChoisi: int, iLigneJouer: int, strCouleurJeton: str):
    global iNbLignePlateau
    global canvasFondPlateau
    global toplevelFenetreJeu

    # iX1 et iY1 définissent les coordonnées du coin supérieur gauche du rectangle et du oval
    iX1: int = iColonneChoisi * 60
    iY1: int = (iNbLignePlateau-iLigneJouer-1) * 60
    # iX2 et iY2 définissent les coordonnées du coin inférieur droit du rectangle et du oval
    iX2: int = iX1 + 60
    iY2: int = iY1 + 60

    # Créé la case de la grille (carré de fond bleu)
    canvasFondPlateau.create_rectangle(iX1, iY1, iX2, iY2, outline="black", fill="blue")

    # Met la couleur du joueur à l'emplacement du jeton (dans le trou de la grille)
    iCasePlateau : int = canvasFondPlateau.create_oval(iX1+5, iY1+5, iX2-5, iY2-5, fill=strCouleurJeton)
        
    # Relie la fonction qui gère le jeu au canva, elle s'activera quand le joueur cliquera sur une case
    # Passe à la fonction la numéro de la colonne de la case cliqué
    canvasFondPlateau.tag_bind(iCasePlateau, '<Button-1>', lambda event,
                        iColonneChoisi=iColonneChoisi: gererJeu(iColonneChoisi))

"""
    @brief Initialise et affiche le plateau de jeu
"""
def initialiserPlateau():
    global iNbColonnePlateau
    global iNbLignePlateau
    global canvasFondPlateau
    global toplevelFenetreJeu

    framePlateau = tk.Frame(toplevelFenetreJeu)
    framePlateau.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=iNbColonnePlateau*60, height=iNbLignePlateau*60)
    
    # Créé et affiche le fond du plateau
    canvasFondPlateau = tk.Canvas(framePlateau, width=iNbColonnePlateau*60, height=iNbLignePlateau*60, background="blue", cursor="hand2")
    canvasFondPlateau.pack()

    # Affiche le plateau
    updateAffichagePlateau()

###########################################################
#                 GESTION DE LA FENETRE                   #
###########################################################

"""
    @brief Gère l'initialisation des variables globales
    @param dictParametre contient les paramètres choisis par le joueur
"""
def initVarGlobal(dictParametre: dict):
    global toplevelFenetreJeu
    global iJoueurCourant
    global iNbColonnePlateau
    global iNbLignePlateau
    global strCouleurJetonJ1
    global strCouleurJetonJ2
    global iNbJetonVictoire
    global iDifficulteIA
    global bStateUndoRedo
    
    global TstatutJeu
    global bFinJeu
    global iTourCourant
    global iCptUndo
    global TstatutJeu

    # Met les paramèteres chosis par l'utilisateur dans des variables globales
    strCouleurJetonJ1 = dictParametre["couleurJetonJ1"]
    strCouleurJetonJ2 = dictParametre["couleurJetonJ2"]
    iJoueurCourant = dictParametre["joueurCommence"]
    iNbColonnePlateau = dictParametre["nbColonnePlateau"]
    iNbLignePlateau = dictParametre["nbLignePlateau"]
    iNbJetonVictoire = dictParametre["nombreJetonVicoire"]
    iDifficulteIA = dictParametre["difficulteIA"]
    bStateUndoRedo = dictParametre["stateUndoRedo"]

    # Réinitialise les variables globales pour que le jeu se relance bien quand le joueur reviens de la page de paramètre
    TstatutJeu = []
    bFinJeu = False
    iTourCourant = 0
    iCptUndo = 0

    TplateauDeJeu: list = []
    # Initialise la plateau avec des 0
    for iColonne in range(iNbColonnePlateau):
        TplateauDeJeu.append([])
        for iLigne in range(iNbLignePlateau):
            TplateauDeJeu[iColonne].append(0)

    # Sauvegarde l'état du jeu du premier tour
    # Contient : plateau de jeu, nombre d'atouts restant pour le J1, nombre d'atouts restant pour le J2
    TstatutJeu.append([TplateauDeJeu, dictParametre["nombreCoupSpecial"], dictParametre["nombreCoupSpecial"]])

"""
    @brief Gère l'affichage de la page de jeu
    @param toplevelFenetre Fenêtre de jeu
    @param dictParametre contient les paramètres choisis par le joueur
"""
def gererInterfaceJeu(toplevelFenetre: tk.Tk, dictParametre: dict):
    global iDifficulteIA
    global iJoueurCourant

    toplevelFenetreJeu = toplevelFenetre

    # Initialise les variables globales
    initVarGlobal(dictParametre)

    # Créé les widgets qui permettent de jouer
    initialiserPlateau()
    creerBoutonUndoRedo()
    afficherInfoJeu()
    creerBoutonCoupSpecial()

    # Si c'est l'IA qui joue le premier tour, joue son tour
    if (iDifficulteIA != 0 and iJoueurCourant == 2):
        gererJeu(meilleur_coup(TstatutJeu[iTourCourant][0], iNbColonnePlateau, iNbLignePlateau, iNbJetonVictoire, iDifficulteIA))

    # Affiche la page créée
    toplevelFenetreJeu.mainloop()