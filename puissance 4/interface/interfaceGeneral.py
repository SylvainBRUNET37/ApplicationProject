#!/usr/bin/python3
"""
    @file    interfaceGeneral.py
    @brief   Contient les fonctions utilisées par toutes les interfaces
    @author  Sylvain BRUNET
    @version 0.3
    @date    2023-2024
"""

from interfaceGeneral import *
import tkinter as tk

"""
    @brief  Créé une fenêtre à partir d'un nom et de dimmensions donné
    @param  iLargeurFenetre   largeur de la fenêtre
    @param  iHauteurFenetre   hauteur de la fenêtre
    @param  bRedimensionnable si égal a True, la fenêtre sera redimensionnable (et inversement pour False)
    @param  sNomFenetre       nom de la fenêtre
    @return la fenêtre créée
"""
def creerToplevelFenetre(iLargeurFenetre: int, iHauteurFenetre: int, bRedimensionnable: bool, sNomFenetre: str) -> tk.Tk:
    toplevelFenetre: tk.Tk = tk.Tk()

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
    @brief  Créé la haut des pages : le bouton pour revenir en arrière, le nom du jeu et le bouton quitter
    @param  toplevelFenetre la fenêtre où placer le haut de page
"""    
def creerFrameHaut(toplevelFenetre: tk.Tk):
    frameHaut: tk.Frame = tk.Frame(toplevelFenetre)
    frameHaut.configure(height=100, width=750)
    frameHaut.place(anchor="nw", x=150, y=5)

    labelNomJeu = tk.Label(frameHaut)
    labelNomJeu.configure(font="{Arial} 36 {bold underline}", text='Puissance N')
    labelNomJeu.place(anchor="nw", relx=0.12, rely=0.20)

    buttonQuitter: tk.Button = tk.Button(frameHaut)
    buttonQuitter.configure(cursor="hand2", font="{Arial} 26 {}", width=6, text='Quitter', command=toplevelFenetre.destroy)
    buttonQuitter.place(anchor="nw", relx=0.6, rely=0.21)

"""
    @brief Gère la création du bouton de retour ; lorsque le bouton est cliqué, détruit la fenêtre actuelle et reviens à l'interface d'avant
"""
def creerBoutonRetour(fonctionRetour, dictParametre: dict, toplevelFenetre: tk.Tk):
    frameBoutonRetour: tk.Frame = tk.Frame(toplevelFenetre)
    frameBoutonRetour.configure(height=150, width=150)
    frameBoutonRetour.place(anchor="nw", x=10, y=5)
    
    buttonRetour: tk.Button = tk.Button()
    # Si il c'est la page principale, désactive le bouton de retour en arrière (puisqu'il n'y a rien avant)
    if (fonctionRetour == None):
        buttonRetour.configure(cursor="hand2", font="{Arial} 26 {}", width=6, text='Retour', state="disabled")
    # Sinon, active le bouton et lie la fonction passée en paramètre avec le bouton
    else:
        buttonRetour.configure(cursor="hand2", font="{Arial} 26 {}", width=6, text='Retour',
                           command= lambda: [toplevelFenetre.destroy(), fonctionRetour(dictParametre)])
    buttonRetour.place(anchor="nw", relx=0.05, rely=0.05)