#!/usr/bin/python3
"""
    @file    interfaceGeneral.py
    @brief   Contient les fonctions utilisées par toutes les interfaces
    @author  Sylvain BRUNET
    @version 0.3
    @date    2023-2024
"""
import tkinter as tk
from typing import *

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
    imageLogo = tk.PhotoImage(file="./logo.png")
    labelLogo.configure(image=imageLogo, height=85, width=85, background="yellow")
    labelLogo.place(anchor="nw", relx=0.08, rely=0.15)

    labelNomJeu = tk.Label(frameHaut)
    labelNomJeu.configure(font="{Arial} 36 {bold underline}", text='Puissance N')
    labelNomJeu.place(anchor="nw", relx=0.3, rely=0.20)

    buttonQuitter = tk.Button(frameHaut)
    buttonQuitter.configure(cursor="hand2", font="{Arial} 26 {}", width=6, text='Quitter', command=toplevelFenetre.destroy)
    buttonQuitter.place(anchor="nw", relx=0.75, rely=0.21)