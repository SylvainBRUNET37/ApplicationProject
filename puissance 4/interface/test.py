import tkinter as tk
from tkinter import messagebox

class InterfaceVictoire:
    def __init__(self, parent, gagnant):
        self.parent = parent
        self.gagnant = gagnant

        self.creer_interface()

    def creer_interface(self):
        self.fenetre = tk.Toplevel(self.parent)
        self.fenetre.title("Victoire")

        label_message = tk.Label(self.fenetre, text=f"Le joueur {self.gagnant} a gagné!", font=("Helvetica", 16))
        label_message.pack(pady=20)

        bouton_quitter = tk.Button(self.fenetre, text="Quitter", command=self.fenetre.destroy)
        bouton_quitter.pack(pady=10)

        # Attend que la fenêtre soit fermée
        self.fenetre.transient(self.parent)
        self.fenetre.grab_set()
        self.parent.wait_window(self.fenetre)

# Exemple d'utilisation
racine = tk.Tk()

# Simuler la victoire du joueur 1
victoire_interface = InterfaceVictoire(racine, 1)

# Simuler la victoire du joueur 2
# victoire_interface = InterfaceVictoire(racine, 2)

racine.mainloop()
