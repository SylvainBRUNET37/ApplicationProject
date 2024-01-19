#!/usr/bin/python3
"""
    @file    interfaceParametre.py
    @brief   Contient les éléments de l'interface de paramètre et les fonctions pour gérer celle-ci
    @author  Sylvain BRUNET
    @version 0.3
    @date    2023-2024
"""

import tkinter as tk

###########################################################
#                  VARIABLES GLOABALES                    #
###########################################################

toplevelFenetreParametre: tk.Tk = None # Fenêtre de paramètre

sCouleurJetonJ1 : str = "yellow"
sCouleurJetonJ2 : str = "red"
iNombreCoupSpecial : int = 1
iJoueurCommence : int = 1
iDifficulteIA : int = 1 # 0 si en JvsJ, 1 pour niveau 1, 2 pour niveau 2 et 4 pour niveau 3 (correspond à la profondeur de l'algorithme)

###########################################################
#                         GETERS                          #
###########################################################

"""
    @brief Renvoie la couleur du jeton du joueur 1
    @return la couleur du jeton du joueur 1
"""
def getCouleurJetonJ1():
    global sCouleurJetonJ1
    return sCouleurJetonJ1

"""
    @brief Renvoie la couleur du jeton du joueur 2
    @return la couleur du jeton du joueur 2
"""
def getCouleurJetonJ2():
    global sCouleurJetonJ2
    return sCouleurJetonJ2

"""
    @brief Renvoie le nombre de coup spécial choisi par le joueur
    @return le nombre de coup spécial choisi par le joueur
"""
def getNombreCoupSpecial():
    global iNombreCoupSpecial
    return iNombreCoupSpecial

"""
    @brief Renvoie le joueur qui commencera la partie
    @return le joueur qui commencera la partie
"""
def getJoueurCommence():
    global iJoueurCommence
    return iJoueurCommence

"""
    @brief Renvoie la difficulté de l'IA ou 0 pour joueur contre joueur
    @return la difficulté de l'IA ou 0 pour joueur contre joueur
"""
def getDificulte():
    global iDifficulteIA
    return iDifficulteIA

###########################################################
#             FONCTIONS LIEES AUX BOUTONS                 #
###########################################################

"""
    @brief Met à jour la variable global qui défini le nombre de fois que les joueurs pourront utiliser le coup spécial
    @param iNombreCoupSpecialChoisi nombre de coup spécial choisi par l'utilisateur avec le slider
"""
def updateNombreCoupSpecial(iNombreCoupSpecialChoisi: int):
    global iNombreCoupSpecial
    iNombreCoupSpecial = iNombreCoupSpecialChoisi

"""
    @brief Ouvre la palette de couleur et stocke la couleur choisi dans la variable du joueur
    @param canvaCouleur canva où la couleur joueur est affiché
    @param iJoueur joueur qui a demander un changement de couleur
"""
def choisirCouleur(canvaCouleur: tk.Canvas, iJoueur: int):
    global toplevelFenetreParametre
    global sCouleurJetonJ1
    global sCouleurJetonJ2

    # Si c'est le joueur 1 qui a choisi de changer de couleur, ouvre la palette de couleur, stocke la couleur choisi et met à jour la couleur affiché
    if (iJoueur == 1):
        sCouleurJetonJ1 = toplevelFenetreParametre.tk.call("tk_chooseColor", "-initialcolor", sCouleurJetonJ1, "-title", "Choisi la couleur de ton jeton")
        canvaCouleur.create_oval(33, 33, 5, 5, outline="black", fill=sCouleurJetonJ1)
    # Si c'est le joueur 2, fait la même chose mais pour lui
    else :
        sCouleurJetonJ2 = toplevelFenetreParametre.tk.call("tk_chooseColor", "-initialcolor", sCouleurJetonJ2, "-title", "Choisi la couleur de ton jeton")
        canvaCouleur.create_oval(33, 33, 5, 5, outline="black", fill=sCouleurJetonJ2)

