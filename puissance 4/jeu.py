def identifierColonneJouer(iTabColonne, iNbLigne):
    for iBoucleL in range(iNbLigne) :
        if iTabColonne[iBoucleL] == 0 :
            return iBoucleL
    return None

def placerJeton(iTabPlateauJeu, iJoueur, iNbColonne, iNbLigne):
    bColonneValide = True
    while bColonneValide == True :
        iColonneJouer = int(input("Saisissez le numero de la colonne ou vous voulez jouer :"))
        if iColonneJouer <= iNbColonne and iColonneJouer >= 0 :
            iLigneJouer = identifierColonneJouer(iTabPlateauJeu[iColonneJouer], iNbLigne)
            if iLigneJouer != None :
                bColonneValide = False

    iTabPlateauJeu[iColonneJouer][iLigneJouer] = iJoueur
    return iTabPlateauJeu

    
    