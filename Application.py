import tkinter.messagebox
from functools import partial
import tkinter as tk
from Fonctions import *
from BDD import *
from functools import partial
import time

class Application(tk.Tk):

    def __init__(self):
        
        tk.Tk.__init__(self)
        self.geometry("1024x720")
        self.create_widget()
        self.v=tk.IntVar()
        
        
        
        
        


    def create_widget(self):

        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)
        self.themeList=BDD.getAllTheme()
        self.questionList=BDD.getAllResponses(BDD.getAllQuestions(self.themeList))
    

        """Titre"""
        self.champ_titre=tk.Label(self,text="Projet Data-pursuit",padx="10",pady="10")
        self.champ_titre.config(font=("Courier", 44))
        self.champ_titre.pack(side="top")
        
        self.resultats=tk.Frame(self)
        self.resultats.pack(fill="both",expand="yes")
        self.affichageQuestions()

        


    def pageAcceuil(self):
        """Ronan"""


    def affichageQuestions(self):
        for widget in self.resultats.winfo_children():
            widget.forget()

        self.jeuFrame=tk.Frame(self.resultats)
        self.jeuFrame.pack(side="left",expand="yes",fill="both")

        #Affichage du tour en cours
        self.frameNumeroTour=tk.Frame(self.jeuFrame)
        self.frameNumeroTour.pack(fill="x")
        self.numero_tour=tk.Label(self.frameNumeroTour,text="Tour n°")
        self.numero_tour.pack(side="right")

        self.nomJoueurFrame=tk.Frame(self.jeuFrame)
        self.nomJoueurFrame.pack()

        self.nom_joueur=tk.Label(self.nomJoueurFrame,text='Nom Joueur')
        self.nom_joueur.pack()

        self.gameFrame=tk.Frame(self.jeuFrame)
        self.gameFrame.pack()

        self.chooseThemeLabel=tk.Label(self.gameFrame,text="Veuillez choisir un thème :")
        self.chooseThemeLabel.grid(row=0,column=0,pady=12)

        
        self.themeChoice=chooseTheme(self.themeList)
        print(self.themeChoice)

        for i in range(len(self.themeChoice)):
            tk.Button(self.gameFrame,text=self.themeChoice[i].libelle,command=partial(self.afficherQuestionReponses,self.themeChoice[i])).grid(row=1,column=i)





        self.jeuFrame2=tk.Frame(self.resultats,borderwidth="1",relief="solid",width=250)
        self.jeuFrame2.pack(side="right",expand="yes",fill="both")


    def afficherQuestionReponses(self,theme):
        for widget in self.gameFrame.winfo_children():
            widget.destroy()

        print(self.questionList)
        print(theme)
        tk.Label(self.gameFrame,text="Vouz avez choisi le thème {}".format(theme.libelle)).pack(pady=12)

        self.question,self.bonneReponse=get_question(theme.libelle,self.questionList)

        tk.Label(self.gameFrame,text=self.question.libelle).pack(pady=12)

        self.reponsesFrame=tk.Frame(self.gameFrame)
        self.reponsesFrame.pack()

        if len(self.question.reponses)>1:
            for i in range(len(self.question.reponses)):
                tk.Button(self.reponsesFrame,text=self.question.reponses[i].libelle,width=20,command=partial(self.recupAndCheckReponses,self.question.reponses[i])).grid(row=i%2,column=i//2)
        else :
            tk.Label(self.reponsesFrame,text=" Saisissez votre réponse",padx=12,pady=12).grid(row=0,column=0)
            self.reponseJoueur=tk.StringVar()
            self.reponseJoueurEntry=tk.Entry(self.reponsesFrame,textvariable=self.reponseJoueur)
            self.reponseJoueurEntry.grid(row=0,column=1)
            tk.Button(self.reponsesFrame,text="Valider",command=partial(self.recupAndCheckReponses,str(self.reponseJoueur.get()))).grid(row=0,column=3)




            
    def recupAndCheckReponses(self,reponseJoueur):
        if len(self.question.reponses)>1:
            if verif_reponse(reponseJoueur,self.bonneReponse,self.question.reponses)==True:
                for widget in self.reponsesFrame.winfo_children():
                    widget.destroy()
                tk.Label(self.reponsesFrame,text="Bravo :)").pack()
                print("coucou")
                tk.Button(self.reponsesFrame,text="Joueur suivant",command=self.affichageQuestions).pack()
            else:
                for widget in self.reponsesFrame.winfo_children():
                    widget.destroy()
                tk.Label(self.reponsesFrame,text="Dommage :(").pack()
                print("coucou")
                tk.Button(self.reponsesFrame,text="Joueur suivant",command=self.affichageQuestions).pack()
        else:
            if verif_reponse(str(self.reponseJoueur.get()),self.bonneReponse,self.question.reponses)==True:
                for widget in self.reponsesFrame.winfo_children():
                    widget.destroy()
                tk.Label(self.reponsesFrame,text="Bravo :)").pack()
                print("coucou")
                tk.Button(self.reponsesFrame,text="Joueur suivant",command=self.affichageQuestions).pack()
            else:
                for widget in self.reponsesFrame.winfo_children():
                    widget.destroy()
                tk.Label(self.reponsesFrame,text="Dommage :(").pack()
                print("coucou")
                tk.Button(self.reponsesFrame,text="Joueur suivant",command=self.affichageQuestions).pack()

            

        


        

app=Application()
app.mainloop()