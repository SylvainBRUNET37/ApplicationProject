iJoueurCourant: int = 1
nombreCoupSpecial = 2
iNbColonnePlateau: int = 7
iNbLignePlateau: int = 6
TplateauDeJeu: list = []
TstatutJeu: list = []

# Create the game board
for iBoucleI in range(iNbLignePlateau):
    TplateauDeJeu.append([])
    for iBoucleJ in range(iNbColonnePlateau):
        TplateauDeJeu[iBoucleI].append(0)

# Append multiple instances to TstatutJeu
TstatutJeu.append([TplateauDeJeu, nombreCoupSpecial, nombreCoupSpecial, 0])

# Print the results
#print(TplateauDeJeu)
print(TstatutJeu[0])
