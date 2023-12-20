def afficherPlateau(iTabPlateauJeu, iNbColonne, iNbLigne) :
    iTabPlateauJeu2 = list(zip(*reversed(iTabPlateauJeu)))  # Pivoter le plateau de 90 degrés vers la gauche
    iTabPlateauJeu2 = list(zip(*reversed(iTabPlateauJeu2)))
    iTabPlateauJeu2 = list(zip(*reversed(iTabPlateauJeu2)))
    for iBoucleL in range(iNbLigne):
        for iBoucleC in range(iNbColonne):
            # Affichage du contenu de chaque case du plateau pivoté
            if iTabPlateauJeu2[iBoucleL][iBoucleC] == 0:
                print(".", end=" ")  # Case vide
            elif iTabPlateauJeu2[iBoucleL][iBoucleC] == 1:
                print("X", end=" ")  # Jeton joueur 1
            elif iTabPlateauJeu2[iBoucleL][iBoucleC] == 2:
                print("O", end=" ")  # Jeton joueur 2
        print()  # Nouvelle ligne pour passer à la ligne suivante
    print()  # Ligne vide pour séparer visuellement les plateaux"""
