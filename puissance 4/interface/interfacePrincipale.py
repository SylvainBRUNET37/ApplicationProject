#!/usr/bin/python3
import tkinter as tk
from typing import *

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
#                        GETERS                          #
##########################################################

"""
    @brief  Renvoie le booléen définissant l'adversaire (joueur ou IA)
    @return le booléen définissant l'adversaire (joueur ou IA)
"""
def getAdversaire():
    return bAdversaire

"""
    @brief  Renvoie la hauteur du plateau
    @return la hauteur du plateau
"""
def getHauteurPlateau():
    return iHauteurPlateau

"""
    @brief  Renvoie la largeur du plateau
    @return la largeur du plateau
"""
def getLargeurPlateau():
    return iLargeurPlateau

"""
    @brief  Renvoie le nombre de jeton à aligner pour gagner
    @return le nombre de jeton à aligner pour gagner
"""
def getNbJetonVictoire():
    return iNbJetonVictoire

"""
    @brief  Renvoie le booléen définissant si le joueur veut que le coup spécial soit utilisable
    @return le booléen définissant si le joueur veut que le coup spécial soit utilisable
"""
def getCoupSpecial():
    return bCoupSpecial

"""
    @brief  Renvoie le booléen définissant si le joueur veut que la fonction d'undo/redo soit utilisable
    @return le booléen définissant si le joueur veut que la fonction d'undo/redo soit utilisable
"""
def getUndoRedo():
    return bUndoRedo

###########################################################
#           FONCTIONS LIEES AUX BOUTONS                  #
##########################################################

"""
    @brief Met à jour la variable global qui défini l'adversaire (True pour IA, False pour joueur)
    @param bTkAdversaire variable tkinter qui contient qui est l'adversaire
"""
def lancerPartie(bTkAdversaire):
    global bAdversaire
    bAdversaire = bTkAdversaire
    # LANCER LA DEUXIEME FENETRE

"""
    @brief Met à jour la variable global qui défini la hauteur du plateau
    @param iTkHauteurPlateau variable tkinter qui contient la hauteur du plateau
"""
def updateHauteurPlateau(iTkHauteurPlateau):
    global iHauteurPlateau
    iHauteurPlateau = iTkHauteurPlateau

"""
    @brief Met à jour la variable global qui défini la lageur du plateau
    @param iTkLargeurPlateau variable tkinter qui contient la lageur du plateau
"""
def updateLargeurPlateau(iTkLargeurPlateau):
    global iLargeurPlateau
    iLargeurPlateau = iTkLargeurPlateau

"""
    @brief Met à jour la variable global qui défini le nombre de jeton à alligner pour gagner
    @param iTkNbJetonVictoire variable tkinter qui contient le nombre de jeton à alligner pour gagner
"""
def updateNbJetonVicoire(iTkNbJetonVictoire):
    global iNbJetonVictoire
    iNbJetonVictoire = iTkNbJetonVictoire

"""
    @brief Met à jour la variable global qui défini si le coup spécial est activé en fonction de l'état de son checkbutton associé
    @param bTkCoupSpecial variable tkinter qui contient l'état du checkbutton coup spécial
"""
def updateCoupSpecial(bTkCoupSpecial):
    global bCoupSpecial
    bCoupSpecial = bTkCoupSpecial

"""
    @brief Met à jour la variable global qui défini si l'undo redo est activé en fonction de l'état de son checkbutton associé
    @param bTkUndoRedo variable tkinter qui contient l'état du checkbutton undo/redo
"""
def updateUndoRedo(bTkUndoRedo):
    global bUndoRedo
    bUndoRedo = bTkUndoRedo

###########################################################
#           FONCTIONS LIEES A L'AFFICHAGE                #
##########################################################

