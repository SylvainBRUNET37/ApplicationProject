def main():
    iNbColonne = int(input("Saisissez le nombre de colonne que vous souhaitez :"))
    iNbLigne = int(input("Saisissez le nombre de ligne que vous souhaitez :"))
    iNbJetonVictoire = int(input("Saisissez le nombre de jeton qu'il faut alligner pour gagner :"))
    iJoueurCommence = int(input("Choisissez le joueur qui commence :"))

    iTabPlateauDeJeu = [[[0]*iNbColonne]*iNbLigne]
    sCouleurJetonJ1 = "yellow"
    sCouleurJetonJ2 = "red"
    bStatutCoupSpecialJ1 = 1
    bStatutCoupSpecialJ2 = 1
    
    tabStatutJeu = [[iTabPlateauDeJeu, bStatutCoupSpecialJ1, bStatutCoupSpecialJ2]]
    tabStatutJeu.append([iTabPlateauDeJeu, bStatutCoupSpecialJ1, bStatutCoupSpecialJ2])

main()
