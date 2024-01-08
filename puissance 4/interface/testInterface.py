#!/usr/bin/python3
import tkinter as tk

def hide_button(widget): 
        # This will remove the widget from toplevel 
    widget.button_JvsJ.place_forget() 
  
  
    # Method to make Button(widget) visible 
def show_button(widget): 
        # This will recover the widget from toplevel 
    widget.button_JvsJ.place(anchor="nw", relx=0.1, rely=0.0, x=0, y=0)


class PagejeuApp:
    def __init__(self, master=None):
        # build ui
        self.pageParametre = tk.Tk() if master is None else tk.Toplevel(master)
        self.pageParametre.configure(height=200, width=200)
        self.pageParametre.geometry("384x288")
        self.frame_haut = tk.Frame(self.pageParametre)
        self.frame_haut.configure(height=50, width=365)
        self.button_quitter = tk.Button(self.frame_haut)
        self.button_quitter.configure(
            cursor="hand2",
            font="{Arial} 16 {}",
            overrelief="sunken",
            text='Quitter')
        self.button_quitter.place(anchor="nw", relx=0.78, rely=0.04, x=0, y=0)
        self.label_nomJeu = tk.Label(self.frame_haut)
        self.label_nomJeu.configure(
            font="{Arial} 20 {bold underline}",
            text='Puissance N')
        self.label_nomJeu.place(anchor="nw", relx=0.23, rely=0.04, x=0, y=0)
        self.label_logo = tk.Label(self.frame_haut)
        self.img_logo = tk.PhotoImage(file="interface/logo.png")
        self.label_logo.configure(
            cursor="coffee_mug",
            height=50,
            image=self.img_logo,
            width=50)
        self.label_logo.place(anchor="nw", x=0, y=0)
        self.frame_haut.place(anchor="nw", x=10, y=5)
        self.frame_choixAdversaire = tk.Frame(self.pageParametre)
        self.frame_choixAdversaire.configure(height=90, width=365)
        self.button_JvsIA = tk.Button(self.frame_choixAdversaire)
        self.button_JvsIA.configure(
            cursor="hand2",
            font="{Arial} 16 {}",
            overrelief="sunken",
            text='Joueur \nVS \nIA',
            width=8)
        self.button_JvsIA.place(anchor="nw", relx=0.6, rely=0.0, x=0, y=0)
        self.button_JvsJ = tk.Button(self.frame_choixAdversaire)
        self.button_JvsJ.configure(
            cursor="hand2",
            font="{Arial} 16 {}",
            overrelief="sunken",
            text='Joueur \nVS \nJoueur',
            width=8,
            command=hide_button(self))
        self.button_JvsJ.place(anchor="nw", relx=0.1, rely=0.0, x=0, y=0)



        self.frame_choixAdversaire.place(anchor="nw", rely=0.23, x=10, y=5)
        self.frame_choixAdversaire.grid_propagate(0)
        self.frame_hauteur = tk.Frame(self.pageParametre)
        self.frame_hauteur.configure(height=75, width=200)
        self.scale_hauteur = tk.Scale(self.frame_hauteur)
        self.scale_hauteur.configure(
            cursor="sb_h_double_arrow",
            from_=3,
            orient="horizontal",
            relief="flat",
            to=10)
        self.scale_hauteur.place(anchor="nw", relx=0.18, rely=0.0, x=0, y=0)
        self.label_hauteur = tk.Label(self.frame_hauteur)
        self.label_hauteur.configure(text='Hauteur du plateau')
        self.label_hauteur.place(anchor="nw", relx=0.17, rely=0.52, x=0, y=0)
        self.frame_hauteur.place(anchor="nw", rely=0.55, x=10, y=5)
        self.frame_largeur = tk.Frame(self.pageParametre)
        self.frame_largeur.configure(height=75, width=200)
        self.scale_largeur = tk.Scale(self.frame_largeur)
        self.scale_largeur.configure(
            cursor="sb_h_double_arrow",
            from_=3,
            orient="horizontal",
            relief="flat",
            to=10)
        self.scale_largeur.place(anchor="nw", relx=0.135, rely=0.0, x=0, y=0)
        self.label_largeur = tk.Label(self.frame_largeur)
        self.label_largeur.configure(text='Largeur du plateau')
        self.label_largeur.place(anchor="nw", relx=0.135, rely=0.52, x=0, y=0)
        self.frame_largeur.place(anchor="nw", relx=0.5, rely=0.55, x=10, y=5)
        self.frame_nombreJeton = tk.Frame(self.pageParametre)
        self.frame_nombreJeton.configure(height=75, width=200)
        self.scale_nombreJeton = tk.Scale(self.frame_nombreJeton)
        self.scale_nombreJeton.configure(
            cursor="sb_h_double_arrow",
            from_=3,
            orient="horizontal",
            relief="flat",
            to=6)
        self.scale_nombreJeton.place(
            anchor="nw", relx=0.18, rely=0.0, x=0, y=0)
        self.label_nombreJeton = tk.Label(self.frame_nombreJeton)
        self.label_nombreJeton.configure(text='Nombre de jeton à alligner')
        self.label_nombreJeton.place(
            anchor="nw", relx=0.1, rely=0.52, x=0, y=0)
        self.frame_nombreJeton.place(
            anchor="nw", relx=0.0, rely=0.75, x=10, y=5)
        self.frame_checkbutton = tk.Frame(self.pageParametre)
        self.frame_checkbutton.configure(height=75, width=200)
        self.checkbutton_undoRedo = tk.Checkbutton(self.frame_checkbutton)
        self.checkbutton_undoRedo.configure(cursor="hand2", text='Undo / Redo')
        self.checkbutton_undoRedo.place(
            anchor="nw", relx=0.14, rely=0.43, x=0, y=0)
        self.checkbutton_coupSpecial = tk.Checkbutton(self.frame_checkbutton)
        self.checkbutton_coupSpecial.configure(
            cursor="hand2", text='Coup special')
        self.checkbutton_coupSpecial.place(
            anchor="nw", relx=0.14, rely=0.15, x=0, y=0)
        self.frame_checkbutton.place(
            anchor="nw", relx=0.5, rely=0.75, x=10, y=5)

        # Main widget
        self.mainwindow = self.pageParametre

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = PagejeuApp()
    app.run()