"""
    @brief  Créé une fenêtre
    @param  iLargeurFenetre   largeur de la fenêtre
    @param  iHauteurFenetre   hauteur de la fenêtre
    @param  bRedimensionnable si égal a True, la fenêtre sera redimensionnable (et inversement pour False)
    @param  sNomFenetre       nom de la fenêtre
    @return la fenêtre créée
"""
def creerToplevelFenetre(iLargeurFenetre : int, iHauteurFenetre : int, bRedimensionnable : bool, sNomFenetre : str) -> tk:
    toplevelFenetre = tk.Tk()

    # Recupère les dimensions (largeur et hauteur) de l'écran de l'utilisateur
    iLargeurEcran : int = toplevelFenetre.winfo_screenwidth()
    iHauteurEcran : int = toplevelFenetre.winfo_screenheight()
 
    # Calcule des coodonnées où devra être placer la fenêtre pour être au centre de l'écran
    iCoordonneeFenetreX : int = int((iLargeurEcran/2) - (iLargeurFenetre/2))
    iCoordonneeFenetreY : int = int((iHauteurEcran/2) - (iHauteurFenetre/2))
 
    # Applique les dimensions à la fenêtre et la place aux coodonnées calculées précédement
    toplevelFenetre.geometry("{}x{}+{}+{}".format(iLargeurFenetre, iHauteurFenetre, iCoordonneeFenetreX, iCoordonneeFenetreY))
    toplevelFenetre.resizable(bRedimensionnable, bRedimensionnable)
    toplevelFenetre.title(sNomFenetre)

    return toplevelFenetre

"""
    @brief  Créé la haut des pages : le logo du jeu, le titre et le bouton quitter
    @param  toplevelFenetre la fenêtre où placer le haut de page
"""    
def creerFrameHaut(toplevelFenetre : tk):
    frameHaut = tk.Frame(toplevelFenetre)
    frameHaut.configure(height=100, width=750)
    frameHaut.place(anchor="nw", x=10, y=5)

    labelLogo = tk.Label(frameHaut)
    imageLogo = tk.PhotoImage(file="./interface/logo.png")
    labelLogo.configure(image=imageLogo, height=85, width=85, background="yellow")
    labelLogo.place(anchor="nw", relx=0.08, rely=0.15)

    labelNomJeu = tk.Label(frameHaut)
    labelNomJeu.configure(font="{Arial} 36 {bold underline}", text='Puissance N')
    labelNomJeu.place(anchor="nw", relx=0.3, rely=0.20)

    buttonQuitter = tk.Button(frameHaut)
    buttonQuitter.configure(cursor="hand2", font="{Arial} 26 {}", width=6, text='Quitter', command=toplevelFenetre.destroy)
    buttonQuitter.place(anchor="nw", relx=0.75, rely=0.21)

"""
    @brief  Créé les boutons pour le choix d'aversaire (Joueur vs IA / Joueur vs Joueur)
    @param  toplevelFenetre la fenêtre où placer les boutons
"""
def creerFrameChoixAdversaire(toplevelFenetre : tk):
    frameChoixAdversaire = tk.Frame(toplevelFenetre)
    frameChoixAdversaire.configure(height=200, width=750)
    frameChoixAdversaire.place(anchor="nw", rely=0.23, x=10, y=5)

    buttonJvsIA = tk.Button(frameChoixAdversaire)
    buttonJvsIA.configure(cursor="hand2", font="{Arial} 32 {}", text='Joueur \nVS \nIA', width=8, command=lancerPartie(True))
    buttonJvsIA.place(anchor="nw", relx=0.6, rely=0.0, x=0, y=0)

    buttonJvsJ = tk.Button(frameChoixAdversaire)
    buttonJvsJ.configure(cursor="hand2", font="{Arial} 32 {}", text='Joueur \nVS \nJoueur', width=8, command=lancerPartie(False))
    buttonJvsJ.place(anchor="nw", relx=0.1, rely=0.0, x=0, y=0)

