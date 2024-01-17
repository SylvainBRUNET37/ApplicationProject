from affichage import *

"""
    Vérifie s'il y a une victoire dans une colonne.

    :param iTabPlateauDeJeu: Le tableau du plateau de jeu.
    :param iNbColonne: Le nombre de colonnes dans le plateau.
    :param iNbLigne: Le nombre de lignes dans le plateau.
    :param iNbJetonVictoire: Le nombre de jetons consécutifs nécessaires pour la victoire.
    :return: 0 si aucune victoire, sinon le numéro du joueur gagnant.
"""
def verifColonne(iTabPlateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire):
    for iBoucleC in range(iNbColonne):        
        tabVerif = []
        for iBoucleL in range(iNbLigne):
            iJeton = iTabPlateauDeJeu[iBoucleC][iBoucleL]
            if tabVerif == []:
                tabVerif.append(iJeton)
            elif iJeton == tabVerif[0] and iJeton !=0:
                tabVerif.append(iJeton)
                if len(tabVerif) == iNbJetonVictoire:
                    return tabVerif[0]
            else:
                tabVerif = [iJeton]                
    return(0)

"""
    Vérifie s'il y a une victoire dans une ligne.

    :param iTabPlateauDeJeu: Le tableau du plateau de jeu.
    :param iNbColonne: Le nombre de colonnes dans le plateau.
    :param iNbLigne: Le nombre de lignes dans le plateau.
    :param iNbJetonVictoire: Le nombre de jetons consécutifs nécessaires pour la victoire.
    :return: 0 si aucune victoire, sinon le numéro du joueur gagnant.
"""
def verifLigne(iTabPlateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire):
    for iBoucleL in range(iNbLigne):
        tabVerif = []
        for iBoucleC in range(iNbColonne):
            iJeton = iTabPlateauDeJeu[iBoucleC][iBoucleL]
            if tabVerif == []:
                tabVerif.append(iJeton)
            elif iJeton == tabVerif[0] and iJeton !=0:
                tabVerif.append(iJeton)
                if len(tabVerif) == iNbJetonVictoire:
                    return tabVerif[0]
            else:
                tabVerif = [iJeton]
        
    return(0)

"""
    Vérifie s'il y a une victoire dans une diagonale ascendante.

    :param iTabPlateauDeJeu: Le tableau du plateau de jeu.
    :param iNbColonne: Le nombre de colonnes dans le plateau.
    :param iNbLigne: Le nombre de lignes dans le plateau.
    :param iNbJetonVictoire: Le nombre de jetons consécutifs nécessaires pour la victoire.
    :return: 0 si aucune victoire, sinon le numéro du joueur gagnant.
"""
def verifDiagonaleAsc(iTabPlateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire):
    for iBoucleC in range(iNbColonne - iNbJetonVictoire + 1):
        for iBoucleL in range(iNbLigne - iNbJetonVictoire + 1):
            if iTabPlateauDeJeu[iBoucleC][iBoucleL] != 0:
                if all(iTabPlateauDeJeu[iBoucleC + i][iBoucleL + i] == iTabPlateauDeJeu[iBoucleC][iBoucleL] for i in range(iNbJetonVictoire)):
                    return(iTabPlateauDeJeu[iBoucleC][iBoucleL])
    return(0)

"""
    Vérifie s'il y a une victoire dans une diagonale descendante.

    :param iTabPlateauDeJeu: Le tableau du plateau de jeu.
    :param iNbColonne: Le nombre de colonnes dans le plateau.
    :param iNbLigne: Le nombre de lignes dans le plateau.
    :param iNbJetonVictoire: Le nombre de jetons consécutifs nécessaires pour la victoire.
    :return: 0 si aucune victoire, sinon le numéro du joueur gagnant.
"""
def verifDiagonaleDesc(iTabPlateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire):
    for iBoucleC in range(iNbJetonVictoire - 1, iNbColonne):
        for iBoucleL in range(iNbLigne - iNbJetonVictoire + 1):
            if iTabPlateauDeJeu[iBoucleC][iBoucleL] != 0:
                if all(iTabPlateauDeJeu[iBoucleC - i][iBoucleL + i] == iTabPlateauDeJeu[iBoucleC][iBoucleL] for i in range(iNbJetonVictoire)):
                    return(iTabPlateauDeJeu[iBoucleC][iBoucleL])
    return(0)

"""
    Vérifie si le plateau de jeu est complètement rempli.

    :param iTabPlateauDeJeu: Le tableau du plateau de jeu.
    :param iNbColonne: Le nombre de colonnes dans le plateau.
    :param iNbLigne: Le nombre de lignes dans le plateau.
    :return: 0 si le plateau n'est pas complètement rempli, sinon 3 (équivalent à un match nul).
"""
def verifRemplie(iTabPlateauDeJeu, iNbColonne, iNbLigne):
    for iBoucleC in range(iNbColonne):
        for iBoucleL in range(iNbLigne):
            if iTabPlateauDeJeu[iBoucleC][iBoucleL] == 0:
                return(0)
    return(3)

"""
    Fonction principale de vérification de l'état du jeu.

    :param iTabPlateauDeJeu: Le tableau du plateau de jeu.
    :param iNbColonne: Le nombre de colonnes dans le plateau.
    :param iNbLigne: Le nombre de lignes dans le plateau.
    :param iNbJetonVictoire: Le nombre de jetons consécutifs nécessaires pour la victoire.
    :return: 0 si aucune victoire, 3 si match nul, sinon le numéro du joueur gagnant.
"""
def Verif(iTabPlateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire):
    iVictoireColonne = verifColonne(iTabPlateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire)
    if iVictoireColonne != 0:
        return(iVictoireColonne)
    iVictoireLigne = verifLigne(iTabPlateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire)
    if iVictoireLigne != 0:
        return(iVictoireLigne)
    iVictoireDiagA = verifDiagonaleAsc(iTabPlateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire)
    if iVictoireDiagA != 0:
        return(iVictoireDiagA)
    iVictoireDiagD = verifDiagonaleDesc(iTabPlateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire)
    if iVictoireDiagD != 0:
        return(iVictoireDiagD)
    iRemplie = verifRemplie(iTabPlateauDeJeu, iNbColonne, iNbLigne)
    if iRemplie != 0:
        return(iRemplie)
    return(0)