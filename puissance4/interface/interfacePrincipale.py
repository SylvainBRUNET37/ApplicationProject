#!/usr/bin/python3
"""
    @file    interfacePrincipale.py
    @brief   Contient les éléments de l'interface principale et les fonctions pour gérer celle-ci
    @author  Sylvain BRUNET
    @version 1.0
    @date    2023-2024
"""

import tkinter as tk

###########################################################
'                 VARIABLES GLOABALES                     '
###########################################################

toplevelFenetrePrincipale: tk.Tk = None # Fenêtre principale

iNbLignePlateau : int = 6
iNbColonnePlateau : int = 7
iNbJetonVictoire : int = 4
bStateCoupSpecial : bool = True
bStateUndoRedo : bool = True

###########################################################
'                        GETERS                           '
###########################################################

def getNbLigne() -> int:
    """
        @brief Renvoie le nombre de ligne du plateau choisi par le joueur
        @return le nombre de ligne du plateau choisi par le joueur
    """

    global iNbLignePlateau
    return iNbLignePlateau

def getNbColonne() -> int: 
    """
        @brief Renvoie le nombre de colonne du plateau choisi par le joueur
        @return le nombre de colonne du plateau choisi par le joueur
    """

    global iNbColonnePlateau
    return iNbColonnePlateau

def getNbJetonVictoire() -> int:
    """
        @brief Renvoie le nombre de jeton à alligner pour gagner
        @return le nombre de jeton à alligner pour gagner
    """

    global iNbJetonVictoire
    return iNbJetonVictoire

def getStateCoupSpecial() -> bool:
    """
        @brief Renvoie le booléen qui défini si le coup spécial sera activé (True activé, False pas activé)
        @return le booléen qui défini si le coup spécial sera activé (True activé, False pas activé)
    """

    global bStateCoupSpecial
    return bStateCoupSpecial

def getStateUndoRedo() -> bool:
    """
        @brief Renvoie le booléen qui défini si l'UNDO/REDO sera activé (True activé, False pas activé)
        @return le booléen qui défini si l'UNDO/REDO sera activé (True activé, False pas activé)
    """

    global bStateUndoRedo
    return bStateUndoRedo

###########################################################
'           FONCTIONS LIEES AUX BOUTONS                   '
###########################################################

def updateNbLignePlateau(iNbLigneChoisi: int) -> None:
    """
        @brief Met à jour la variable global qui défini le nombre de ligne du plateau
        @param iNbLigneChoisi variable tkinter qui contient le nombre de ligne du plateau
    """
        
    global iNbLignePlateau
    iNbLignePlateau = int(iNbLigneChoisi)

def updateNbColonnePlateau(iNbColonneChoisi: int) -> None:        
    """
        @brief Met à jour la variable global qui défini le nombre de colonne du plateau
        @param iNbColonneChoisi variable tkinter qui contient le nombre de colonne du plateau
    """

    global iNbColonnePlateau
    iNbColonnePlateau = int(iNbColonneChoisi)

def updateNbJetonVicoire(iNbJetonVictoireChoisi: int) -> None:
    """
        @brief Met à jour la variable global qui défini le nombre de jeton à alligner pour gagner
        @param iNbJetonVictoireChoisi variable tkinter qui contient le nombre de jeton à alligner pour gagner
    """

    global iNbJetonVictoire
    iNbJetonVictoire = int(iNbJetonVictoireChoisi)

def updateCoupSpecial(bCoupSpecialChoisi: bool) -> None:
    """
        @brief Met à jour la variable global qui défini si le coup spécial est activé en fonction de l'état de son checkbutton associé
        @param bCoupSpecialChoisi variable tkinter qui contient l'état du checkbutton coup spécial
    """

    global bStateCoupSpecial
    bStateCoupSpecial = bCoupSpecialChoisi

def updateUndoRedo(bUndoRedoChoisi: bool) -> None:
    """
        @brief Met à jour la variable global qui défini si l'undo redo est activé en fonction de l'état de son checkbutton associé
        @param bUndoRedoChoisi variable tkinter qui contient l'état du checkbutton undo/redo
    """

    global bStateUndoRedo
    bStateUndoRedo = bUndoRedoChoisi

###########################################################
'             FONCTIONS LIEES A AFFICHAGE                 '
###########################################################

def creerFrameNbLigne() -> None:
    """
        @brief Créé le widget permettant de choisir la nombre de ligne du plateau
    """

    global toplevelFenetrePrincipale
    global iNbLignePlateau

    # Créé la variable tkinter liée au slider et l'initialise à 6
    iTkNbLignePlateau: tk.IntVar = tk.IntVar()
    iTkNbLignePlateau.set(iNbLignePlateau)

    frameNbLigne: tk.Frame = tk.Frame(toplevelFenetrePrincipale)
    frameNbLigne.configure(height=150, width=400)
    frameNbLigne.place(anchor="nw", rely=0.55, x=10, y=5)

    # Créé et configure le slider
    scaleNbLigne: tk.Scale = tk.Scale(frameNbLigne)
    scaleNbLigne.configure(cursor="sb_h_double_arrow", from_=5, orient="horizontal", relief="flat", to=8, length=200, width=20,
                            variable=iTkNbLignePlateau, command = updateNbLignePlateau)
    scaleNbLigne.place(anchor="nw", relx=0.2, rely=0.0, x=0, y=0)

    labelNbLigne: tk.Label = tk.Label(frameNbLigne)
    labelNbLigne.configure(text='Nombre de ligne du plateau', font=20)
    labelNbLigne.place(anchor="nw", relx=0.20, rely=0.4, x=0, y=0)

