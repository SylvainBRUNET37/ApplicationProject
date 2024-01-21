#!/usr/bin/python3
"""
    @file    verification.py
    @brief   Contient les fonctions permettant de véirifier si le jeu est terminé (victoire/égalité)
    @author  Matthieu CHARTON
    @version 1.0
    @date    2023-2024
"""

"""
    @brief Vérifie s'il y a une victoire dans une colonne
    @param TplateauDeJeu    Le tableau du plateau de jeu
    @param iNbColonne       Le nombre de colonnes dans le plateau
    @param iNbLigne         Le nombre de lignes dans le plateau
    @param iNbJetonVictoire Le nombre de jetons consécutifs nécessaires pour la victoire
    @return 0 si aucune victoire, sinon le numéro du joueur gagnant
"""
def verifierColonne(TplateauDeJeu: list, iNbColonne: int, iNbLigne: int, iNbJetonVictoire: int) -> int:

    # Parcours les colonnes
    for iBoucleColonne in range(iNbColonne):        
        Tverification: list = []

        # Parcours des lignes dans la colonne
        for iBoucleLigne in range(iNbLigne):
            iJeton = TplateauDeJeu[iBoucleColonne][iBoucleLigne]

            # Initialisation du tableau de vérification si vide
            if Tverification == []:
                Tverification.append(iJeton)
            # Ajout du jeton au tableau si identique et non nul
            elif iJeton == Tverification[0] and iJeton != 0:
                Tverification.append(iJeton)
                # Vérification de la victoire
                if len(Tverification) == iNbJetonVictoire:
                    return Tverification[0]
            # Réinitialisation du tableau si jeton différent
            else:
                Tverification = [iJeton]

    return 0

"""
    @brief Vérifie s'il y a une victoire dans une ligne
    @param TplateauDeJeu    Le tableau du plateau de jeu
    @param iNbColonne       Le nombre de colonnes dans le plateau
    @param iNbLigne         Le nombre de lignes dans le plateau
    @param iNbJetonVictoire Le nombre de jetons consécutifs nécessaires pour la victoire
    @return 0 si aucune victoire, sinon le numéro du joueur gagnant
"""
def verifierLigne(TplateauDeJeu: list, iNbColonne: int, iNbLigne: int, iNbJetonVictoire: int) -> int:

    # Parcours les lignes
    for iBoucleLigne in range(iNbLigne):
        Tverification: list = []

        # Parcours des colonnes dans la ligne
        for iBoucleColonne in range(iNbColonne):
            iJeton: int = TplateauDeJeu[iBoucleColonne][iBoucleLigne]

            # Initialisation du tableau de vérification si vide
            if Tverification == []:
                Tverification.append(iJeton)
            # Ajout du jeton au tableau si identique et non nul
            elif iJeton == Tverification[0] and iJeton != 0:
                Tverification.append(iJeton)
                # Vérification de la victoire
                if len(Tverification) == iNbJetonVictoire:
                    return Tverification[0]
            # Réinitialisation du tableau si jeton différent
            else:
                Tverification = [iJeton]
        
    return 0

"""
    @brief Vérifie s'il y a une victoire dans une diagonale ascendante
    @param TplateauDeJeu    Le tableau du plateau de jeu
    @param iNbColonne       Le nombre de colonnes dans le plateau
    @param iNbLigne         Le nombre de lignes dans le plateau
    @param iNbJetonVictoire Le nombre de jetons consécutifs nécessaires pour la victoire
    @return 0 si aucune victoire, sinon le numéro du joueur gagnant
"""
def verifierDiagonaleAsc(TplateauDeJeu: list, iNbColonne: int, iNbLigne: int, iNbJetonVictoire: int) -> int:
    # Parcours des colonnes
    for iBoucleColonne in range(iNbColonne - iNbJetonVictoire + 1):
        # Parcours des lignes
        for iBoucleLigne in range(iNbLigne - iNbJetonVictoire + 1):
            # Vérifie si le premier jeton n'est pas nul
            if TplateauDeJeu[iBoucleColonne][iBoucleLigne] != 0:
                # Vérifie si tous les jetons consécutifs dans la diagonale sont identiques
                if all(TplateauDeJeu[iBoucleColonne + i][iBoucleLigne + i] == TplateauDeJeu[iBoucleColonne][iBoucleLigne] for i in range(iNbJetonVictoire)):
                    return TplateauDeJeu[iBoucleColonne][iBoucleLigne]
    return 0

