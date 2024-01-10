#!/usr/bin/python3
"""
    @file    interfaceParametre.py
    @brief   Contient l'interface de paramètrage de la partie
    @author  Sylvain BRUNET & Matthieu CHARTON
    @version 0.1
    @date    2023-2024
"""

from fonctionGeneralInterface import *

###########################################################
#                 VARIABLES GLOABALES                    #
##########################################################

sCouleurJetonJ1 : str = "yellow"
sCouleurJetonJ2 : str = "red"

###########################################################
#           FONCTIONS LIEES A L'AFFICHAGE                #
##########################################################

"""
    @brief Ouvre la palette de couleur et stocke la couleur choisi dans la variable du joueur
    @param toplevelFenetre Fenêtre où afficher la palette de couleur
    @param canvaCouleur canva où il faudra redessiner le cercle
    @param iJoueur joueur qui a demander un changement de couleur (1 pour J1, 2 pour J2)
"""
def choisirCouleur(toplevelFenetre : tk.Toplevel, canvaCouleur: tk.Canvas, iJoueur : int):
    if (iJoueur == 1):
        global sCouleurJetonJ1
        # Ouvre une palette de couleur et demande au joueur de choisir sa couleur
        sCouleurJetonJ1 = toplevelFenetre.tk.call("tk_chooseColor", "-initialcolor", sCouleurJetonJ1, "-title", "Choisi la couleur de ton jeton")
        # Redessine le cercle pour mettre à jour la couleur
        canvaCouleur.create_oval(33, 33, 5, 5, outline="black", fill=sCouleurJetonJ1)
    else :
        global sCouleurJetonJ2
        sCouleurJetonJ2 = toplevelFenetre.tk.call("tk_chooseColor", "-initialcolor", sCouleurJetonJ2, "-title", "Choisi la couleur de ton jeton")
        canvaCouleur.create_oval(33, 33, 5, 5, outline="black", fill=sCouleurJetonJ2)

"""
    @brief  Créé les widgets permettants de choisir une couleur et de l'afficher sous forme de cercle/jeton
    @param  toplevelFenetre la fenêtre où placer les boutons
    @param  iCoordonneeX coordonnée en abscisse où doit être placer le widget
    @param  iCoordonneeY coordonnée en ordonnée où doit être placer le widget
    @param  sNomLabel texte sur le label devant le widget de choix de couleur
    @param  iJoueur joueur qui a demander un changement de couleur (1 pour J1, 2 pour J2)
"""
def creerChoixCouleur(toplevelFenetre : tk.Toplevel, iCoordonneeX : int, iCoordonneeY : int, sNomLabel : str, iJoueur : int):
    if (iJoueur == 1):
        sCouleurJeton = sCouleurJetonJ1
    else:
        sCouleurJeton = sCouleurJetonJ2

    frameCouleur = tk.Frame(toplevelFenetre)
    frameCouleur.configure(height=50, width=350)
    frameCouleur.place(anchor="nw", rely=iCoordonneeX, relx=iCoordonneeY)

    labelCouleur = tk.Label(frameCouleur)
    labelCouleur.configure(font="{Arial} 16 {underline}",text=sNomLabel)
    labelCouleur.place(anchor="nw", relx=0.08, rely=0.27, x=0, y=0)

    canvaCouleur = tk.Canvas(frameCouleur)
    canvaCouleur.configure(closeenough=0, confine=False, cursor="pencil", height=75, width=75)
    canvaCouleur.create_oval(33, 33, 5, 5, outline="black", fill=sCouleurJeton)
    canvaCouleur.bind("<Button-1>", lambda event : choisirCouleur(toplevelFenetre, canvaCouleur, iJoueur))
    canvaCouleur.place(relx=0.9, rely=0.13, x=0, y=0)

"""
    @brief  Créé le slider pour avoir le nombre de coup spécial que le joueur veut utiliser
    @param  toplevelFenetre la fenêtre où placer les boutons
"""
def creerFrameNombreCoupSpecial(toplevelFenetre : tk.Toplevel):
    frameNombreCoupSpecial = tk.Frame(toplevelFenetre)
    frameNombreCoupSpecial.configure(height=150, width=600)
    frameNombreCoupSpecial.place(anchor="nw", relx=0.15, rely=0.45, x=0, y=0)

    labelCoupSpecial = tk.Label(frameNombreCoupSpecial)
    labelCoupSpecial.configure(text='Nombre de coup spécial :', font="{Arial} 16 {underline}")
    labelCoupSpecial.place(anchor="nw", relx=0, rely=0.1, x=0, y=0) 

    scaleNombreCoupSpecial = tk.Scale(frameNombreCoupSpecial)
    scaleNombreCoupSpecial.configure(cursor="sb_h_double_arrow", from_=0, orient="horizontal", to=5, length=200, width=20)
    scaleNombreCoupSpecial.place(anchor="nw", relx=0.5, rely=0, x=0, y=0)