"""
    @brief  Met à jour le joueur qui doit commencer
    @param  buttonCommenceJ1 bouton du J1
    @param  buttonCommenceJ2 bouton du J2
    @param  iJoueur joueur lié au bouton cliqué
"""
def updateChoixJoueurCommence(buttonCommenceJ1: tk.Button, buttonCommenceJ2: tk.Button, iJoueur: int):
    global iJoueurCommence

    iJoueurCommence = iJoueur
    # Si c'est bouton lié au joueur 1 qui a été cliqué, le dégrise et grise celui du joueur 2
    if (iJoueur == 1):
        buttonCommenceJ1.configure(background="#ffffff", cursor="hand2", text='J1', width=3,
                                   command = lambda : updateChoixJoueurCommence(buttonCommenceJ1, buttonCommenceJ2, 1))
        buttonCommenceJ2.configure(background="#c0c0c0", cursor="hand2", text='J2', width=3,
                                   command = lambda : updateChoixJoueurCommence(buttonCommenceJ1, buttonCommenceJ2, 2))
    # Si c'est celui du joueur 2, fait la même chose mais pour lui
    else:
        buttonCommenceJ1.configure(background="#c0c0c0", cursor="hand2", text='J1', width=3,
                                   command = lambda : updateChoixJoueurCommence(buttonCommenceJ1, buttonCommenceJ2, 1))
        buttonCommenceJ2.configure(background="#ffffff", cursor="hand2", text='J2', width=3,
                                   command = lambda : updateChoixJoueurCommence(buttonCommenceJ1, buttonCommenceJ2, 2))

"""
    @brief  Met à jour la difficulté de l'IA
    @param  buttonDifficulte1 bouton lié à la difficulté 1
    @param  buttonDifficulte2 bouton lié à la difficulté 2
    @param  buttonDifficulte3 bouton lié à la difficulté 3
    @param  iDifficulteChoisi difficulté lié au bouton cliqué
"""
def updateChoixDifficulteIA(buttonDifficulte1: tk.Button, buttonDifficulte2: tk.Button, buttonDifficulte3: tk.Button, iDifficulteChoisi: int):
    global iDifficulteIA

    iDifficulteIA = iDifficulteChoisi
    # Si c'est bouton lié à la difficulté 1 qui a été cliqué, le dégrise et grise les autres
    if (iDifficulteChoisi == 1):
        buttonDifficulte1.configure(background="#ffffff", cursor="hand2", text='1', width=3,
                                    command = lambda : updateChoixDifficulteIA(buttonDifficulte1, buttonDifficulte2, buttonDifficulte3, 1))
        buttonDifficulte2.configure(background="#c0c0c0", cursor="hand2", text='2', width=3,
                                    command = lambda : updateChoixDifficulteIA(buttonDifficulte1, buttonDifficulte2, buttonDifficulte3, 2))
        buttonDifficulte3.configure(background="#c0c0c0", cursor="hand2", text='3', width=3,
                                    command = lambda : updateChoixDifficulteIA(buttonDifficulte1, buttonDifficulte2, buttonDifficulte3, 4))
    # Si c'est celui de la difficulté 2, fait la même chose mais pour lui
    elif (iDifficulteChoisi == 2):
        buttonDifficulte1.configure(background="#c0c0c0", cursor="hand2", text='1', width=3,
                                    command = lambda : updateChoixDifficulteIA(buttonDifficulte1, buttonDifficulte2, buttonDifficulte3, 1))
        buttonDifficulte2.configure(background="#ffffff", cursor="hand2", text='2', width=3,
                                    command = lambda : updateChoixDifficulteIA(buttonDifficulte1, buttonDifficulte2, buttonDifficulte3, 2))
        buttonDifficulte3.configure(background="#c0c0c0", cursor="hand2", text='3', width=3,
                                    command = lambda : updateChoixDifficulteIA(buttonDifficulte1, buttonDifficulte2, buttonDifficulte3, 4))
    # Si c'est celui de la difficulté 3, fait la même chose mais pour lui
    else:
        buttonDifficulte1.configure(background="#c0c0c0", cursor="hand2", text='1', width=3,
                                    command = lambda : updateChoixDifficulteIA(buttonDifficulte1, buttonDifficulte2, buttonDifficulte3, 1))
        buttonDifficulte2.configure(background="#c0c0c0", cursor="hand2", text='2', width=3,
                                    command = lambda : updateChoixDifficulteIA(buttonDifficulte1, buttonDifficulte2, buttonDifficulte3, 2))
        buttonDifficulte3.configure(background="#ffffff", cursor="hand2", text='3', width=3,
                                    command = lambda : updateChoixDifficulteIA(buttonDifficulte1, buttonDifficulte2, buttonDifficulte3, 4))
    
    # Lie cette fonction avec les boutons


###########################################################
#             FONCTIONS LIEES A L'AFFICHAGE               #
###########################################################

