import tkinter as tk

def creer_grille(hauteur, largeur):
    root = tk.Tk()
    root.title("Puissance 4")
    root.geometry("768x768")

    frame = tk.Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=largeur*60, height=hauteur*60)

    canva = tk.Canvas(frame, width=largeur*60, height=hauteur*60)
    canva.pack()

    grille_canva = [[None] * largeur for _ in range(hauteur)]

    for i in range(hauteur):
        for j in range(largeur):
            x1, y1 = j * 60, i * 60
            x2, y2 = x1 + 60, y1 + 60
            canva.create_rectangle(x1, y1, x2, y2, outline="black", fill="blue")
            grille_canva[i][j] = canva.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="white")

    root.mainloop()

# Exemple d'utilisation
hauteur = 5
largeur = 6
creer_grille(hauteur, largeur)
