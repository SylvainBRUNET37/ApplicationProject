TplateauDeJeu = []
TstatutJeu = []

# Initialise le plateau avec des cases vides
for iColonne in range(7):
    TplateauDeJeu.append([])
    for iLigne in range(6):
        TplateauDeJeu[iColonne].append(0)

for i in range(4):
    # Crée une copie du plateau de jeu actuel
    plateauCopie = [ligne.copy() for ligne in TplateauDeJeu]
    
    # Modifie le plateau de jeu copié
    plateauCopie[i][3] = 1
    
    # Sauvegarde la copie dans TstatutJeu
    TstatutJeu.append(plateauCopie)
    
    print(TstatutJeu)
    print("\n")