def creerFrameNbColonne() -> None:
    """
        @brief  Créé le widget permettant de choisir le nombre de colonne du plateau
    """

    global toplevelFenetrePrincipale
    global iNbColonnePlateau

    # Créé la variable tkinter liée au slider et l'initialise à 7
    iTkNbColonnePlateau: tk.IntVar = tk.IntVar()
    iTkNbColonnePlateau.set(iNbColonnePlateau)

    frameNbColonne: tk.Frame = tk.Frame(toplevelFenetrePrincipale)
    frameNbColonne.configure(height=150, width=400)
    frameNbColonne.place(anchor="nw", relx=0.5, rely=0.55, x=10, y=5)

    # Créé et configure le slider
    scaleNbColonne: tk.Scale = tk.Scale(frameNbColonne)
    scaleNbColonne.configure(cursor="sb_h_double_arrow", from_=5, orient="horizontal", relief="flat", to=10, length=200, width=20,
                             variable=iTkNbColonnePlateau, command = updateNbColonnePlateau)
    scaleNbColonne.place(anchor="nw", relx=0.18, rely=0, x=0, y=0)

    labelNbColonne: tk.Label = tk.Label(frameNbColonne)
    labelNbColonne.configure(text='Nombre de colonne du plateau', font=20)
    labelNbColonne.place(anchor="nw", relx=0.18, rely=0.4, x=0, y=0) 

def creerFrameNombreJetonVictoire() -> None:
    """
        @brief  Créé le widget permettant de choisir le nombre de jeton à alligner pour gagner
    """

    global toplevelFenetrePrincipale
    global iNbJetonVictoire

    # Créé la variable tkinter liée au slider et l'initialise à 4
    iTkNbJetonVictoire: tk.IntVar = tk.IntVar()
    iTkNbJetonVictoire.set(iNbJetonVictoire)

    frameNombreJetonVictoire: tk.Frame = tk.Frame(toplevelFenetrePrincipale)
    frameNombreJetonVictoire.configure(height=150, width=400)
    frameNombreJetonVictoire.place(anchor="nw", relx=0.0, rely=0.75, x=10, y=5)

    # Créé et configure le slider
    scaleNombreJetonVictoire: tk.Scale = tk.Scale(frameNombreJetonVictoire)
    scaleNombreJetonVictoire.configure(cursor="sb_h_double_arrow", from_=3, orient="horizontal", relief="flat", to=5, length=200, width=20, 
                                       variable=iTkNbJetonVictoire, command = updateNbJetonVicoire)
    scaleNombreJetonVictoire.place(anchor="nw", relx=0.2, rely=0.0, x=0, y=0)

    labelNombreJetonVictoire: tk.Label = tk.Label(frameNombreJetonVictoire)
    labelNombreJetonVictoire.configure(text='Nombre de jeton à alligner', font=20)
    labelNombreJetonVictoire.place(anchor="nw", relx=0.18, rely=0.37, x=0, y=0)
     
def creerFrameCheckButton() -> None:
    """
        @brief Créé les checkbutton pour l'activation/désactivation de l'UNDO/REDO et du coup spécial
    """

    global toplevelFenetrePrincipale
    global bStateCoupSpecial
    global bStateUndoRedo

    # Créé les variables tkinter liées aux checkbuttons
    bTkUndoRedo: tk.BooleanVar = tk.BooleanVar()
    bTkCoupSpecial: tk.BooleanVar = tk.BooleanVar()
    bTkUndoRedo.set(bStateUndoRedo)
    bTkCoupSpecial.set(bStateCoupSpecial)

    frameCheckButton: tk.Frame = tk.Frame(toplevelFenetrePrincipale)
    frameCheckButton.configure(height=150, width=400)
    frameCheckButton.place(anchor="nw", relx=0.5, rely=0.75, x=10, y=5)

    # Créé et configure le bouton lié à l'activation/désactivation du coup spécial
    checkbuttonCoupSpecial: tk.Checkbutton = tk.Checkbutton(frameCheckButton)
    checkbuttonCoupSpecial.configure(cursor="hand2", text='Coup special', font=14, variable=bTkCoupSpecial, command = lambda:updateCoupSpecial(bTkCoupSpecial.get()))
    checkbuttonCoupSpecial.place(anchor="nw", relx=0.2, rely=0.1, x=0, y=0)

    # Créé et configure le bouton lié à l'activation/désactivation de l'UNDO/REDO
    checkbuttonUndoRedo: tk.Checkbutton = tk.Checkbutton(frameCheckButton)
    checkbuttonUndoRedo.configure(cursor="hand2", text='Undo / Redo', font=14, variable=bTkUndoRedo, command = lambda:updateUndoRedo(bTkUndoRedo.get()))
    checkbuttonUndoRedo.place(anchor="nw", relx=0.2, rely=0.35, x=0, y=0)


###########################################################
'                 GESTION DE LA FENETRE                   '
###########################################################

def gererInterfacePrincipale(toplevelFenetre: tk.Tk) -> None:
    """
        @brief Gère l'affichage de la page principale
        @param toplevelFenetre Fenêtre principale
    """

    global toplevelFenetrePrincipale

    toplevelFenetrePrincipale = toplevelFenetre

    # Créé tous les widgets qui permettent de changer les paramètres
    creerFrameNbLigne()
    creerFrameNbColonne()
    creerFrameNombreJetonVictoire()
    creerFrameCheckButton()

    # Affiche la page créée
    toplevelFenetrePrincipale.mainloop()