"""
    @brief  Créé le widget permettant de choisir la hauteur (nombre de ligne) du plateau
    @param  toplevelFenetre la fenêtre où placer les boutons
"""
def creerFrameHauteur(toplevelFenetre : tk):
    iTkHauteurPlateau : int = tk.IntVar()
    iTkHauteurPlateau.set(6)

    frameHauteur = tk.Frame(toplevelFenetre)
    frameHauteur.configure(height=150, width=400)
    frameHauteur.place(anchor="nw", rely=0.55, x=10, y=5)

    scaleHauteur = tk.Scale(frameHauteur)
    scaleHauteur.configure(cursor="sb_h_double_arrow", from_=5, orient="horizontal", relief="flat", to=10, length=200, width=20,
                            variable=iTkHauteurPlateau, command=updateHauteurPlateau(iTkHauteurPlateau))
    scaleHauteur.place(anchor="nw", relx=0.2, rely=0.0, x=0, y=0)

    labelHauteur = tk.Label(frameHauteur)
    labelHauteur.configure(text='Hauteur du plateau', font=20)
    labelHauteur.place(anchor="nw", relx=0.25, rely=0.4, x=0, y=0)

"""
    @brief  Créé le widget permettant de choisir la largeur (nombre de colonne) du plateau
    @param  toplevelFenetre la fenêtre où placer les boutons
"""
def creerFrameLargeur(toplevelFenetre : tk):
    iTkLargeurPlateau : int = tk.IntVar()
    iTkLargeurPlateau.set(7)

    frameLargeur = tk.Frame(toplevelFenetre)
    frameLargeur.configure(height=150, width=400)
    frameLargeur.place(anchor="nw", relx=0.5, rely=0.55, x=10, y=5)

    scaleLargeur = tk.Scale(frameLargeur)
    scaleLargeur.configure(cursor="sb_h_double_arrow", from_=5, orient="horizontal", relief="flat", to=10, length=200, width=20,
                            variable=iTkLargeurPlateau, command=updateLargeurPlateau(iTkLargeurPlateau))
    scaleLargeur.place(anchor="nw", relx=0.18, rely=0, x=0, y=0)

    labelLargeur = tk.Label(frameLargeur)
    labelLargeur.configure(text='Largeur du plateau', font=20)
    labelLargeur.place(anchor="nw", relx=0.23, rely=0.4, x=0, y=0) 

"""
    @brief  Créé le widget permettant de choisir le nombre de jeton à alligner pour gagner
    @param  toplevelFenetre la fenêtre où placer les boutons
"""
def creerFrameNombreJetonVictoire(toplevelFenetre : tk):
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
def creerFrameCheckButton(toplevelFenetre : tk):
    bTkUndoRedo : bool = tk.BooleanVar()
    bTkUndoRedo.set(True)

    frameCheckButton = tk.Frame(toplevelFenetre)
    frameCheckButton.configure(height=150, width=400)
    frameCheckButton.place(anchor="nw", relx=0.5, rely=0.75, x=10, y=5)

    checkbuttonCoupSpecial = tk.Checkbutton(frameCheckButton)
    checkbuttonCoupSpecial.configure(cursor="hand2", text='Coup special', font=14)
    checkbuttonCoupSpecial.place(anchor="nw", relx=0.2, rely=0.1, x=0, y=0)

    checkbuttonUndoRedo = tk.Checkbutton(frameCheckButton)
    checkbuttonUndoRedo.configure(cursor="hand2", text='Undo / Redo', font=14, variable=bTkUndoRedo, command=updateUndoRedo(bTkUndoRedo))
    checkbuttonUndoRedo.place(anchor="nw", relx=0.2, rely=0.35, x=0, y=0)

"""
    @brief  Gère l'affichage de la page principale
    @param  toplevelFenetre la fenêtre où placer les boutons
"""
def gererInterfacePrincipale():
    toplevelPagePrincipale = creerToplevelFenetre(768, 576, False, "Page principale") 

    creerFrameHaut(toplevelPagePrincipale)
    creerFrameChoixAdversaire(toplevelPagePrincipale)
    creerFrameHauteur(toplevelPagePrincipale)
    creerFrameLargeur(toplevelPagePrincipale)
    creerFrameNombreJetonVictoire(toplevelPagePrincipale)
    creerFrameCheckButton(toplevelPagePrincipale)

    toplevelPagePrincipale.mainloop()



gererInterfacePrincipale()