"""
    @brief  Créé le widget permettants de choisir une couleur et de l'afficher
    @param  iCoordonneeX coordonnée en abscisse où doit être placer le widget
    @param  iCoordonneeY coordonnée en ordonnée où doit être placer le widget
    @param  sNomLabel texte sur le label devant le widget de choix de couleur
    @param  iJoueur joueur qui a demander un changement de couleur (1 pour J1, 2 pour J2)
"""
def creerChoixCouleur(iCoordonneeX: int, iCoordonneeY: int, sNomLabel: str, iJoueur: int):
    global toplevelFenetreParametre
    global sCouleurJetonJ1
    global sCouleurJetonJ2

    frameCouleur: tk.Frame = tk.Frame(toplevelFenetreParametre)
    frameCouleur.configure(height=50, width=350)
    frameCouleur.place(anchor="nw", rely=iCoordonneeX, relx=iCoordonneeY)

    # Créé le label qui indique le joueur lié à la couleur
    labelCouleur: tk.Label = tk.Label(frameCouleur)
    labelCouleur.configure(font="{Arial} 16 {underline}", text=sNomLabel)
    labelCouleur.place(anchor="nw", relx=0.08, rely=0.27, x=0, y=0)

    canvaCouleur: tk.Canvas = tk.Canvas(frameCouleur)
    canvaCouleur.configure(cursor="pencil", height=75, width=75)
    
    # Affiche la couleur du jeton du joueur qui a cliqué sur le bouton
    if (iJoueur == 1):
        canvaCouleur.create_oval(33, 33, 5, 5, outline="black", fill=sCouleurJetonJ1)
    else:
        canvaCouleur.create_oval(33, 33, 5, 5, outline="black", fill=sCouleurJetonJ2)
    
    # Lie la fonction qui permet de choisir la couleur du jeton avec la couleur affichée
    canvaCouleur.bind("<Button-1>", lambda event, canvaCouleur=canvaCouleur, iJoueur=iJoueur: choisirCouleur(canvaCouleur, iJoueur))
    canvaCouleur.place(relx=0.9, rely=0.13, x=0, y=0)

"""
    @brief  Créé le slider lié au nombre de coup spécial que le joueur veut utiliser
    @param  bCoupSpecial variable qui défini si le joueur a choisi d'autoriser le coup spécial ou non
"""
def creerFrameNombreCoupSpecial(bCoupSpecial : bool):
    global toplevelFenetreParametre
    global iNombreCoupSpecial

    # Créé la variable tkinter lié au slider
    iTkNombreCoupSpecial: tk.IntVar = tk.IntVar()
    iTkNombreCoupSpecial.set(iNombreCoupSpecial)

    frameNombreCoupSpecial: tk.Frame = tk.Frame(toplevelFenetreParametre)
    frameNombreCoupSpecial.configure(height=150, width=600)
    frameNombreCoupSpecial.place(anchor="nw", relx=0.15, rely=0.4, x=0, y=0)

    labelCoupSpecial: tk.Label = tk.Label(frameNombreCoupSpecial)
    scaleNombreCoupSpecial = tk.Scale(frameNombreCoupSpecial)

    # Si le joueur ne veut pas activer le coup spécial, met le nombre de coup spécial à 0, désactive le slider et le grise
    if (bCoupSpecial == False):
        iTkNombreCoupSpecial.set(0)
        iNombreCoupSpecial = 0
        labelCoupSpecial.configure(text='Nombre de coup spécial :', font="{Arial} 16 {underline}", background="grey")
        scaleNombreCoupSpecial.configure(cursor="sb_h_double_arrow", from_=0, orient="horizontal", to=5, length=200, width=20,
                                         state="disabled", background="grey")
    # Si le joueur veut activer le coup spécial, configure et affiche le slider
    else:
        iTkNombreCoupSpecial.set(1)
        iNombreCoupSpecial = 1
        labelCoupSpecial.configure(text='Nombre de coup spécial :', font="{Arial} 16 {underline}")
        scaleNombreCoupSpecial.configure(cursor="sb_h_double_arrow", from_=0, orient="horizontal", to=5, length=200, width=20,
                                         variable=iTkNombreCoupSpecial, command=updateNombreCoupSpecial)

    labelCoupSpecial.place(anchor="nw", relx=0, rely=0.1, x=0, y=0) 
    scaleNombreCoupSpecial.place(anchor="nw", relx=0.5, rely=0, x=0, y=0)
    
