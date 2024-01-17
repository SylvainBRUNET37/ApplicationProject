#!/usr/bin/python3
"""
    @file    interfaceJeu.py
    @brief   Contient les éléments de l'interface de jeu et les fonctions pour gérer celui-ci
    @author  Sylvain BRUNET
    @version 0.3
    @date    2023-2024
"""

from interfaceGeneral import *
from jeu import *

###########################################################
#                 VARIABLES GLOABALES                    #
##########################################################

canvasFondPlateau: tk.Canvas = None # Fond du plateau de jeu
toplevelFenetreJeu: tk.Toplevel = None # Fenêtre de jeu

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
#           FONCTIONS LIEES AUX BOUTONS                  #
##########################################################

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

    # Met à jour les boutons d'UNDO/REDO
    creerBoutonUndoRedo()

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
    global strCouleurJetonJ1
    global strCouleurJetonJ2
    global iCptUndo
    global bFinJeu

    # Si la partie n'est pas terminée, autorise le joueur à jouer
    if (bFinJeu == False):
        # Récupère la ligne où le jeton va tomber, ou "-1" si la colonne est pleine
        iLigneJouer: int = identifierLigne(TstatutJeu[iTourCourant][0][iColonneChoisi], iNbLignePlateau)

        # Si la colonne n'était pas pleine, 
        if (iLigneJouer != -1):
            
            # Supprime autant de plateau sauvegarder que de fois où le joueur à utilisé l'UNDO 
            for i in range(iCptUndo):
                TstatutJeu.pop()

            # Passe au tour suivant et remet le compteur de UNDO à 0
            iCptUndo = 0
            iTourCourant += 1
            
            # Actualise les boutons UNDO et REDO
            creerBoutonUndoRedo()

            # Crée une copie du plateau de jeu actuel
            TplateauCopie: list = [ligne.copy() for ligne in TstatutJeu[iTourCourant-1][0]]
            
            # Ajoute le jeton joué à la copie
            TplateauCopie[iColonneChoisi][iLigneJouer] = iJoueurCourant
            
            # Sauvegarde la copie
            TstatutJeu.append([TplateauCopie, 0, 0])
            
            # Affiche le jeton et met à jour le joueur qui doit jouer
            if (iJoueurCourant == 1):
                afficherJeton(iColonneChoisi, iLigneJouer, strCouleurJetonJ1)
                iJoueurCourant = 2
            else:
                afficherJeton(iColonneChoisi, iLigneJouer, strCouleurJetonJ2)
                iJoueurCourant = 1

            # Vérifie si c'est la fin du jeu (plateau plein ou joueur qui gagne) et affiche l'écran de fin de partie
            afficherFinJeu(Verif(TstatutJeu[iTourCourant][0], iNbColonnePlateau, iNbLignePlateau, iNbJetonVictoire))

            # Si le mode de jeu est JvsIA et que c'est au tour de l'IA,
            # relance la fonction en donnant en paramètre le coup qu'elle estime être le meilleur pour gagner
            if (iDifficulteIA != 0 and iJoueurCourant == 2):
                gererJeu(meilleur_coup(TstatutJeu[iTourCourant][0], iNbColonnePlateau, iNbLignePlateau, iNbJetonVictoire, iDifficulteIA))

           
###########################################################
#           FONCTIONS LIEES A L'AFFICHAGE                #
##########################################################

"""
    @brief Affiche l'écran de fin de partie
    @param bVerifGagner 0 si ce n'est pas la fin de la partie, 1 si J1 a gagné, 2 si J2 a gagné 3 si plateau plein
"""
def afficherFinJeu(bVerifGagner: bool):
    global bFinJeu

    # Si c'est la fin de la partie
    if (bVerifGagner != 0):
        bFinJeu = True
        # Affiche la fenêtre de victoire du joueur 2
        if (bVerifGagner == 1):
            toplevelFenetreJeu = creerToplevelFenetre(300, 300, False, "GAGNEE")
            test = tk.Label(toplevelFenetreJeu, text="J1 GAGNE")
            test.pack()
        # Affiche la fenêtre de victoire du joueur 2
        elif (bVerifGagner == 2):
            toplevelFenetreJeu = creerToplevelFenetre(300, 300, False, "GAGNEE")
            test = tk.Label(toplevelFenetreJeu, text="J2 GAGNE")
            test.pack()
        # Affiche la fenêtre d'égalité
        elif (bVerifGagner == 3):
            toplevelFenetreJeu = creerToplevelFenetre(300, 300, False, "GAGNEE")
            test = tk.Label(toplevelFenetreJeu, text="EGALITEE")
            test.pack()

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

"""
    @brief Gère l'affichage de la page de jeu
    @param dictParametre contient les paramètres choisis par le joueur
"""
def gererInterfaceJeu(dictParametre: dict):
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

    # Créé la fenêtre et le haut de la fenêtre
    toplevelFenetreJeu = creerToplevelFenetre(768, 768, False, "Puissance N") 
    creerFrameHaut(toplevelFenetreJeu)

    # Met les paramèteres chosis par l'utilisateur dans des variables globales
    strCouleurJetonJ1 = dictParametre["couleurJetonJ1"]
    strCouleurJetonJ2 = dictParametre["couleurJetonJ2"]
    iJoueurCourant = dictParametre["joueurCommence"]
    iNbColonnePlateau = dictParametre["nbColonnePlateau"]
    iNbLignePlateau = dictParametre["nbLignePlateau"]
    iNbJetonVictoire = dictParametre["nombreJetonVicoire"]
    iDifficulteIA = dictParametre["difficulteIA"]
    bStateUndoRedo = dictParametre["stateUndoRedo"]

    TplateauDeJeu: list = []
    # Initialise la plateau avec des cases vides
    for iColonne in range(iNbColonnePlateau):
        TplateauDeJeu.append([])
        for iLigne in range(iNbLignePlateau):
            TplateauDeJeu[iColonne].append(0)

    # Sauvegarde l'état du jeu du premier tour
    # Contient : plateau de jeu, nombre d'atouts restant pour le J1, nombre d'atouts restant pour le J2
    TstatutJeu.append([TplateauDeJeu, dictParametre["nombreCoupSpecial"], dictParametre["nombreCoupSpecial"]])

    initialiserPlateau()
    creerBoutonUndoRedo()

    # Si c'est l'IA qui joue le premier tour, joue son tour
    if (iDifficulteIA != 0 and iJoueurCourant == 2):
        gererJeu(meilleur_coup(TstatutJeu[iTourCourant][0], iNbColonnePlateau, iNbLignePlateau, iNbJetonVictoire, iDifficulteIA))

    # Affiche la page créée
    toplevelFenetreJeu.mainloop()


dictTest  : dict = {"adversaire": True, "nbLignePlateau": 6,
                    "nbColonnePlateau": 7, "nombreJetonVicoire": 4,
                    "stateCoupSpecial": True, "nombreCoupSpecial": 25, "joueurCommence": 1,
                    "couleurJetonJ1": "yellow", "couleurJetonJ2": "red", "difficulteIA": 1, "stateUndoRedo": True}
gererInterfaceJeu(dictTest)