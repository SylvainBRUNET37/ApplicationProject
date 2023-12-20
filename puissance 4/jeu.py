def identifierColonneJouer(iTabColonne, iNbLigne):
    for iBoucleL in range(iNbLigne) :
        if iTabColonne[iBoucleL] == 0 :
            return iBoucleL
    return None

def placerJeton(iTabPlateauDeJeu, iJoueur, iNbColonne, iNbLigne):
    bColonneValide = True
    while bColonneValide == True :
        iColonneJouer = int(input("Saisissez le numero de la colonne ou vous voulez jouer :"))
        if iColonneJouer <= iNbColonne and iColonneJouer >= 0 :
            iLigneJouer = identifierColonneJouer(iTabPlateauDeJeu[iColonneJouer], iNbLigne)
            if iLigneJouer != None :
                bColonneValide = 0

    iTabPlateauDeJeu[iColonneJouer][iLigneJouer] = iJoueur
    return iTabPlateauDeJeu

    
    