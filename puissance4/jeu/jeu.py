"""
    @file    jeu.py
    @brief   Contient les fonctions permettant de jouer au jeu
    @author  Sylvain BRUNET & Matthieu CHARTON
    @version 0.1
    @date    2023-2024
"""

import copy

from jeu.verification import *

"""
    @brief Identifie la ligne où devra être posé le jeton à partir de la colonne que le joueur a choisi
    @param iTabColonne Colonne où le joueur veut placer son jeton
    @return -1 si la colonne est pleine, l'indice de la ligne où le jeton doit être posé si ce n'est pas le cas
"""
def identifierLigne(iTabColonne: list, iNbLignePlateau: int) -> int:
    iBoucleLigne: int = 0
    bCaseVideTrouve: bool = False

    # Parcours la colonne de bas en haut et s'arrête
    while (iBoucleLigne != iNbLignePlateau and bCaseVideTrouve != True):
        # Si une case vide est trouvée, renvoie met fin à la boucle
        if iTabColonne[iBoucleLigne] == 0 :
            bCaseVideTrouve = True
        iBoucleLigne += 1

    # Si une case vide a été trouvée, renvoie l'indice le ligne de celle-ci
    if (bCaseVideTrouve == True):
        return iBoucleLigne-1 # -1 car la variable est ittéré avant de sortir de la boucle
    # Sinon, la colonne est pleine et renvoie donc -1
    else:
        return -1

"""
    @brief Inverse les jetons du plateau de jeu pour l'effet spécial
    @param TplateauDeJeu Le tableau du plateau de jeu
    @param iNbColonne    Le nombre de colonnes dans le plateau
    @param iNbLigne      Le nombre de lignes dans le plateau
    @return le plateau modifié
"""
def inverserCouleur(TplateauDeJeu: list, iNbColonne: int, iNbLigne: int) -> list:
    TplateauModifie: list = copy.deepcopy(TplateauDeJeu)
    # Parcourt toutes les cellules du plateau
    for iColonne in range(iNbColonne):
        for iLigne in range(iNbLigne):
            if TplateauDeJeu[iColonne][iLigne] == 1:
                # Inverse les jetons du joueur 1
                TplateauModifie[iColonne][iLigne] = 2
            elif TplateauDeJeu[iColonne][iLigne] == 2:
                # Inverse les jetons du joueur 2
                TplateauModifie[iColonne][iLigne] = 1
    return TplateauModifie

###########################################################
#                    JEU CONSOLE / IA                     # 
###########################################################

"""
    @brief Vérifie si la colonne spécifiée est valide pour placer un jeton
    @param TplateauDeJeu Le tableau du plateau de jeu
    @param iColonne      La colonne à vérifier
    @param iNbLigne      Le nombre de lignes dans le plateau
    @return True si la colonne est valide, False sinon
"""
def verifierColonnePleine(TplateauDeJeu: list, iColonne: int, iNbLigne: int) -> bool:
    # Parcourt les lignes de la colonne spécifiée
    for iBoucleLigne in range(iNbLigne):
        # Vérifie si la case est vide (contient un jeton nul)
        if TplateauDeJeu[iColonne][iBoucleLigne] == 0:
            return True
    return False

"""
    @brief Joue un coup en plaçant un jeton dans la colonne spécifiée
    @param TplateauDeJeu Le tableau du plateau de jeu
    @param iColonne      La colonne dans laquelle placer le jeton
    @param iJoueur       Le joueur qui joue le coup
    @return True si le coup est joué avec succès, False sinon
"""
def placerJetonIA(TplateauDeJeu: list, iColonne: int, iJoueur: int) -> bool:
    # Parcourt les lignes de la colonne spécifiée
    for i in range(len(TplateauDeJeu[0])):
        # Vérifie si la case est vide (contient un jeton nul)
        if TplateauDeJeu[iColonne][i] == 0:
            # Place le jeton du joueur dans la case vide
            TplateauDeJeu[iColonne][i] = iJoueur
            return True
    # La colonne est pleine, le coup n'a pas pu être joué
    return False