"""
    @brief Créé les boutons qui permettent de choisir le joueur qui commence
"""
def creerFrameJoueurCommence():
    global toplevelFenetreParametre
    global iJoueurCommence

    frameCommence = tk.Frame(toplevelFenetreParametre)
    frameCommence.configure(height=100, width=600)
    frameCommence.place(anchor="nw", relx=0.2, rely=0.55, x=0, y=0)

    labelCommence = tk.Label(frameCommence)
    labelCommence.configure(font="{Arial} 16 {underline}", text='Joueur qui commence :')
    labelCommence.place(anchor="nw", relx=0.03, rely=0.0, x=0, y=0)
    
    # Créé puis configure les boutons
    buttonCommenceJ1 = tk.Button(frameCommence)
    buttonCommenceJ2 = tk.Button(frameCommence)
    updateChoixJoueurCommence(buttonCommenceJ1, buttonCommenceJ2, iJoueurCommence)
   
    buttonCommenceJ1.place(anchor="nw", relx=0.5, rely=0.0, x=0, y=0)
    buttonCommenceJ2.place(anchor="nw", relx=0.65, x=0, y=0)

"""
    @brief  Créé les boutons qui permettent de choisir la difficulté de l'IA
"""
def creerFrameDifficulteIA():
    global toplevelFenetreParametre
    global iDifficulteIA

    frameDifficulte = tk.Frame(toplevelFenetreParametre)
    frameDifficulte.configure(height=30, width=600)
    frameDifficulte.place(anchor="nw", relx=0.2, rely=0.7, x=0, y=0)

    labelDifficulte = tk.Label(frameDifficulte)
    buttonDifficulte1 = tk.Button(frameDifficulte)
    buttonDifficulte2 = tk.Button(frameDifficulte)
    buttonDifficulte3 = tk.Button(frameDifficulte)

    # Si le joueur veut jouer contre l'IA, active les boutons liés à la difficulté de celle-ci
    if (iDifficulteIA != 0):
        labelDifficulte.configure(font="{Arial} 16 {underline}", text='Difficultée de l\'IA :')
        updateChoixDifficulteIA(buttonDifficulte1, buttonDifficulte2, buttonDifficulte3, iDifficulteIA)
    # Si le joueur veut faire du JvsJ, désactive et grise les boutons liés à la diffuculté
    else:
        labelDifficulte.configure(font="{Arial} 16 {underline}", text='Diffcultée de l\'IA :', background="grey")
        buttonDifficulte1.configure(background="#c0c0c0", cursor="hand2", text='1', width=3, state="disabled")
        buttonDifficulte2.configure(background="#c0c0c0", cursor="hand2", text='2', width=3, state="disabled")
        buttonDifficulte3.configure(background="#c0c0c0", cursor="hand2", text='3', width=3, state="disabled")

    labelDifficulte.place(anchor="nw", relx=0.03, rely=0.0, x=0, y=0)
    buttonDifficulte1.place(anchor="nw", relx=0.37, rely=0.0, x=0, y=0)
    buttonDifficulte2.place(anchor="nw", relx=0.52, x=0, y=0)
    buttonDifficulte3.place(anchor="nw", relx=0.67, x=0, y=0)

###########################################################
#                 GESTION DE LA FENETRE                   #
###########################################################

"""
    @brief Gère l'affichage de la page de paramètre
    @param toplevelFenetre Fenêtre de paramètre
    @param dictParametre contient les paramètres déjà choisis par le joueur sur la page principale
"""
def gererInterfaceParametre(toplevelFenetre: tk.Tk, dictParametre: dict):
    global toplevelFenetreParametre
    global iDifficulteIA

    toplevelFenetreParametre = toplevelFenetre

    # Initialise la difficulté de l'IA en fonction du choisis précédement fait par le joueur sur la page principale
    iDifficulteIA = dictParametre["difficulteIA"]

    # Créé tous les widgets qui permettent de changer les paramètres
    creerChoixCouleur(0.25, 0.02, "Couleur de jeton du joueur 1 :", 1)
    creerChoixCouleur(0.25, 0.48, "Couleur de jeton du joueur 2 :", 2)
    creerFrameNombreCoupSpecial(dictParametre["stateCoupSpecial"])
    creerFrameJoueurCommence()
    creerFrameDifficulteIA()


    # Affiche la page créée
    toplevelFenetreParametre.mainloop()


