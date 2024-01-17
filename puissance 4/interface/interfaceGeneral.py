#!/usr/bin/python3
"""
    @file    interfaceGeneral.py
    @brief   Contient les fonctions utilisées par toutes les interfaces
    @author  Sylvain BRUNET
    @version 0.3
    @date    2023-2024
"""

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
def creerFrameHaut(toplevelFenetre: tk.Tk) -> None:
    frameHaut: tk.Frame = tk.Frame(toplevelFenetre)
    frameHaut.configure(height=100, width=750)
    frameHaut.place(anchor="nw", x=10, y=5)

    #buttonRevenirArriere: tk.Button = tk.Button(frameHaut)
    #buttonRevenirArriere.configure(cursor="hand2", font="{Arial} 26 {}", width=6, text='Quitter', command=toplevelFenetre.destroy)
    #buttonRevenirArriere.place(anchor="nw", relx=0.08, rely=0.15)

    labelNomJeu: tk.Label = tk.Label(frameHaut)
    labelNomJeu.configure(font="{Arial} 36 {bold underline}", text='Puissance N')
    labelNomJeu.place(anchor="nw", relx=0.3, rely=0.20)

    buttonQuitter: tk.Button = tk.Button(frameHaut)
    buttonQuitter.configure(cursor="hand2", font="{Arial} 26 {}", width=6, text='Quitter', command=toplevelFenetre.destroy)
    buttonQuitter.place(anchor="nw", relx=0.75, rely=0.21)