"""
    @brief  Demande au joueur la colonne où il veut placer son jeton puis le place
    @param  iTabPlateauJeu Plateau de jeu dans lequel le jeton doit être placé
    @param  iJoueur        Joueur qui veut placer le jeton
    @param  iNbColonne     Nombre de colonne du plateau de jeu
    @param  iNbLigne       Nombre de ligne du plateau de jeu
    @return le plateau de jeu avec le jeton posé
"""
def placerJetonJoueur(iTabPlateauJeu: int, iJoueur: int, iNbColonne: int, iNbLigne: int) -> int:
    bColonneValide: bool = True
    while bColonneValide == True :
        iColonneChoisi = int(input("Saisissez le numero de la colonne ou vous voulez jouer :"))-1
        # Si l'indice de colonne saisi correspond bien a une ligne bien dans le plateau, trouve la ligne où jouer
        if iColonneChoisi <= iNbColonne and iColonneChoisi >= 0 :
            iLigneJouer = identifierLigne(iTabPlateauJeu[iColonneChoisi], iNbLigne)
            # Si la colonne n'est pas pleine, sort de la boucle (sinon, repart au début)
            if iLigneJouer != -1 :
                bColonneValide = False

    iTabPlateauJeu[iColonneChoisi][iLigneJouer] = iJoueur
    return iTabPlateauJeu

###########################################################
#                  FONCTIONS ABANDONNEES                  #
###########################################################

'''
"""
    @brief  Demande au joueur la position d'un jeton et vérifie si il est bien dans le plateau
    @param  TplateauDeJeu  Plateau de jeu où le jeton doit être trouvé
    @param  iNbColonne     Nombre de colonne du plateau de jeu
    @param  iNbLigne       Nombre de ligne du plateau de jeu
    @return indice de la colonne où doit être posé le jeton
    @return indice de la ligne où doit être posé le jeton
"""
def demanderPositionPlateau(TplateauDeJeu: list, iNbColonne: int, iNbLigne: int) -> int: # revoie 2 int
    bPostionValide: bool = False
    while bPostionValide == False :
        iColonneChoisi = int(input("Saisissez le numero de la colonne ou vous voulez retirer le jeton :"))-1
        # Si l'indice de colonne saisi correspond bien a une ligne bien dans le plateau
        if iColonneChoisi <= iNbColonne and iColonneChoisi >= 0 :
            iLigneChoisi = int(input("Saisissez le numero de la ligne ou vous voulez retirer le jeton :"))-1
            # Si l'indice de ligne saisi correspond bien a une ligne bien dans le plateau
            if iLigneChoisi <= iNbLigne and iLigneChoisi >= 0 :
                # Si la position du jeton est vide (0), sort de la boucle (sinon, repart au début)
                if (TplateauDeJeu[iColonneChoisi][iLigneChoisi] != 0) :
                    bPostionValide = True
    return iColonneChoisi, iLigneChoisi

"""
    @brief  Retire un pion du plateau de jeu
    @param  TplateauDeJeu  Plateau de jeu où le jeton doit retiré
    @param  iNbColonne     Nombre de colonne du plateau de jeu
    @param  iNbLigne       Nombre de ligne du plateau de jeu
    @return plateau de jeu avec le jeton retiré
"""
def retirerJeton(TplateauDeJeu: int, iNbColonne: int, iNbLigne: int) -> int:
    iColonneChoisi, iLigneChoisi = demanderPositionPlateau(TplateauDeJeu, iNbColonne, iNbLigne)
    # Suprime le jeton à la position donnée
    TplateauDeJeu[iColonneChoisi][iLigneChoisi] = 0
    # Initialise la boucle à la position du jeton au dessus du jeton retiré
    iBoucleLigne: int = iLigneChoisi+1
    bFinBoucle: bool = False
    # Boucle tant qu'il faut descendre des jetons
    while iBoucleLigne < iNbLigne and bFinBoucle == False:
        # Si il n'y avait pas de jeton au dessus, sort de la boucle
        if TplateauDeJeu[iColonneChoisi][iBoucleLigne] == 0 :
            bFinBoucle = True
        # Sinon, déplace/fait tomber le jeton en dessous
        else :
            TplateauDeJeu[iColonneChoisi][iBoucleLigne-1] = TplateauDeJeu[iColonneChoisi][iBoucleLigne]
            TplateauDeJeu[iColonneChoisi][iBoucleLigne] = 0
        iBoucleLigne += 1

    return TplateauDeJeu
'''

