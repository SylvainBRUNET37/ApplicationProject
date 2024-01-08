from affichage import *

def verifColonne(iTabPlateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire):
    tabVerif = [0]
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
    tabVerif = [0]
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

def verifDiagonaleAsc(iTabPlateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire):
    for iBoucleC in range(iNbColonne - iNbJetonVictoire + 1):
        for iBoucleL in range(iNbLigne - iNbJetonVictoire + 1):
            if iTabPlateauDeJeu[iBoucleC][iBoucleL] != 0:
                if all(iTabPlateauDeJeu[iBoucleC + i][iBoucleL + i] == iTabPlateauDeJeu[iBoucleC][iBoucleL] for i in range(iNbJetonVictoire)):
                    return(iTabPlateauDeJeu[iBoucleC][iBoucleL])
    return(0)

def verifDiagonaleDesc(iTabPlateauDeJeu, iNbColonne, iNbLigne, iNbJetonVictoire):
    for iBoucleC in range(iNbJetonVictoire - 1, iNbColonne):
        for iBoucleL in range(iNbLigne - iNbJetonVictoire + 1):
            if iTabPlateauDeJeu[iBoucleC][iBoucleL] != 0:
                if all(iTabPlateauDeJeu[iBoucleC - i][iBoucleL + i] == iTabPlateauDeJeu[iBoucleC][iBoucleL] for i in range(iNbJetonVictoire)):
                    return(iTabPlateauDeJeu[iBoucleC][iBoucleL])
    return(0)

def verifRemplie(iTabPlateauDeJeu, iNbColonne, iNbLigne):
    for iBoucleC in range(iNbColonne):
        for iBoucleL in range(iNbLigne):
            if iTabPlateauDeJeu[iBoucleC][iBoucleL] == 0:
                return(0)
    return(3)

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
