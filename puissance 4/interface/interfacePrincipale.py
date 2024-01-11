#!/usr/bin/python3
"""
    @file    interfacePrincipale.py
    @brief   Contient l'interface qui permet au joueur de lancer la partie
    @author  Sylvain BRUNET & Matthieu CHARTON
    @version 0.2
    @date    2023-2024
"""

from fonctionGeneralInterface import *
from interfaceParametre import gestionPageParametre

###########################################################
#                 VARIABLES GLOABALES                    #
##########################################################

bAdversaire : bool = True # False pour joueur contre joueur, True pour joueur contre IA
iHauteurPlateau : int = 6
iLargeurPlateau : int = 7
iNbJetonVictoire : int = 4
bCoupSpecial : bool = True
bUndoRedo : bool = True

###########################################################
#           FONCTIONS LIEES AUX BOUTONS                  #
##########################################################

"""
    @brief Met à jour la variable global qui défini l'adversaire (True pour IA, False pour joueur) et lance la fenêtre de paramètre
    @param bTkAdversaire variable tkinter qui contient qui est l'adversaire
    @param bAdversaireChoisi adversaire choisi par l'utilisateur (True pour IA, False pour joueur)
"""
def lancerPartie(toplevelFenetre : tk.Toplevel, bAdversaireChoisi : bool):
    global bAdversaire
    global iHauteurPlateau
    global iLargeurPlateau
    global iNbJetonVictoire
    global bCoupSpecial
    global bUndoRedo
    bAdversaire = bAdversaireChoisi
    dictParametres : dict = {"adversaire": bAdversaire, "hauteurPlateau": iHauteurPlateau,
                             "largeurPlateau": iLargeurPlateau, "nombreJetonVicoire": iNbJetonVictoire,
                             "coupSpecial": bCoupSpecial, "undoRedo": bUndoRedo}
    
    toplevelFenetre.destroy() # Ferme la fenêtre pricipale
    gestionPageParametre(dictParametres) # Lance la fenêtre de paramètere en donnant les paramètres déjà choisis

"""
    @brief Met à jour la variable global qui défini la hauteur du plateau
    @param iHauteurChoisi variable tkinter qui contient la hauteur du plateau
"""
def updateHauteurPlateau(iHauteurChoisi : int):
    global iHauteurPlateau
    iHauteurPlateau = iHauteurChoisi

"""
    @brief Met à jour la variable global qui défini la lageur du plateau
    @param iLargeurChoisi variable tkinter qui contient la lageur du plateau
"""
def updateLargeurPlateau(iLargeurChoisi : int):
    global iLargeurPlateau
    iLargeurPlateau = iLargeurChoisi

"""
    @brief Met à jour la variable global qui défini le nombre de jeton à alligner pour gagner
    @param iNbJetonVictoireChoisi variable tkinter qui contient le nombre de jeton à alligner pour gagner
"""
def updateNbJetonVicoire(iNbJetonVictoireChoisi : int):
    global iNbJetonVictoire
    iNbJetonVictoire = iNbJetonVictoireChoisi

"""
    @brief Met à jour la variable global qui défini si le coup spécial est activé en fonction de l'état de son checkbutton associé
    @param bCoupSpecialChoisi variable tkinter qui contient l'état du checkbutton coup spécial
"""
def updateCoupSpecial(bCoupSpecialChoisi : bool):
    global bCoupSpecial
    bCoupSpecial = bCoupSpecialChoisi

"""
    @brief Met à jour la variable global qui défini si l'undo redo est activé en fonction de l'état de son checkbutton associé
    @param bUndoRedoChoisi variable tkinter qui contient l'état du checkbutton undo/redo
"""
def updateUndoRedo(bUndoRedoChoisi : bool):
    global bUndoRedo
    bUndoRedo = bUndoRedoChoisi

###########################################################
#           FONCTIONS LIEES A L'AFFICHAGE                #
##########################################################

"""
    @brief  Créé les boutons pour le choix d'aversaire (Joueur vs IA / Joueur vs Joueur)
    @param  toplevelFenetre la fenêtre où placer les boutons
"""
def creerFrameChoixAdversaire(toplevelFenetre : tk.Toplevel):
    frameChoixAdversaire = tk.Frame(toplevelFenetre)
    frameChoixAdversaire.configure(height=200, width=750)
    frameChoixAdversaire.place(anchor="nw", rely=0.23, x=10, y=5)

    buttonJvsIA = tk.Button(frameChoixAdversaire)
    buttonJvsIA.configure(cursor="hand2", font="{Arial} 32 {}", text='Joueur \nVS \nIA', width=8, command=lambda: lancerPartie(toplevelFenetre, True))
    buttonJvsIA.place(anchor="nw", relx=0.6, rely=0.0, x=0, y=0)

    buttonJvsJ = tk.Button(frameChoixAdversaire)
    buttonJvsJ.configure(cursor="hand2", font="{Arial} 32 {}", text='Joueur \nVS \nJoueur', width=8, command=lambda: lancerPartie(toplevelFenetre, False))
    buttonJvsJ.place(anchor="nw", relx=0.1, rely=0.0, x=0, y=0)

