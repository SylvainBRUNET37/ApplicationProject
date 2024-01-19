#!/usr/bin/python3
"""
    @file    interfaceGestion.py
    @brief   Contient les fonctions qui gère la création des interfaces et des passages entre elles
             Les fonctions misent dans ce fichier sont là pour éviter les importations circulaires
    @author  Sylvain BRUNET
    @version 0.3
    @date    2023-2024
"""

from interfaceGeneral import *
from interfacePrincipale import *
from interfaceParametre import *
from interfaceJeu import *

###########################################################
#             FONCTIONS INTERFACE PRINCIPALE              #
###########################################################

"""
    @brief Initialise la page principale
    @param dictParametre Contient les paramètre choisis par le joueur
"""
def initInterfacePrincipale(dictParametre: dict) -> tk.Tk:
    # Créé la fenêtre et le haut de la fenêtre
    # Donne 2 fois "None" à la fonction qui créé le bouton de retour car on ne peut pas retourner en arriere sur cette page et qu'elle ne nécessite aucun paramètres
    toplevelFenetrePrincipale = creerToplevelFenetre(768, 576, False, "Page principale") 
    creerFrameHaut(toplevelFenetrePrincipale)
    creerBoutonRetour(None, None, toplevelFenetrePrincipale)
    creerFrameChoixAdversaire(toplevelFenetrePrincipale)
    gererInterfacePrincipale(toplevelFenetrePrincipale)

"""
    @brief  Créé les boutons pour le choix d'aversaire (Joueur vs IA / Joueur vs Joueur)
    @param  Fenêtre où afficher les boutons (fenêtre principale)
"""
def creerFrameChoixAdversaire(toplevelFenetre: tk.Tk):
    frameChoixAdversaire: tk.Frame = tk.Frame(toplevelFenetre)
    frameChoixAdversaire.configure(height=200, width=750)
    frameChoixAdversaire.place(anchor="nw", rely=0.23, x=10, y=5)

    # Créé et configure le bouton JvsJ, active la fonction qui lance la page de parametre en lui envoyant 1 pour indiquer que le bouton JvsIA à été cliqué
    buttonJvsIA: tk.Button = tk.Button(frameChoixAdversaire)
    buttonJvsIA.configure(cursor="hand2", font="{Arial} 32 {}", text='Joueur \nVS \nIA', width=8, command = lambda: lancerPageParametre(toplevelFenetre, 1))
    buttonJvsIA.place(anchor="nw", relx=0.6, rely=0.0, x=0, y=0)

    # Créé et configure le bouton JvsJ, active la fonction qui lance la page de parametre en lui envoyant 0 pour indiquer que le bouton JvsJ à été cliqué
    buttonJvsJ: tk.Button = tk.Button(frameChoixAdversaire)
    buttonJvsJ.configure(cursor="hand2", font="{Arial} 32 {}", text='Joueur \nVS \nJoueur', width=8, command = lambda: lancerPageParametre(toplevelFenetre, 0))
    buttonJvsJ.place(anchor="nw", relx=0.1, rely=0.0, x=0, y=0)

"""
    @brief Met à jour la variable global qui défini l'adversaire (1 pour IA, 0 pour joueur) et lance la fenêtre de paramètre
    @param toplevelFenetre Fenêtre à détruire
    @param iAdversaireChoisi adversaire choisi par l'utilisateur (1 pour IA, 0 pour joueur)
"""
def lancerPageParametre(toplevelFenetre: tk.Tk, iAdversaireChoisi: int):
    dictParametres : dict = {"difficulteIA": iAdversaireChoisi, "nbColonnePlateau": getNbColonne(),
                             "nbLignePlateau": getNbLigne(), "nombreJetonVicoire": getNbJetonVictoire(),
                             "stateCoupSpecial": getStateCoupSpecial(), "stateUndoRedo": getStateUndoRedo()}

    # Ferme la fenêtre principale et lance la fenêtre de paramètre en donnant les paramètres déjà choisis
    toplevelFenetre.destroy()
    initInterfaceParametre(dictParametres)

###########################################################
#             FONCTIONS INTERFACE PARAMETRES              #
###########################################################

"""
    @brief Initialise la page de paramètre
    @param dictParametre dictionnaire contenant les paramètres déjà choisis sur la page principale
"""
def initInterfaceParametre(dictParametre: dict) -> tk.Tk:
    # Créé la fenêtre et le haut de la fenêtre
    # Donne en paramètre à "creerBoutonRetour" la fonction qui initialise la page principale pour pouvoir y retourner
    toplevelFenetreParametre = creerToplevelFenetre(768, 563, False, "Paramètres")
    creerFrameHaut(toplevelFenetreParametre)
    creerBoutonRetour(initInterfacePrincipale, None, toplevelFenetreParametre)
    creerBoutonLancer(toplevelFenetreParametre, dictParametre)
    gererInterfaceParametre(toplevelFenetreParametre, dictParametre)

"""
    @brief Créé le bouton pour lancer la partie
    @param toplevelFenetre fenêtre où afficher le bouton (fenêtre paramètre)
    @param dictParametre dictionnaire contenant les paramètres déjà choisis sur la page principale
"""
def creerBoutonLancer(toplevelFenetre: tk.Tk, dictParametre: dict):
    frameBoutonLancer = tk.Frame(toplevelFenetre)
    frameBoutonLancer.configure(height=200, width=400)
    frameBoutonLancer.place(anchor="nw", relx=0.3, rely=0.81, x=0, y=0)

    # Créé et configure le bouton pour lancer la partie
    buttonLancer = tk.Button(frameBoutonLancer)
    buttonLancer.configure(cursor="hand2", font="{Arial} 26", width=15, text='Lancer la partie', command= lambda: lancerPageJeu(toplevelFenetre, dictParametre))
    buttonLancer.place(anchor="nw", relx=0, x=0, y=0)

"""
    @brief Met à jour les paramètres et lance la fenêtre de jeu
    @param dictParametre paramètres déjà choisis par le joueur
"""
def lancerPageJeu(toplevelFenetre: tk.Tk, dictParametre: dict):
    # Ajoute et met à jour les paramètres dans le dictionnaire
    dictParametre.update({"couleurJetonJ1": getCouleurJetonJ1(), "couleurJetonJ2": getCouleurJetonJ2(), "nombreCoupSpecial": getNombreCoupSpecial(),
                          "joueurCommence": getJoueurCommence(), "difficulteIA": getDificulte()})
    
    # Ferme la fenêtre de parametre et lance la fenêtre de jeu en donnant les paramètres
    toplevelFenetre.destroy()
    initInterfaceJeu(dictParametre)

###########################################################
#               FONCTIONS INTERFACE DE JEU                #
###########################################################

"""
    @brief Initialise la page de jeu
    @param dictParametre paramètres choisis par le joueur
"""
def initInterfaceJeu(dictParametre: dict) -> tk.Tk:
    # Créé la fenêtre et le haut de la fenêtre
    # Donne en paramètre à "creerBoutonRetour" la fonction qui initialise la page de paramètre pour pouvoir y retourner
    toplevelFenetreJeu = creerToplevelFenetre(768, 768, False, "Puissance N")
    creerFrameHaut(toplevelFenetreJeu)
    creerBoutonRetour(initInterfaceParametre, dictParametre, toplevelFenetreJeu)
    gererInterfaceJeu(toplevelFenetreJeu, dictParametre)


# Lance la première fenêtre
initInterfacePrincipale(None)