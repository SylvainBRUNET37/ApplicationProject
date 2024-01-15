"""
    @file jeu.py
    @brief   Contient les fonctions permettant de jouer au jeu
    @author  Sylvain BRUNET & Matthieu CHARTON
    @version 0.3
    @date    2023-2024
"""

"""
    @brief  Identifie la ligne où devra être posé le jeton à partir de la colonne que le joueur a choisi
    @param  iTabColonne colonne où le joueur veut placer son jeton
    @return "-1" si la colonne est pleine, l'indice de la ligne où le jeton doit être posé si ce n'est pas le cas
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
    @brief  Demande au joueur la colonne où il veut placer son jeton puis le place
    @param  iTabPlateauJeu plateau de jeu dans lequel le jeton doit être placé
    @param  iJoueur        joueur qui veut placer le jeton
    @param  iNbColonne     nombre de colonne du plateau de jeu
    @param  iNbLigne       nombre de ligne du plateau de jeu
    @return le plateau de jeu avec le jeton posé
"""
def placerJeton(iTabPlateauJeu: int, iJoueur: int, iNbColonne: int, iNbLigne: int) -> list:
    bColonneValide: bool = True
    while bColonneValide == True :
        iColonneChoisi = int(input("Saisissez le numero de la colonne ou vous voulez jouer :"))
        # Si l'indice de colonne saisi correspond bien a une ligne bien dans le plateau, verifie si la colonne associée est pleine
        if iColonneChoisi <= iNbColonne and iColonneChoisi >= 0 :
            iLigneJouer = identifierLigne(iTabPlateauJeu[iColonneChoisi], iNbLigne)
            # Si la colonne n'est pas pleine, sort de la boucle (sinon, repart au début)
            if iLigneJouer != None :
                bColonneValide = False

    iTabPlateauJeu[iColonneChoisi][iLigneJouer] = iJoueur
    return iTabPlateauJeu
"""
    @brief  Demande au joueur la position d'un jeton et vérifie si il est bien dans le plateau
    @param  iTabPlateauJeu plateau de jeu où le jeton doit être trouvé
    @param  iNbColonne     nombre de colonne du plateau de jeu
    @param  iNbLigne       nombre de ligne du plateau de jeu
    @return indice de la colonne où doit être posé le jeton
    @return indice de la ligne où doit être posé le jeton
"""
def demanderPositionPlateau(iTabPlateauJeu: int, iNbColonne: int, iNbLigne: int) -> int: # revoie 2 int
    bPostionValide: bool = False
    while bPostionValide == False :
        iColonneChoisi = int(input("Saisissez le numero de la colonne ou vous voulez retirer le jeton :"))
        # Si l'indice de colonne saisi correspond bien a une ligne bien dans le plateau
        if iColonneChoisi <= iNbColonne and iColonneChoisi >= 0 :
            iLigneChoisi = int(input("Saisissez le numero de la ligne ou vous voulez retirer le jeton :"))
            # Si l'indice de ligne saisi correspond bien a une ligne bien dans le plateau
            if iLigneChoisi <= iNbLigne and iLigneChoisi >= 0 :
                # Si la position du jeton est vide (0), sort de la boucle (sinon, repart au début)
                if (iTabPlateauJeu[iColonneChoisi][iLigneChoisi] != 0) :
                    bPostionValide = True
    return iColonneChoisi, iLigneChoisi

"""
    @brief  Retire un pion du plateau de jeu
    @param  iTabPlateauJeu plateau de jeu où le jeton doit retiré
    @param  iNbColonne     nombre de colonne du plateau de jeu
    @param  iNbLigne       nombre de ligne du plateau de jeu
    @return plateau de jeu avec le jeton retiré
"""
def retirerJeton(iTabPlateauJeu: int, iNbColonne: int, iNbLigne: int) -> int:
    iColonneChoisi, iLigneChoisi = demanderPositionPlateau(iTabPlateauJeu, iNbColonne, iNbLigne)
    # Suprime le jeton à la position donnée
    iTabPlateauJeu[iColonneChoisi][iLigneChoisi] = 0
    # Initialise la boucle à la position du jeton au dessus du jeton retiré
    iBoucleL: int = iLigneChoisi+1
    bFinBoucle: bool = False
    # Boucle tant qu'il faut descendre des jetons
    while iBoucleL < iNbLigne and bFinBoucle == False:
        # Si il n'y avait pas de jeton au dessus, sort de la boucle
        if iTabPlateauJeu[iColonneChoisi][iBoucleL] == 0 :
            bFinBoucle = True
        # Sinon, déplace/fait tomber le jeton en dessous
        else :
            iTabPlateauJeu[iColonneChoisi][iBoucleL-1] = iTabPlateauJeu[iColonneChoisi][iBoucleL]
            iTabPlateauJeu[iColonneChoisi][iBoucleL] = 0
        iBoucleL += 1

    return iTabPlateauJeu