"""
    @brief  Créé le widget permettant de choisir la hauteur (nombre de ligne) du plateau
    @param  toplevelFenetre la fenêtre où placer les boutons
"""
def creerFrameHauteur(toplevelFenetre : tk.Toplevel):
    iTkHauteurPlateau : int = tk.IntVar()
    iTkHauteurPlateau.set(6)

    frameHauteur = tk.Frame(toplevelFenetre)
    frameHauteur.configure(height=150, width=400)
    frameHauteur.place(anchor="nw", rely=0.55, x=10, y=5)

    scaleHauteur = tk.Scale(frameHauteur)
    scaleHauteur.configure(cursor="sb_h_double_arrow", from_=5, orient="horizontal", relief="flat", to=10, length=200, width=20,
                            variable=iTkHauteurPlateau, command=updateHauteurPlateau)
    scaleHauteur.place(anchor="nw", relx=0.2, rely=0.0, x=0, y=0)

    labelHauteur = tk.Label(frameHauteur)
    labelHauteur.configure(text='Hauteur du plateau', font=20)
    labelHauteur.place(anchor="nw", relx=0.25, rely=0.4, x=0, y=0)

"""
    @brief  Créé le widget permettant de choisir la largeur (nombre de colonne) du plateau
    @param  toplevelFenetre la fenêtre où placer les boutons
"""
def creerFrameLargeur(toplevelFenetre : tk.Toplevel):
    iTkLargeurPlateau : int = tk.IntVar()
    iTkLargeurPlateau.set(7)

    frameLargeur = tk.Frame(toplevelFenetre)
    frameLargeur.configure(height=150, width=400)
    frameLargeur.place(anchor="nw", relx=0.5, rely=0.55, x=10, y=5)

    scaleLargeur = tk.Scale(frameLargeur)
    scaleLargeur.configure(cursor="sb_h_double_arrow", from_=5, orient="horizontal", relief="flat", to=10, length=200, width=20,
                            variable=iTkLargeurPlateau, command=updateLargeurPlateau)
    scaleLargeur.place(anchor="nw", relx=0.18, rely=0, x=0, y=0)

    labelLargeur = tk.Label(frameLargeur)
    labelLargeur.configure(text='Largeur du plateau', font=20)
    labelLargeur.place(anchor="nw", relx=0.23, rely=0.4, x=0, y=0) 

"""
    @brief  Créé le widget permettant de choisir le nombre de jeton à alligner pour gagner
    @param  toplevelFenetre la fenêtre où placer les boutons
"""
def creerFrameNombreJetonVictoire(toplevelFenetre : tk.Toplevel):
    iTkNbJetonVictoire : int = tk.IntVar()
    iTkNbJetonVictoire.set(4)

    frameNombreJetonVictoire = tk.Frame(toplevelFenetre)
    frameNombreJetonVictoire.configure(height=150, width=400)
    frameNombreJetonVictoire.place(anchor="nw", relx=0.0, rely=0.75, x=10, y=5)

    scaleNombreJetonVictoire = tk.Scale(frameNombreJetonVictoire)
    scaleNombreJetonVictoire.configure(cursor="sb_h_double_arrow", from_=3, orient="horizontal", relief="flat", to=5, length=200, width=20, 
                                       variable=iNbJetonVictoire, command=updateNbJetonVicoire(iTkNbJetonVictoire))
    scaleNombreJetonVictoire.place(anchor="nw", relx=0.2, rely=0.0, x=0, y=0)

    labelNombreJetonVictoire = tk.Label(frameNombreJetonVictoire)
    labelNombreJetonVictoire.configure(text='Nombre de jeton à alligner', font=20)
    labelNombreJetonVictoire.place(anchor="nw", relx=0.18, rely=0.37, x=0, y=0)
     
"""
    @brief  Créé les checkbutton pour undo/redo et coup spécial
    @param  toplevelFenetre la fenêtre où placer les boutons
"""
def creerFrameCheckButton(toplevelFenetre : tk.Toplevel):
    bTkUndoRedo : bool = tk.BooleanVar()
    bTkCoupSpecial : bool = tk.BooleanVar()
    bTkUndoRedo.set(True)
    bTkCoupSpecial.set(True)

    frameCheckButton = tk.Frame(toplevelFenetre)
    frameCheckButton.configure(height=150, width=400)
    frameCheckButton.place(anchor="nw", relx=0.5, rely=0.75, x=10, y=5)

    checkbuttonCoupSpecial = tk.Checkbutton(frameCheckButton)
    checkbuttonCoupSpecial.configure(cursor="hand2", text='Coup special', font=14, variable=bTkCoupSpecial, command=lambda:updateCoupSpecial(bTkCoupSpecial.get()))
    checkbuttonCoupSpecial.place(anchor="nw", relx=0.2, rely=0.1, x=0, y=0)

    checkbuttonUndoRedo = tk.Checkbutton(frameCheckButton)
    checkbuttonUndoRedo.configure(cursor="hand2", text='Undo / Redo', font=14, variable=bTkUndoRedo, command=lambda:updateUndoRedo(bTkUndoRedo.get()))
    checkbuttonUndoRedo.place(anchor="nw", relx=0.2, rely=0.35, x=0, y=0)

"""
    @brief  Gère l'affichage de la page principale
"""
def gererInterfacePrincipale():
    toplevelFenetrePrincipale = creerToplevelFenetre(768, 576, False, "Page principale") 

    creerFrameHaut(toplevelFenetrePrincipale)
    creerFrameChoixAdversaire(toplevelFenetrePrincipale)
    creerFrameHauteur(toplevelFenetrePrincipale)
    creerFrameLargeur(toplevelFenetrePrincipale)
    creerFrameNombreJetonVictoire(toplevelFenetrePrincipale)
    creerFrameCheckButton(toplevelFenetrePrincipale)

    toplevelFenetrePrincipale.mainloop()

gererInterfacePrincipale()