"""
    @brief  Créé les boutons qui permettent de choisir le joueur qui commence
    @param  toplevelFenetre la fenêtre où placer les boutons
"""
def creerFrameJoueurCommence(toplevelFenetre : tk.Toplevel):
    frameCommence = tk.Frame(toplevelFenetre)
    frameCommence.configure(height=150, width=600)
    frameCommence.place(anchor="nw", relx=0.2, rely=0.65, x=0, y=0)

    labelCommence = tk.Label(frameCommence)
    labelCommence.configure(font="{Arial} 16 {underline}", text='Joueur qui commence :')
    labelCommence.place(anchor="nw", relx=0.03, rely=0.0, x=0, y=0)
    
    buttonCommenceJ1 = tk.Button(frameCommence)
    buttonCommenceJ1.configure(background="#ffffff", cursor="hand2", text='J1', width=3)
    buttonCommenceJ1.place(anchor="nw", relx=0.5, rely=0.0, x=0, y=0)
    
    buttonCommenceJ2 = tk.Button(frameCommence)
    buttonCommenceJ2.configure(background="#c0c0c0", cursor="hand2", text='J2', width=3)
    buttonCommenceJ2.place(anchor="nw", relx=0.65, x=0, y=0)

"""
    @brief  Créé les boutons qui permettent de choisir la difficulté de l'IA
    @param  toplevelFenetre la fenêtre où placer les boutons
"""
def creerFrameDiffuclteIA(toplevelFenetre : tk.Toplevel):
    frameDiffculte = tk.Frame(toplevelFenetre)
    frameDiffculte.configure(height=150, width=600)
    frameDiffculte.place(anchor="nw", relx=0.2, rely=0.8, x=0, y=0)

    labelDifficulte = tk.Label(frameDiffculte)
    labelDifficulte.configure(font="{Arial} 16 {underline}", text='Diffcultée de l\'IA :')
    labelDifficulte.place(anchor="nw", relx=0.03, rely=0.0, x=0, y=0)
    
    buttonDifficulte1 = tk.Button(frameDiffculte)
    buttonDifficulte1.configure(background="#ffffff", cursor="hand2", text='J1', width=3)
    buttonDifficulte1.place(anchor="nw", relx=0.37, rely=0.0, x=0, y=0)
    
    buttonDifficulte2 = tk.Button(frameDiffculte)
    buttonDifficulte2.configure(background="#c0c0c0", cursor="hand2", text='J2', width=3)
    buttonDifficulte2.place(anchor="nw", relx=0.52, x=0, y=0)

    buttonDifficulte3 = tk.Button(frameDiffculte)
    buttonDifficulte3.configure(background="#c0c0c0", cursor="hand2", text='J2', width=3)
    buttonDifficulte3.place(anchor="nw", relx=0.67, x=0, y=0)

"""
    @brief  Gère l'affichage de la page de paramètre
    @param diectParametres contient les paramètres déjà choisis par le joueur
"""
def gestionPageParametre(dictParametres : dict):
    global sCouleurJetonJ1
    global sCouleurJetonJ2

    #dictParametres.update({"CouleurJetonJ1": sCouleurJetonJ1, "CouleurJetonJ2": sCouleurJetonJ2})
    #print(dictParametres)

    toplevelPageParametre = creerToplevelFenetre(768, 563, False, "Paramètres")
    creerFrameHaut(toplevelPageParametre)
    creerChoixCouleur(toplevelPageParametre, 0.25, 0.02, "Couleur de jeton du joueur 1 :", 1)
    creerChoixCouleur(toplevelPageParametre, 0.25, 0.48, "Couleur de jeton du joueur 2 :", 2)
    creerFrameNombreCoupSpecial(toplevelPageParametre)
    creerFrameJoueurCommence(toplevelPageParametre)
    creerFrameDiffuclteIA(toplevelPageParametre)

    toplevelPageParametre.mainloop()

gestionPageParametre(None)