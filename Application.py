import tkinter.messagebox
from functools import partial
import tkinter as tk


class Application(tk.Tk):

    def __init__(self):
        
        tk.Tk.__init__(self)
        self.geometry("1024x720")
        self.create_widget()
        self.v=tk.IntVar()
        
        


    def create_widget(self):

        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)



        

        

        """Titre"""
        self.champ_titre=tk.Label(self,text="Projet Data-pursuit",padx="10",pady="10")
        self.champ_titre.config(font=("Courier", 44))
        self.champ_titre.pack(side="top")
        
        self.resultats=tk.Frame(self)
        self.resultats.pack(fill ="both", expand="yes")
        self.pageAcceuil()


    """Ronan"""
# page du choix du nombre de joueurs
    def pageAcceuil(self):
        # Création de la fenêtre de l'application
        self.AcceuilFrame = tk.Frame(self.resultats)
        self.AcceuilFrame.pack(expand="YES")
        # le titre
        self.AcceuilTitre = tk.Label(self.AcceuilFrame, text="Paramètres de Partie", pady="20")
        self.AcceuilTitre.config(font=("Courier", 25))
        self.AcceuilTitre.pack(side = "top")
        self.TitreChoixJoueurs = tk.Label(self.AcceuilFrame, text="Combien de joueurs ?")
        self.TitreChoixJoueurs.pack()
        self.TitreChoixJoueurs.config(font=("Courier", 20))
        #Les boutons "Radio"
        self.ChoixJoueurs = tk.Label(self.AcceuilFrame)
        vals = ['1', '2', '3', '4']
        etiqs = ['1 Joueur', '2 Joueurs', '3 Joueurs', '4 Joueurs']
        self.varGr = tk.StringVar()
        self.varGr.set(vals[1])
        for i in range(4):
            self.ChoixJoueurs = tk.Radiobutton(self.AcceuilFrame, variable=self.varGr, text=etiqs[i], value=vals[i])
            self.ChoixJoueurs.pack(side='left', expand=1)
        #le bouton de validation
        self.BoutonChoixJoueurs = tk.Button(self.resultats, text = "Valider", height=6, width=20, bd=2, bg="#dbdbdb")
        self.BoutonChoixJoueurs.config(command=partial(self.choixDesNoms))
        self.BoutonChoixJoueurs.pack(side="bottom")


#page de choix des noms des joueurs en fonction du nombre
    def choixDesNoms(self):
        nombre_joueur = self.varGr.get()
        for widget in self.resultats.winfo_children():
            widget.destroy()
        self.nomFrame = tk.Frame(self.resultats)
        self.nomFrame.pack(expand="YES")
        self.nomTitre = tk.Label(self.nomFrame, text="Nom des Joueurs", pady="20")
        self.nomTitre.config(font=("Courier", 25))
        self.nomTitre.pack(side = "top")
        self.champNom = tk.Label(self.nomFrame)
        #boucle d'affichage des champs en fonction du nombre de joueurs choisis
        rouge = tk.StringVar()
        bleu = tk.StringVar()
        jaune = tk.StringVar()
        vert = tk.StringVar()
        liste_joueurs = [rouge, bleu, jaune, vert]
        for i in range(int(nombre_joueur)):
            self.champNom = tk.Entry(self.nomFrame, text = "Joueur :",textvariable = liste_joueurs[i], width=20, justify="center")
            self.champNom.pack(side='left', expand=1)
        #le bouton de validation
        self.BoutonValidation = tk.Button(self.resultats, text = "Valider", height=6, width=20, bd=2, bg="#dbdbdb")
        self.BoutonValidation.pack(side="bottom")


    """Ronan"""


    """def affichageQuestions(self):"""

app = Application()
app.mainloop()
        