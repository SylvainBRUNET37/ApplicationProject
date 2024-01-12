#!/usr/bin/python3
"""
    @file    interfaceParametre.py
    @brief   Contient l'interface de paramètrage de la partie
    @author  Sylvain BRUNET & Matthieu CHARTON
    @version 0.2
    @date    2023-2024
"""

from fonctionGeneralInterface import *
from interfaceJeu import gererInterfaceJeu

###########################################################
#                 VARIABLES GLOABALES                    #
##########################################################

sCouleurJetonJ1 : str = "yellow"
sCouleurJetonJ2 : str = "red"
iNombreCoupSpecial : int = 1
iJoueurCommence : int = 1
iDifficulteIA : int = 1

###########################################################
#           FONCTIONS LIEES AUX BOUTONS                  #
##########################################################

"""
    @brief Met à jour les paramètres et lance la fenêtre de partie
    @param toplevelFenetre fenêtre a fermer
    @param dictParametre adversaire choisi par l'utilisateur (True pour IA, False pour joueur)
"""
def lancerPartie(toplevelFenetre : tk.Toplevel, dictParametre : dict):
    global sCouleurJetonJ1
    global sCouleurJetonJ2
    global iNombreCoupSpecial
    global iJoueurCommence
    global iDifficulteIA
    dictParametre.update({"couleurJetonJ1": sCouleurJetonJ1, "couleurJetonJ2": sCouleurJetonJ2, "nombreCoupSpecial": iNombreCoupSpecial,
                          "joueurCommence": iJoueurCommence, "difficulteIA": iDifficulteIA})
    
    toplevelFenetre.destroy() # Ferme la fenêtre de parametre
    gererInterfaceJeu(dictParametre) # Lance la fenêtre de jeu en donnant les paramètres

"""
    @brief Met à jour la variable global qui défini le nombre de fois que les joueurs pourront utiliser le coup spécial
    @param iNombreCoupSpecialChoisi Nombre de coup spécial choisi par l'utilisateur avec le slider
"""
def updateNombreCoupSpecial(iNombreCoupSpecialChoisi : int):
    global iNombreCoupSpecial
    iNombreCoupSpecial = iNombreCoupSpecialChoisi

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
    @brief  Met à jour le joueur qui doit commencer
    @param  buttonCommenceJ1 bouton J1
    @param  buttonCommenceJ2 bouton J2
    @param  iJoueur joueur lié au bouton cliqué
"""
def updateChoixJoueurCommence(buttonCommenceJ1 : tk.Button, buttonCommenceJ2 : tk.Button, iJoueur : int):
    global iJoueurCommence
    iJoueurCommence = iJoueur
    if (iJoueur == 1):
        buttonCommenceJ1.configure(background="#ffffff", cursor="hand2", text='J1', width=3, command = lambda : updateChoixJoueurCommence(buttonCommenceJ1, buttonCommenceJ2, 1))
        buttonCommenceJ2.configure(background="#c0c0c0", cursor="hand2", text='J2', width=3, command = lambda : updateChoixJoueurCommence(buttonCommenceJ1, buttonCommenceJ2, 2))
    else:

        buttonCommenceJ1.configure(background="#c0c0c0", cursor="hand2", text='J1', width=3, command = lambda : updateChoixJoueurCommence(buttonCommenceJ1, buttonCommenceJ2, 1))
        buttonCommenceJ2.configure(background="#ffffff", cursor="hand2", text='J2', width=3, command = lambda : updateChoixJoueurCommence(buttonCommenceJ1, buttonCommenceJ2, 2))

"""
    @brief  Met à jour la difficulté de l'IA
    @param  buttonDifficulte1 bouton lié à la difficulté 1
    @param  buttonDifficulte2 bouton lié à la difficulté 2
    @param  buttonDifficulte3 bouton lié à la difficulté 3
    @param  iDifficulteChoisi difficulté lié au bouton cliqué