"""
    @brief Vérifie s'il y a une victoire dans une diagonale descendante
    @param TplateauDeJeu    Le tableau du plateau de jeu
    @param iNbColonne       Le nombre de colonnes dans le plateau
    @param iNbLigne         Le nombre de lignes dans le plateau
    @param iNbJetonVictoire Le nombre de jetons consécutifs nécessaires pour la victoire
    @return 0 si aucune victoire, sinon le numéro du joueur gagnant
"""
def verifierDiagonaleDesc(TplateauDeJeu: list, iNbColonne: int, iNbLigne: int, iNbJetonVictoire: int) -> int:
    # Parcours des colonnes
    for iBoucleColonne in range(iNbJetonVictoire - 1, iNbColonne):
        # Parcours des lignes
        for iBoucleLigne in range(iNbLigne - iNbJetonVictoire + 1):
            # Vérifie si le premier jeton n'est pas nul
            if TplateauDeJeu[iBoucleColonne][iBoucleLigne] != 0:
                # Vérifie si tous les jetons consécutifs dans la diagonale sont identiques
                if all(TplateauDeJeu[iBoucleColonne - i][iBoucleLigne + i] == TplateauDeJeu[iBoucleColonne][iBoucleLigne] for i in range(iNbJetonVictoire)):
                    return TplateauDeJeu[iBoucleColonne][iBoucleLigne]
    return 0

"""
    @brief Vérifie si le plateau de jeu est complètement rempli
    @param TplateauDeJeu Le tableau du plateau de jeu
    @param iNbColonne    Le nombre de colonnes dans le plateau
    @param iNbLigne      Le nombre de lignes dans le plateau
    @return 0 si le plateau n'est pas complètement rempli, sinon 3 (équivalent à un match nul)
"""
def verifierPlateauRempli(TplateauDeJeu: list, iNbColonne: int, iNbLigne: int) -> int:
    # Parcours des colonnes
    for iBoucleColonne in range(iNbColonne):
        # Parcours des lignes
        for iBoucleLigne in range(iNbLigne):
            # Vérifie si il reste des emplacements vide dans le plateau
            if TplateauDeJeu[iBoucleColonne][iBoucleLigne] == 0:
                return(0)
    return(3)

"""
    @brief Fonction principale de vérification de l'état du jeu
    @param TplateauDeJeu    Le tableau du plateau de jeu
    @param iNbColonne       Le nombre de colonnes dans le plateau
    @param iNbLigne         Le nombre de lignes dans le plateau
    @param iNbJetonVictoire Le nombre de jetons consécutifs nécessaires pour la victoire
    @return 0 si aucune victoire, 3 si match nul, sinon le numéro du joueur gagnant
"""
def verifierFinJeu(TplateauDeJeu: list, iNbColonne: int, iNbLigne: int, iNbJetonVictoire: int) -> int:
    iVictoireColonne: int = verifierColonne(TplateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire)

    # Vérification de la victoire par colonne
    if iVictoireColonne != 0:
        return iVictoireColonne

    iVictoireLigne: int = verifierLigne(TplateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire)

    # Vérification de la victoire par ligne
    if iVictoireLigne != 0:
        return iVictoireLigne

    iVictoireDiagA: int = verifierDiagonaleAsc(TplateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire)

    # Vérification de la victoire par diagonale ascendante
    if iVictoireDiagA != 0:
        return iVictoireDiagA

    iVictoireDiagD: int = verifierDiagonaleDesc(TplateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire)

    # Vérification de la victoire par diagonale descendante
    if iVictoireDiagD != 0:
        return iVictoireDiagD

    iRemplie: int = verifierPlateauRempli(TplateauDeJeu, iNbColonne, iNbLigne)

    # Vérification du plateau complètement rempli
    if iRemplie != 0:
        return iRemplie

    return 0