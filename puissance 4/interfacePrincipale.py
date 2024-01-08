#!/usr/bin/python3
import tkinter as tk

def __init__(master=None):
    # build ui
    pageParametre = tk.Tk()
    pageParametre.configure(height=200, width=200)
    pageParametre.geometry("384x288")
    frame_haut = tk.Frame(pageParametre)
    frame_haut.configure(height=50, width=365)
    button_quitter = tk.Button(frame_haut)
    button_quitter.configure(
    cursor="hand2",
    font="{Arial} 16 {}",
    overrelief="sunken",
    text='Quitter')
    button_quitter.place(anchor="nw", relx=0.78, rely=0.04, x=0, y=0)
    label_nomJeu = tk.Label(frame_haut)
    label_nomJeu.configure(
    font="{Arial} 20 {bold underline}",
    text='Puissance N')
    label_nomJeu.place(anchor="nw", relx=0.23, rely=0.04, x=0, y=0)
    label_logo = tk.Label(frame_haut)
    img_logo = tk.PhotoImage(file="interface/logo.png")
    label_logo.configure(
    cursor="coffee_mug",
    height=50,
    image=img_logo,
    width=50)
    label_logo.place(anchor="nw", x=0, y=0)
    frame_haut.place(anchor="nw", x=10, y=5)
    frame_choixAdversaire = tk.Frame(pageParametre)
    frame_choixAdversaire.configure(height=90, width=365)
    button_JvsIA = tk.Button(frame_choixAdversaire)
    button_JvsIA.configure(
    cursor="hand2",
    font="{Arial} 16 {}",
    overrelief="sunken",
    text='Joueur \nVS \nIA',
    width=8)
    button_JvsIA.place(anchor="nw", relx=0.6, rely=0.0, x=0, y=0)
    button_JvsJ = tk.Button(frame_choixAdversaire)
    button_JvsJ.configure(
    cursor="hand2",
    font="{Arial} 16 {}",
    overrelief="sunken",
    text='Joueur \nVS \nJoueur',
    width=8)
    button_JvsJ.place(anchor="nw", relx=0.1, rely=0.0, x=0, y=0)



    frame_choixAdversaire.place(anchor="nw", rely=0.23, x=10, y=5)
    frame_choixAdversaire.grid_propagate(0)
    frame_hauteur = tk.Frame(pageParametre)
    frame_hauteur.configure(height=75, width=200)
    scale_hauteur = tk.Scale(frame_hauteur)
    scale_hauteur.configure(
    cursor="sb_h_double_arrow",
    from_=3,
    orient="horizontal",
    relief="flat",
    to=10)
    scale_hauteur.place(anchor="nw", relx=0.18, rely=0.0, x=0, y=0)
    label_hauteur = tk.Label(frame_hauteur)
    label_hauteur.configure(text='Hauteur du plateau')
    label_hauteur.place(anchor="nw", relx=0.17, rely=0.52, x=0, y=0)
    frame_hauteur.place(anchor="nw", rely=0.55, x=10, y=5)
    frame_largeur = tk.Frame(pageParametre)
    frame_largeur.configure(height=75, width=200)
    scale_largeur = tk.Scale(frame_largeur)
    scale_largeur.configure(
    cursor="sb_h_double_arrow",
    from_=3,
    orient="horizontal",
    relief="flat",
    to=10)
    scale_largeur.place(anchor="nw", relx=0.135, rely=0.0, x=0, y=0)
    label_largeur = tk.Label(frame_largeur)
    label_largeur.configure(text='Largeur du plateau')
    label_largeur.place(anchor="nw", relx=0.135, rely=0.52, x=0, y=0)
    frame_largeur.place(anchor="nw", relx=0.5, rely=0.55, x=10, y=5)
    frame_nombreJeton = tk.Frame(pageParametre)
    frame_nombreJeton.configure(height=75, width=200)
    scale_nombreJeton = tk.Scale(frame_nombreJeton)
    scale_nombreJeton.configure(
    cursor="sb_h_double_arrow",
    from_=3,
    orient="horizontal",
    relief="flat",
    to=6)
    scale_nombreJeton.place(
    anchor="nw", relx=0.18, rely=0.0, x=0, y=0)
    label_nombreJeton = tk.Label(frame_nombreJeton)
    label_nombreJeton.configure(text='Nombre de jeton à alligner')
    label_nombreJeton.place(
    anchor="nw", relx=0.1, rely=0.52, x=0, y=0)
    frame_nombreJeton.place(
    anchor="nw", relx=0.0, rely=0.75, x=10, y=5)
    frame_checkbutton = tk.Frame(pageParametre)
    frame_checkbutton.configure(height=75, width=200)
    checkbutton_undoRedo = tk.Checkbutton(frame_checkbutton)
    checkbutton_undoRedo.configure(cursor="hand2", text='Undo / Redo')
    checkbutton_undoRedo.place(
    anchor="nw", relx=0.14, rely=0.43, x=0, y=0)
    checkbutton_coupSpecial = tk.Checkbutton(frame_checkbutton)
    checkbutton_coupSpecial.configure(
    cursor="hand2", text='Coup special')
    checkbutton_coupSpecial.place(
    anchor="nw", relx=0.14, rely=0.15, x=0, y=0)
    frame_checkbutton.place(
    anchor="nw", relx=0.5, rely=0.75, x=10, y=5)
    pageParametre.mainloop()


__init__()