"""
def updateChoixDifficulteIA(buttonDifficulte1 : tk.Button, buttonDifficulte2 : tk.Button, buttonDifficulte3 : tk.Button, iDifficulteChoisi : int):
    global iDifficulteIA
    iDifficulteIA = iDifficulteChoisi
    if (iDifficulteChoisi == 1):
        buttonDifficulte1.configure(background="#ffffff", cursor="hand2", text='1', width=3)
        buttonDifficulte2.configure(background="#c0c0c0", cursor="hand2", text='2', width=3)
        buttonDifficulte3.configure(background="#c0c0c0", cursor="hand2", text='3', width=3)
    elif (iDifficulteChoisi == 2):
        buttonDifficulte1.configure(background="#c0c0c0", cursor="hand2", text='1', width=3)
        buttonDifficulte2.configure(background="#ffffff", cursor="hand2", text='2', width=3)
        buttonDifficulte3.configure(background="#c0c0c0", cursor="hand2", text='3', width=3)
    else:
        buttonDifficulte1.configure(background="#c0c0c0", cursor="hand2", text='1', width=3)
        buttonDifficulte2.configure(background="#c0c0c0", cursor="hand2", text='2', width=3)
        buttonDifficulte3.configure(background="#ffffff", cursor="hand2", text='3', width=3)


###########################################################
#           FONCTIONS LIEES A L'AFFICHAGE                #
##########################################################

"""
    @brief  Créé les widgets permettants de choisir une couleur et de l'afficher sous forme de cercle/jeton
    @param  toplevelFenetre la fenêtre où placer les boutons
    @param  iCoordonneeX coordonnée en abscisse où doit être placer le widget
    @param  iCoordonneeY coordonnée en ordonnée où doit être placer le widget
    @param  sNomLabel texte sur le label devant le widget de choix de couleur
    @param  iJoueur joueur qui a demander un changement de couleur (1 pour J1, 2 pour J2)
"""
def creerChoixCouleur(toplevelFenetre : tk.Toplevel, iCoordonneeX : int, iCoordonneeY : int, sNomLabel : str, iJoueur : int):
    global sCouleurJetonJ1
    global sCouleurJetonJ2
    if (iJoueur == 1):
        sCouleurJeton : str = sCouleurJetonJ1
    else:
        sCouleurJeton : str = sCouleurJetonJ2

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
    @param  bCoupSpecial variable qui défini si le joueur a choisi d'autoriser le coup spécial ou non
"""
def creerFrameNombreCoupSpecial(toplevelFenetre : tk.Toplevel, bCoupSpecial : bool):
    global iNombreCoupSpecial
    iTkNombreCoupSpecial : int = tk.IntVar()

    frameNombreCoupSpecial = tk.Frame(toplevelFenetre)
    frameNombreCoupSpecial.configure(height=150, width=600)
    frameNombreCoupSpecial.place(anchor="nw", relx=0.15, rely=0.4, x=0, y=0)

    labelCoupSpecial = tk.Label(frameNombreCoupSpecial)
    scaleNombreCoupSpecial = tk.Scale(frameNombreCoupSpecial)

    if (bCoupSpecial == False):
        iTkNombreCoupSpecial.set(0)
        iNombreCoupSpecial = 0
        scaleNombreCoupSpecial.configure(cursor="sb_h_double_arrow", from_=0, orient="horizontal", to=5, length=200, width=20,
                                        state="disabled", background="grey")
        labelCoupSpecial.configure(text='Nombre de coup spécial :', font="{Arial} 16 {underline}", background="grey")
    else:
        iTkNombreCoupSpecial.set(1)
        iNombreCoupSpecial = 1
        scaleNombreCoupSpecial.configure(cursor="sb_h_double_arrow", from_=0, orient="horizontal", to=5, length=200, width=20,
                                     variable=iTkNombreCoupSpecial, command=updateNombreCoupSpecial)
        labelCoupSpecial.configure(text='Nombre de coup spécial :', font="{Arial} 16 {underline}")

    labelCoupSpecial.place(anchor="nw", relx=0, rely=0.1, x=0, y=0) 
    scaleNombreCoupSpecial.place(anchor="nw", relx=0.5, rely=0, x=0, y=0)
    
"""
    @brief  Créé les boutons qui permettent de choisir le joueur qui commence
    @param  toplevelFenetre la fenêtre où placer les boutons
"""
def creerFrameJoueurCommence(toplevelFenetre : tk.Toplevel):
    frameCommence = tk.Frame(toplevelFenetre)
    frameCommence.configure(height=150, width=600)
    frameCommence.place(anchor="nw", relx=0.2, rely=0.55, x=0, y=0)

    labelCommence = tk.Label(frameCommence)
    labelCommence.configure(font="{Arial} 16 {underline}", text='Joueur qui commence :')
    labelCommence.place(anchor="nw", relx=0.03, rely=0.0, x=0, y=0)
    
    buttonCommenceJ1 = tk.Button(frameCommence)
    buttonCommenceJ1.configure(background="#ffffff", cursor="hand2", text='J1', width=3,
                               command = lambda : updateChoixJoueurCommence(buttonCommenceJ1, buttonCommenceJ2, 1))
    buttonCommenceJ1.place(anchor="nw", relx=0.5, rely=0.0, x=0, y=0)
    
    buttonCommenceJ2 = tk.Button(frameCommence)
    buttonCommenceJ2.configure(background="#c0c0c0", cursor="hand2", text='J2', width=3,
                               command = lambda : updateChoixJoueurCommence(buttonCommenceJ1, buttonCommenceJ2, 2))
    buttonCommenceJ2.place(anchor="nw", relx=0.65, x=0, y=0)

