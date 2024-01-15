#!/usr/bin/python3
"""
    @file    interfaceJeu.py
    @brief   Contient les éléments de l'interface de jeu
    @author  Sylvain BRUNET & Matthieu CHARTON
    @version 0.2
    @date    2023-2024
"""

from interfaceGeneral import *
from jeu import identifierLigne
from verification import *

###########################################################
#                 VARIABLES GLOABALES                    #
##########################################################

iTourCourant: int = 1
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
    @brief  Reviens en arrière dans la partie
    @param  toplevelFenetre fenêtre
"""
def undo(toplevelFenetre: tk.Toplevel):
    return None
        
"""
    @brief  Place le jeton dans la colonne choisi si elle n'est pas pleine
    @param  iColonneChoisi plateau de jeu dans lequel le jeton doit être placé
    @param  canvasFondPlateau     plateau de jeu dans lequel le jeton doit être placé
"""
def gererJeu(iColonneChoisi: int, canvasFondPlateau: tk.Canvas):
    global TplateauDeJeu
    global iTourCourant
    global iJoueurCourant
    global iNbLignePlateau
    global iNbColonnePlateau
    global iNbJetonVictoire
    global strCouleurJetonJ1
    global strCouleurJetonJ2

    # Récupère la ligne où le jeton va tomber, ou "-1" si la colonne est pleine
    iLigneJouer: int = identifierLigne(TplateauDeJeu[iColonneChoisi], iNbLignePlateau)

    # Si la colonne n'était pas pleine, place le jeton 
    if (iLigneJouer != -1):
        # Place le jeton dans le tableau de jeu 
        TplateauDeJeu[iColonneChoisi][iLigneJouer] = iJoueurCourant

        # Met la couleur du joueur courant à l'emplacement du jeton et passe le tour à l'autre joueur
        if (iJoueurCourant == 1):
            afficherJeton(canvasFondPlateau, iColonneChoisi, iLigneJouer, strCouleurJetonJ1)
            iJoueurCourant = 2
        else:
            afficherJeton(canvasFondPlateau, iColonneChoisi, iLigneJouer, strCouleurJetonJ2)
            iJoueurCourant = 1

        # Copie le plateau acutel pour le sauvegarder sinon le plateau est acutalisé à chaque fois que la variable global change
        plateauCopie = [ligne.copy() for ligne in TplateauDeJeu]
        # Sauvegarde le tour actuel pour le undo/redo 
        # (plateau de jeu / nombre de coup spécial restant J1 / nombre de coup spécial restant J2 / nombre de pions dans la grille)
        TstatutJeu[iTourCourant][0] = plateauCopie
        
        # Vérifie si un joueur a gagné
        bVerifGagner: bool = Verif(TplateauDeJeu, iNbColonnePlateau, iNbLignePlateau, iNbJetonVictoire)
        
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
        # Si aucun joueur n'a gagné, passe au tour suivant
        else:
            TstatutJeu.append(TstatutJeu[iTourCourant])
            iTourCourant += 1
            
        
###########################################################
#           FONCTIONS LIEES A L'AFFICHAGE                #
##########################################################

"""
    @brief  Place le jeton dans la colonne choisi si elle n'est pas pleine
    @param  iColonneChoisi plateau de jeu dans lequel le jeton doit être placé
    @param  canvasFondPlateau     plateau de jeu dans lequel le jeton doit être placé
"""
def creerBoutonUndoRedo(toplevelFenetre: tk.Toplevel):
    framUndoRedo: tk.Frame = tk.Frame(toplevelFenetre)
    framUndoRedo.place(relx=0.04, rely=0.83, width=125, height=125)
    
    # Créé le bouton undo
    buttonUndo : tk.Button = tk.Button(framUndoRedo)
    buttonUndo.configure(cursor="hand2", font="{Arial} 18", width=5, text='Undo', command= lambda: undo(toplevelFenetre))
    buttonUndo.place(anchor="nw", relx=0, rely=0)

    # Créé le bouton redo
    buttonRedo : tk.Button = tk.Button(framUndoRedo)
    buttonRedo.configure(cursor="hand2", font="{Arial} 18", width=5, text='Redo', state="disabled")
    buttonRedo.place(anchor="nw", relx=0, rely=0.5)

"""
    @brief  Affiche le jeton placé par le joueur
    @param  canvasFondPlateau      fond du plateau de jeu (pour pouvoir afficher le jeton dedans)
    @param  iColonneChoisi  colonne dans laquel le jeton doit être placé
    @param  iLigneJouer     ligne dans laquel le jeton doit être placé
    @param  strCouleurJeton couleur du jeton à placer
"""
def afficherJeton(canvasFondPlateau: tk.Canvas, iColonneChoisi: int, iLigneJouer: int, strCouleurJeton: str):
    global iNbLignePlateau

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
                        iColonneChoisi=iColonneChoisi, canvasFondPlateau=canvasFondPlateau: gererJeu(iColonneChoisi, canvasFondPlateau))

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
    for iLigne in range(iNbLignePlateau-1, -1, -1): # Part de la fin du plateau pour ne pas afficher le plateau à l'envers
        for iColonne in range(iNbColonnePlateau):
            # Créé et affiche les emplacements du plateau
            afficherJeton(canvasFondPlateau, iColonne, iLigne, "white")

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
    global iNbJetonVictoire

    strCouleurJetonJ1 = dictParametre["couleurJetonJ1"]
    strCouleurJetonJ2 = dictParametre["couleurJetonJ2"]
    iJoueurCourant = dictParametre["joueurCommence"]
    iNbColonnePlateau = dictParametre["nbColonnePlateau"]
    iNbLignePlateau = dictParametre["nbLignePlateau"]
    iNbJetonVictoire = dictParametre["nombreJetonVicoire"]

    # Initialise la plateau avec des cases vides
    for iColonne in range(iNbColonnePlateau):
        TplateauDeJeu.append([])
        for iLigne in range(iNbLignePlateau):
            TplateauDeJeu[iColonne].append(0)

    plateauCopie = [ligne.copy() for ligne in TplateauDeJeu]

    # Liste qui contient : plateau de jeu, nombre d'atouts restant pour le J1, nombre d'atouts restant pour le J2, nombre de jeton dans la grille
    TstatutJeu.append([plateauCopie, dictParametre["nombreCoupSpecial"], dictParametre["nombreCoupSpecial"], 0])
    TstatutJeu.append([plateauCopie, dictParametre["nombreCoupSpecial"], dictParametre["nombreCoupSpecial"], 0])

    initialiserPlateau(toplevelInterfaceJeu)
    creerBoutonUndoRedo(toplevelInterfaceJeu)

    toplevelInterfaceJeu.mainloop()






dictTest  : dict = {"adversaire": True, "nbLignePlateau": 8,
                    "nbColonnePlateau": 10, "nombreJetonVicoire": 4,
                    "coupSpecial": True, "undoRedo": False, "nombreCoupSpecial": 25, "joueurCommence": 1,
                    "couleurJetonJ1": "yellow", "couleurJetonJ2": "red"}
gererInterfaceJeu(dictTest)