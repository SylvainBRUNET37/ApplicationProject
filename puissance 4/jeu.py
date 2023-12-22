def identifierColonneChoisi(iTabColonne, iNbLigne):
    for iBoucleL in range(iNbLigne) :
        if iTabColonne[iBoucleL] == 0 :
            return iBoucleL
    return None

def placerJeton(iTabPlateauJeu, iJoueur, iNbColonne, iNbLigne):
    bColonneValide = True
    while bColonneValide == True :
        iColonneChoisi = int(input("Saisissez le numero de la colonne ou vous voulez jouer :"))
        if iColonneChoisi <= iNbColonne and iColonneChoisi >= 0 :
            iLigneJouer = identifierColonneChoisi(iTabPlateauJeu[iColonneChoisi], iNbLigne)
            if iLigneJouer != None :
                bColonneValide = False

    iTabPlateauJeu[iColonneChoisi][iLigneJouer] = iJoueur
    return iTabPlateauJeu

def demanderPositionPlateau(iTabPlateauJeu, iNbColonne, iNbLigne):
    bPostionValide = True
    while bPostionValide == True :
        iColonneChoisi = int(input("Saisissez le numero de la colonne ou vous voulez retirer le jeton :"))
        if iColonneChoisi <= iNbColonne and iColonneChoisi >= 0 :
            iLigneChoisi = int(input("Saisissez le numero de la ligne ou vous voulez retirer le jeton :"))
            if iLigneChoisi <= iNbLigne and iLigneChoisi >= 0 :
                if (iTabPlateauJeu[iColonneChoisi][iLigneChoisi] != 0) :
                    bPostionValide = False
    return iColonneChoisi, iLigneChoisi

def retirerJeton(iTabPlateauJeu, iNbColonne, iNbLigne):
    iColonneChoisi, iLigneChoisi = demanderPositionPlateau(iTabPlateauJeu, iNbColonne, iNbLigne)
    iTabPlateauJeu[iColonneChoisi][iLigneChoisi] = 0
    iBoucleL = iLigneChoisi+1
    while iBoucleL < iNbLigne :
        if iTabPlateauJeu[iColonneChoisi][iBoucleL] == 0 :
            break
        else :
            iTabPlateauJeu[iColonneChoisi][iBoucleL-1] = iTabPlateauJeu[iColonneChoisi][iBoucleL]
            iTabPlateauJeu[iColonneChoisi][iBoucleL] = 0
        iBoucleL += 1

    return iTabPlateauJeu