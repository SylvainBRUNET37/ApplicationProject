import tkinter as tk
from tkinter import colorchooser

def dessiner_cercle(event):
    # Effacer le contenu précédent du Canvas
    canvas.delete("all")

    # Récupérer les dimensions du Canvas
    largeur = canvas.winfo_width()
    hauteur = canvas.winfo_height()

    # Calculer les coordonnées du centre du cercle
    centre_x = largeur / 2
    centre_y = hauteur / 2

    # Calculer le rayon du cercle (prendre la moitié de la dimension minimale)
    rayon = min(centre_x, centre_y) - 10

    # Dessiner le cercle sur le Canvas avec une couleur de remplissage
    canvas.create_oval(centre_x - rayon, centre_y - rayon, centre_x + rayon, centre_y + rayon, outline="black", fill=couleur, width=2)

def choisir_couleur(couleur_defaut, event):
    global couleur
    couleur_dialogue = colorchooser.askcolor(initialcolor=couleur_defaut)
    if couleur_dialogue[1] is not None:
        couleur = couleur_dialogue[1]
        dessiner_cercle(None)  # Passer None car la fonction est appelée par la liaison d'événement

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Cercle avec Tkinter")

# Variable pour stocker la couleur
couleur = "black"

# Créer un Canvas pour dessiner le cercle
canvas = tk.Canvas(fenetre, width=300, height=300, bg="white")
canvas.pack()

# Lier le clic sur le Canvas au choix de couleur en utilisant une fonction lambda pour passer le paramètre
canvas.bind("<Button-1>", lambda event: choisir_couleur(couleur, event))

# Lier le double-clic sur le Canvas au dessin du cercle
canvas.bind("<Double-Button-1>", dessiner_cercle)

# Démarrer la boucle principale Tkinter
fenetre.mainloop()
