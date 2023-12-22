#!/usr/bin/python3
import tkinter as tk

def __init__():
    # build ui
    pagePrincipale = tk.Tk()
    pagePrincipale.configure(height=200, width=200)
    pagePrincipale.geometry("640x480")
    bouton_quitter = tk.Button(pagePrincipale)
    bouton_quitter.configure(font="{Arial} 16 {}", text='Quitter')
    bouton_quitter.place(anchor="nw", relx=0.83, rely=0.04, x=0, y=0)
    bouton_JvsIA = tk.Button(pagePrincipale)
    bouton_JvsIA.configure(
        compound="top",
        font="{Arial} 26 {}",
        overrelief="flat",
        text='Joueur \nVS \nIA',
        width=8)
    bouton_JvsIA.place(anchor="nw", relx=0.6, rely=0.20, x=0, y=0)
    label_nomJeu = tk.Label(pagePrincipale)
    label_nomJeu.configure(
        font="{Arial} 20 {bold underline}",
        text='Puissance N')
    label_nomJeu.place(anchor="nw", relx=0.38, rely=0.04, x=0, y=0)
    bouton_JcJ = tk.Button(pagePrincipale)
    bouton_JcJ.configure(
        compound="top",
        font="{Arial} 26 {}",
        overrelief="flat",
        text='Joueur \nVS \nJoueur',
        width=8)
    bouton_JcJ.place(anchor="nw", relx=0.15, rely=0.20, x=0, y=0)
    scale_hauteur = tk.Scale(pagePrincipale)
    scale_hauteur.configure(
        from_=3, orient="horizontal", relief="flat", to=10)
    scale_hauteur.place(anchor="nw", relx=0.20, rely=0.55, x=0, y=0)
    scale_largeur = tk.Scale(pagePrincipale)
    scale_largeur.configure(
        from_=3, orient="horizontal", relief="flat", to=10)
    scale_largeur.place(anchor="nw", relx=0.65, rely=0.55, x=0, y=0)
    scale_nombreJeton = tk.Scale(pagePrincipale)
    scale_nombreJeton.configure(
        from_=3, orient="horizontal", relief="flat", to=6)
    scale_nombreJeton.place(
            anchor="nw", relx=0.20, rely=0.70, x=0, y=0)
    label_hauteur = tk.Label(pagePrincipale)
    label_hauteur.configure(text='Hauteur du plateau')
    label_hauteur.place(anchor="nw", relx=0.20, rely=0.64, x=0, y=0)
    label_nombreJeton = tk.Label(pagePrincipale)
    label_nombreJeton.configure(
        text='Nombre de jeton \nà alligner pour gagner')
    label_nombreJeton.place(
        anchor="nw", relx=0.185, rely=0.80, x=0, y=0)
    label_largeur = tk.Label(pagePrincipale)
    label_largeur.configure(text='Largeur du plateau')
    label_largeur.place(anchor="nw", relx=0.65, rely=0.64, x=0, y=0)
    checkbutton_undoRedo = tk.Checkbutton(pagePrincipale)
    checkbutton_undoRedo.configure(text='Undo / Redo')
    checkbutton_undoRedo.place(
        anchor="nw", relx=0.65, rely=0.70, x=0, y=0)
    checkbutton_coupSpecial = tk.Checkbutton(pagePrincipale)
    checkbutton_coupSpecial.configure(text='Coup special')
    checkbutton_coupSpecial.place(
        anchor="nw", relx=0.65, rely=0.80, x=0, y=0)

    # Main widget
    mainwindow = pagePrincipale
    mainwindow.mainloop()  

__init__()
