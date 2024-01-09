#!/usr/bin/python3
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
    imageLogo = tk.PhotoImage(file="interface/logo.png")
    labelLogo.configure(image=imageLogo, height=85, width=85, background="yellow")
    labelLogo.place(anchor="nw", relx=0.05, rely=0.15)

    labelNomJeu = tk.Label(frameHaut)
    labelNomJeu.configure(font="{Arial} 36 {bold underline}", text='Puissance N')
    labelNomJeu.place(anchor="nw", relx=0.25, rely=0.20)

    buttonQuitter = tk.Button(frameHaut)
    buttonQuitter.configure(cursor="hand2", font="{Arial} 26 {}", width=10, text='Quitter', command=toplevelFenetre.destroy)
    buttonQuitter.place(anchor="nw", relx=0.70, rely=0.20)


def main():
    toplevelPagePrincipale = creerToplevelFenetre(768, 576, False, "Page principale")    
    creerFrameHaut(toplevelPagePrincipale)


    frame_choixAdversaire = tk.Frame(toplevelPagePrincipale)
    frame_choixAdversaire.configure(height=90, width=365)
    button_JvsIA = tk.Button(frame_choixAdversaire)
    button_JvsIA.configure(cursor="hand2", font="{Arial} 16 {}", text='Joueur \nVS \nIA', width=8)
    button_JvsIA.place(anchor="nw", relx=0.6, rely=0.0, x=0, y=0)
    button_JvsJ = tk.Button(frame_choixAdversaire)
    button_JvsJ.configure(cursor="hand2", font="{Arial} 16 {}", text='Joueur \nVS \nJoueur', width=8)
    button_JvsJ.place(anchor="nw", relx=0.1, rely=0.0, x=0, y=0)

    frame_choixAdversaire.place(anchor="nw", rely=0.23, x=10, y=5)
    frame_hauteur = tk.Frame(toplevelPagePrincipale)
    frame_hauteur.configure(height=75, width=200)
    scale_hauteur = tk.Scale(frame_hauteur)
    scale_hauteur.configure(cursor="sb_h_double_arrow", from_=3,orient="horizontal", relief="flat", to=10)
    scale_hauteur.place(anchor="nw", relx=0.18, rely=0.0, x=0, y=0)
    label_hauteur = tk.Label(frame_hauteur)
    label_hauteur.configure(text='Hauteur du plateau')
    label_hauteur.place(anchor="nw", relx=0.17, rely=0.52, x=0, y=0)
    frame_hauteur.place(anchor="nw", rely=0.55, x=10, y=5)
    
    frame_largeur = tk.Frame(toplevelPagePrincipale)
    frame_largeur.configure(height=75, width=200)
    scale_largeur = tk.Scale(frame_largeur)
    scale_largeur.configure(cursor="sb_h_double_arrow", from_=3, orient="horizontal", relief="flat", to=10)
    scale_largeur.place(anchor="nw", relx=0.135, rely=0.0, x=0, y=0)
    label_largeur = tk.Label(frame_largeur)
    label_largeur.configure(text='Largeur du plateau')
    label_largeur.place(anchor="nw", relx=0.135, rely=0.52, x=0, y=0)
    frame_largeur.place(anchor="nw", relx=0.5, rely=0.55, x=10, y=5)
    
    frame_nombreJeton = tk.Frame(toplevelPagePrincipale)
    frame_nombreJeton.configure(height=75, width=200)
    scale_nombreJeton = tk.Scale(frame_nombreJeton)
    scale_nombreJeton.configure(cursor="sb_h_double_arrow",from_=3,orient="horizontal",relief="flat",to=6)
    scale_nombreJeton.place(anchor="nw", relx=0.18, rely=0.0, x=0, y=0)
    label_nombreJeton = tk.Label(frame_nombreJeton)
    label_nombreJeton.configure(text='Nombre de jeton à alligner')
    label_nombreJeton.place(anchor="nw", relx=0.1, rely=0.52, x=0, y=0)
    frame_nombreJeton.place(anchor="nw", relx=0.0, rely=0.75, x=10, y=5)
    
    frame_checkbutton = tk.Frame(toplevelPagePrincipale)
    frame_checkbutton.configure(height=75, width=200)
    checkbutton_undoRedo = tk.Checkbutton(frame_checkbutton)
    checkbutton_undoRedo.configure(cursor="hand2", text='Undo / Redo')
    checkbutton_undoRedo.place(anchor="nw", relx=0.14, rely=0.43, x=0, y=0)
    checkbutton_coupSpecial = tk.Checkbutton(frame_checkbutton)
    checkbutton_coupSpecial.configure(cursor="hand2", text='Coup special')
    checkbutton_coupSpecial.place(anchor="nw", relx=0.14, rely=0.15, x=0, y=0)
    frame_checkbutton.place(anchor="nw", relx=0.5, rely=0.75, x=10, y=5)
    toplevelPagePrincipale.mainloop()


main()

