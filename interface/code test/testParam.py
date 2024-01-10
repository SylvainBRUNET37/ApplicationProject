#!/usr/bin/python3
import tkinter as tk


class PageparametreApp:
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
        self.img_logo = tk.PhotoImage(file="logo.png")
        self.label_logo.configure(
            cursor="coffee_mug",
            height=50,
            image=self.img_logo,
            width=50)
        self.label_logo.place(anchor="nw", x=0, y=0)
        self.frame_haut.place(anchor="nw", x=10, y=5)
        self.frame_couleurJ1 = tk.Frame(self.pageParametre)
        self.frame_couleurJ1.configure(height=50, width=350)
        self.label_couleurJ1 = tk.Label(self.frame_couleurJ1)
        self.label_couleurJ1.configure(
            font="{Arial} 16 {underline}",
            text='Couleur de jeton J1 :')
        self.label_couleurJ1.place(anchor="nw", relx=0.08, rely=0.27, x=0, y=0)
        self.canva_couleurJ1 = tk.Canvas(self.frame_couleurJ1)
        self.canva_couleurJ1.configure(
            background="#8000ff",
            closeenough=0,
            confine=False,
            cursor="pencil",
            height=35,
            highlightcolor="#ffff80",
            width=35)
        self.canva_couleurJ1.place(relx=0.75, rely=0.13, x=0, y=0)
        self.frame_couleurJ1.place(anchor="nw", rely=0.20, x=17, y=0)
        self.frame_couleurJ2 = tk.Frame(self.pageParametre)
        self.frame_couleurJ2.configure(height=50, width=350)
        self.label_couleurJ2 = tk.Label(self.frame_couleurJ2)
        self.label_couleurJ2.configure(
            font="{Arial} 16 {underline}",
            text='Couleur de jeton J2 :')
        self.label_couleurJ2.place(anchor="nw", relx=0.08, rely=0.27, x=0, y=0)
        self.canva_couleurJ2 = tk.Canvas(self.frame_couleurJ2)
        self.canva_couleurJ2.configure(
            background="#8000ff",
            closeenough=0,
            confine=False,
            cursor="pencil",
            height=35,
            width=35)
        self.canva_couleurJ2.place(relx=0.75, rely=0.13, x=0, y=0)
        self.frame_couleurJ2.place(anchor="nw", rely=0.35, x=17, y=0)
        self.frame_nombreCoupSpecial = tk.Frame(self.pageParametre)
        self.frame_nombreCoupSpecial.configure(height=50, width=350)
        self.label15 = tk.Label(self.frame_nombreCoupSpecial)
        self.label15.configure(
            font="{Arial} 16 {underline}",
            text='Nombre de coup \nspécial :')
        self.label15.place(anchor="nw", relx=0.08, rely=0.0, x=0, y=0)
        self.scale_nombreCoupSpecial = tk.Scale(self.frame_nombreCoupSpecial)
        self.scale_nombreCoupSpecial.configure(
            cursor="sb_h_double_arrow", from_=0, orient="horizontal", to=5)
        self.scale_nombreCoupSpecial.place(
            anchor="nw", relx=0.68, rely=0.1, x=0, y=0)
        self.frame_nombreCoupSpecial.place(anchor="nw", rely=0.52, x=17, y=0)
        self.frame_commence = tk.Frame(self.pageParametre)
        self.frame_commence.configure(height=50, width=350)
        self.label_commence = tk.Label(self.frame_commence)
        self.label_commence.configure(
            font="{Arial} 16 {underline}",
            text='Joueur qui commence :')
        self.label_commence.place(anchor="nw", relx=0.07, rely=0.0, x=0, y=0)
        self.button_commenceJ1 = tk.Button(self.frame_commence)
        self.button_commenceJ1.configure(
            background="#ffffff",
            cursor="hand2",
            overrelief="sunken",
            text='J1',
            width=3)
        self.button_commenceJ1.place(
            anchor="nw", relx=0.76, rely=0.0, x=0, y=0)
        self.button_commenceJ2 = tk.Button(self.frame_commence)
        self.button_commenceJ2.configure(
            background="#c0c0c0",
            cursor="hand2",
            overrelief="sunken",
            text='J2',
            width=3)
        self.button_commenceJ2.place(anchor="nw", relx=0.90, x=0, y=0)
        self.frame_commence.place(anchor="nw", rely=0.72, x=17, y=0)
        self.frame_diffculte = tk.Frame(self.pageParametre)
        self.frame_diffculte.configure(height=50, width=350)
        self.label_difficulte = tk.Label(self.frame_diffculte)
        self.label_difficulte.configure(
            cursor="pirate",
            font="{Arial} 16 {underline}",
            text="Difficulté de l'IA :")
        self.label_difficulte.place(anchor="nw", relx=0.07, rely=0.0, x=0, y=0)
        self.button_difficulte1 = tk.Button(self.frame_diffculte)
        self.button_difficulte1.configure(
            background="#ffffff",
            cursor="hand2",
            overrelief="sunken",
            text='1',
            width=3)
        self.button_difficulte1.place(anchor="nw", relx=0.6, x=0, y=0)
        self.button_difficulte2 = tk.Button(self.frame_diffculte)
        self.button_difficulte2.configure(
            background="#c0c0c0",
            cursor="hand2",
            overrelief="sunken",
            text='2',
            width=3)
        self.button_difficulte2.place(anchor="nw", relx=0.75, x=0, y=0)
        self.button_difficulte3 = tk.Button(self.frame_diffculte)
        self.button_difficulte3.configure(
            background="#c0c0c0",
            cursor="hand2",
            overrelief="sunken",
            text='3',
            width=3)
        self.button_difficulte3.place(anchor="nw", relx=0.90, x=0, y=0)
        self.frame_diffculte.place(anchor="nw", rely=0.85, x=17, y=0)

        # Main widget
        self.mainwindow = self.pageParametre

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = PageparametreApp()
    app.run()

