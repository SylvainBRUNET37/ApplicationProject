#!/usr/bin/python3
"""
    @file    minMax.py
    @brief   Contient les fonctions pour l'IA
    @author  Matthieu CHARTON
    @version 1.0
    @date    2023-2024
"""

import random

from jeu.jeu import *

def gererMinMax(TplateauDeJeu: list, iProfondeur: int, bMaximisant: bool, iNbColonne: int, iNbLigne: int, iNbJetonVictoire: int) -> float:
    """
        @brief Algorithme minimax pour évaluer la position du plateau de jeu
        @param TplateauDeJeu    Le tableau du plateau de jeu.
        @param iProfondeur      La iProfondeur de recherche de l'algorithme.
        @param bMaximisant      True si bMaximisant (joueur 2), False sinon (joueur 1).
        @param iNbColonne       Le nombre de colonnes dans le plateau.
        @param iNbLigne         Le nombre de lignes dans le plateau.
        @param iNbJetonVictoire Le nombre de jetons consécutifs nécessaires pour la victoire.
        @return la valeur d'évaluation de la position du plateau.
    """
    
    iVictoire: int = verifierFinJeu(TplateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire)
    if iProfondeur == 0 or iVictoire != 0:
        # Cas de base : iProfondeur atteinte ou victoire/défaite/égalité
        if iVictoire == 1:
            # Victoire du joueur 1
            iScore: int = -1000
        elif iVictoire == 2:
            # Victoire du joueur 2 (IA)
            iScore: int = 1000
        elif iVictoire == 3:
            # Égalité
            iScore: int = 0
        elif iVictoire == 0:
            # Position neutre
            iScore: int = 0
        return iScore
    
    if bMaximisant:
        # Joueur 2 (IA) cherche à maximiser le score
        fMaxEval: float = float('-inf')
        # Parcourt les colonnes du plateau
        for iBoucleColonne in range(len(TplateauDeJeu)):
            if verifierColonnePleine(TplateauDeJeu, iBoucleColonne, iNbLigne):
                # Copie temporaire du plateau avec le coup joué
                TgrilleTemporaire: list = copy.deepcopy(TplateauDeJeu)
                placerJetonIA(TgrilleTemporaire, iBoucleColonne, 2)
                # Appel récursif avec le plateau modifié
                evaluation = gererMinMax(TgrilleTemporaire, iProfondeur - 1, False, iNbColonne, iNbLigne, iNbJetonVictoire)
                # Mise à jour du score maximal
                fMaxEval = max(fMaxEval, evaluation)
        return fMaxEval
    else:
        # Joueur 1 cherche à minimiser le score
        fMinEval: float = float('inf')
        # Parcourt les colonnes du plateau
        for iBoucleColonne in range(len(TplateauDeJeu)):
            if verifierColonnePleine(TplateauDeJeu, iBoucleColonne, iNbLigne):
                # Copie temporaire du plateau avec le coup joué
                TgrilleTemporaire = copy.deepcopy(TplateauDeJeu)
                placerJetonIA(TgrilleTemporaire, iBoucleColonne, 1)
                # Appel récursif avec le plateau modifié
                evaluation = gererMinMax(TgrilleTemporaire, iProfondeur - 1, True, iNbColonne, iNbLigne, iNbJetonVictoire)
                # Mise à jour du score minimal
                fMinEval = min(fMinEval, evaluation)
        return fMinEval

def trouverMeilleurCoup(TplateauDeJeu: list, iNbColonne: int, iNbLigne: int, iNbJetonVictoire: int, iProfondeur: int) -> int:
    """
        @brief Trouve le meilleur coup pour l'IA en utilisant l'algorithme minimax
        @param TplateauDeJeu    Le tableau du plateau de jeu
        @param iNbColonne       Le nombre de colonnes dans le plateau
        @param iNbLigne         Le nombre de lignes dans le plateau
        @param iNbJetonVictoire Le nombre de jetons consécutifs nécessaires pour la victoire
        @param iProfondeur      La iProfondeur de recherche de l'algorithme
        @return la colonne du meilleur coup trouvé pas l'algorithme min-max
    """

    fMaxEval: float = float('-inf')
    iMeilleurCoup: int = 0
    TplateauMelange: list = list(range(iNbColonne))
    random.shuffle(TplateauMelange)

    # Parcourt les colonnes du plateau
    for iBoucleColonne in TplateauMelange:
        if verifierColonnePleine(TplateauDeJeu, iBoucleColonne, iNbLigne):
            # Copie temporaire du plateau avec le coup joué
            TgrilleTemporaire: list = copy.deepcopy(TplateauDeJeu)
            placerJetonIA(TgrilleTemporaire, iBoucleColonne, 2)
            # Appel de l'algorithme minimax pour évaluer le coup
            fEvaluation: float = gererMinMax(TgrilleTemporaire, iProfondeur, False, iNbColonne, iNbLigne, iNbJetonVictoire)
            # Mise à jour de la colonne du meilleur coup
            if fEvaluation > fMaxEval:
                fMaxEval = fEvaluation
                iMeilleurCoup = iBoucleColonne
    return iMeilleurCoup