"""
    @brief  Créé les boutons qui permettent de choisir la difficulté de l'IA
    @param  toplevelFenetre la fenêtre où placer les boutons
    @param  bAdversaireChoisi adversaire choisi par le joueur (True : IA, False : joueur)
"""
def creerFrameDiffuclteIA(toplevelFenetre : tk.Toplevel, bAdversaireChoisi : bool):
    frameDiffculte = tk.Frame(toplevelFenetre)
    frameDiffculte.configure(height=150, width=600)
    frameDiffculte.place(anchor="nw", relx=0.2, rely=0.7, x=0, y=0)

    labelDifficulte = tk.Label(frameDiffculte)
    buttonDifficulte1 = tk.Button(frameDiffculte)
    buttonDifficulte2 = tk.Button(frameDiffculte)
    buttonDifficulte3 = tk.Button(frameDiffculte)

    # Si l'adeversaire veut jouer contre l'IA, active les boutons liés à la difficulté de celle-ci
    if (bAdversaireChoisi == True):
        labelDifficulte.configure(font="{Arial} 16 {underline}", text='Diffcultée de l\'IA :')

        buttonDifficulte1.configure(background="#ffffff", cursor="hand2", text='1', width=3,
                                    command = lambda : updateChoixDifficulteIA(buttonDifficulte1, buttonDifficulte2, buttonDifficulte3, 1))
        buttonDifficulte2.configure(background="#c0c0c0", cursor="hand2", text='2', width=3,
                                    command = lambda : updateChoixDifficulteIA(buttonDifficulte1, buttonDifficulte2, buttonDifficulte3, 2))
        buttonDifficulte3.configure(background="#c0c0c0", cursor="hand2", text='3', width=3,
                                    command = lambda : updateChoixDifficulteIA(buttonDifficulte1, buttonDifficulte2, buttonDifficulte3, 3))
    # Sinon, désactive et grise les boutons
    else:
        labelDifficulte.configure(font="{Arial} 16 {underline}", text='Diffcultée de l\'IA :', background="grey")

        buttonDifficulte1.configure(background="#c0c0c0", cursor="hand2", text='1', width=3, state="disabled")
        buttonDifficulte2.configure(background="#c0c0c0", cursor="hand2", text='2', width=3, state="disabled")
        buttonDifficulte3.configure(background="#c0c0c0", cursor="hand2", text='3', width=3, state="disabled")

    labelDifficulte.place(anchor="nw", relx=0.03, rely=0.0, x=0, y=0)
    buttonDifficulte1.place(anchor="nw", relx=0.37, rely=0.0, x=0, y=0)
    buttonDifficulte2.place(anchor="nw", relx=0.52, x=0, y=0)
    buttonDifficulte3.place(anchor="nw", relx=0.67, x=0, y=0)

"""
    @brief  Créé le bouton pour lancer la partie
    @param  toplevelFenetre la fenêtre où placer les boutons
    @param  dictParametre dictionnaire contenant les paramètres déjà choisis
"""
def creerBoutonLancer(toplevelFenetre : tk.Toplevel, dictParametre : dict):
    frameBoutonLancer = tk.Frame(toplevelFenetre)
    frameBoutonLancer.configure(height=250, width=600)
    frameBoutonLancer.place(anchor="nw", relx=0.3, rely=0.81, x=0, y=0)

    buttonLancer = tk.Button(frameBoutonLancer)
    buttonLancer.configure(cursor="hand2", font="{Arial} 26 {}", width=15, text='Lancer la partie', command= lambda: lancerPartie(toplevelFenetre, dictParametre))
    buttonLancer.place(anchor="nw", relx=0, x=0, y=0)

"""
    @brief  Gère l'affichage de la page de paramètre
    @param dictParametre contient les paramètres déjà choisis par le joueur
"""
def gestionPageParametre(dictParametre : dict):
    toplevelFenetreParametre = creerToplevelFenetre(768, 563, False, "Paramètres")
    
    creerFrameHaut(toplevelFenetreParametre)
    creerChoixCouleur(toplevelFenetreParametre, 0.25, 0.02, "Couleur de jeton du joueur 1 :", 1)
    creerChoixCouleur(toplevelFenetreParametre, 0.25, 0.48, "Couleur de jeton du joueur 2 :", 2)
    creerFrameNombreCoupSpecial(toplevelFenetreParametre, dictParametre["coupSpecial"])
    creerFrameJoueurCommence(toplevelFenetreParametre)
    creerFrameDiffuclteIA(toplevelFenetreParametre, dictParametre["adversaire"])
    creerBoutonLancer(toplevelFenetreParametre, dictParametre)

    toplevelFenetreParametre.mainloop()


