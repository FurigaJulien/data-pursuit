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
        self.resultats.pack()


    def pageAcceuil(self):
        """Ronan"""


    def affichageQuestions(self):
        