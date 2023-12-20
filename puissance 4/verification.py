def verifColonne(iTabPlateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire):
    tabVerif = []
    for iBoucleC in range(iNbColonne):
        for iBoucleL in range(iNbLigne):
            iJeton = iTabPlateauDeJeu[iBoucleC][iBoucleL]
            if len(tabVerif) == iNbJetonVictoire:
                return tabVerif[0]
            elif iJeton == tabVerif[0]:
                tabVerif.append(iJeton)
            else:
                tabVerif = [iJeton]
    return(0)

def verifLigne(iTabPlateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire):
    tabVerif = []
    for iBoucleL in range(iNbLigne):
        for iBoucleC in range(iNbColonne):
            iJeton = iTabPlateauDeJeu[iBoucleC][iBoucleL]
            if len(tabVerif) == iNbJetonVictoire:
                return tabVerif[0]
            elif iJeton == tabVerif[0]:
                tabVerif.append(iJeton)
            else:
                tabVerif = [iJeton]
    return(0)

def verifDiagonaleGauche(iTabPlateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire):
    for iBoucleC in range(iNbColonne - iNbJetonVictoire + 1):
        for iBoucleL in range(iNbLigne - iNbJetonVictoire + 1):
            iJeton = iTabPlateauDeJeu[iBoucleC][iBoucleL]
            
    return 0


def verifRemplie(iTabPlateauDeJeu, iNbColonne, iNbLigne):
    for iBoucleC in range(iNbColonne):
        for iBoucleL in range(iNbLigne):
            if iTabPlateauDeJeu[iBoucleC][iBoucleL] == 0:
                return(0)
    return(3)

a = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]