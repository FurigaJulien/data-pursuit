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
        self.tourNumber=0
        self.nombreDeTour=0

        """Titre"""
        self.champ_titre=tk.Label(self,text="Projet Data-pursuit",padx="10",pady="10")
        self.champ_titre.config(font=("Courier", 44))
        self.champ_titre.pack(side="top")
        
        self.resultats=tk.Frame(self)

        self.resultats.pack(fill ="both", expand="yes")
        self.pageAcceuil()

        self.resultats.pack(fill="both",expand="yes")
        self.continueGame=True

        #Ajout du score 

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



    def choixDesNoms(self):
        self.nombre_joueur = self.varGr.get()
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
        self.liste_joueurs = [rouge, bleu, jaune, vert]
        for i in range(int(self.nombre_joueur)):
            self.champNom = tk.Entry(self.nomFrame, text = "Joueur :",textvariable = self.liste_joueurs[i], width=20, justify="center")
            self.champNom.pack(side='left', expand=1)
        #le bouton de validation
        self.BoutonValidation = tk.Button(self.resultats, text = "Valider",command=self.startPlaying, height=6, width=20, bd=2, bg="#dbdbdb")
        self.BoutonValidation.pack(side="bottom")

    def startPlaying(self):
        self.playerList=[]
        for i in range(int(self.nombre_joueur)):
            score={}
            joueur=Joueur(self.liste_joueurs[i].get(),score=score)
            self.playerList.append(joueur)

        for joueur in self.playerList:
            for theme in self.themeList:
                joueur.score[theme]=False

        self.affichageQuestions(self.tourNumber,self.playerList[0])





    """def affichageQuestions(self):"""
    def affichageQuestions(self,tourNumber,playerTurn):

        for widget in self.resultats.winfo_children():
            widget.forget()

        if self.continueGame==True:

            self.nombreDeTour=self.nombreDeTour+1
            self.jeuFrame2=tk.Frame(self.resultats,borderwidth="1",relief="solid",width=250)
            self.jeuFrame2.pack(side="right",expand="yes",fill="both")
            self.affichage_joueurs_scores(self.playerList)
            self.tourNumber=self.tourNumber+1
            self.jeuFrame=tk.Frame(self.resultats)
            self.jeuFrame.pack(side="left",expand="yes",fill="both")

            #Affichage du tour en cours
            self.frameNumeroTour=tk.Frame(self.jeuFrame)
            self.frameNumeroTour.pack(fill="x")
            self.numero_tour=tk.Label(self.frameNumeroTour,text="Tour n°{}".format(self.nombreDeTour))
            self.numero_tour.pack(side="right")

            self.nomJoueurFrame=tk.Frame(self.jeuFrame)
            self.nomJoueurFrame.pack()

            self.nom_joueur=tk.Label(self.nomJoueurFrame,text=playerTurn.prenom)
            self.nom_joueur.pack()

            self.gameFrame=tk.Frame(self.jeuFrame)
            self.gameFrame.pack()

            self.chooseThemeLabel=tk.Label(self.gameFrame,text="Veuillez choisir un thème :")
            self.chooseThemeLabel.grid(row=0,column=0,pady=12)

            
            self.themeChoice=chooseTheme(self.themeList)
            print(self.themeChoice)

            for i in range(len(self.themeChoice)):
                tk.Button(self.gameFrame,text=self.themeChoice[i].libelle,command=partial(self.afficherQuestionReponses,self.themeChoice[i])).grid(row=1,column=i)
        else:
            tk.Label(self.resultats,text="Bravo {}, tu remporte cette partie !".format(self.winner.prenom)).pack()


    def afficherQuestionReponses(self,theme):
        for widget in self.gameFrame.winfo_children():
            widget.destroy()

        print(self.questionList)
        self.actualTheme=theme
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
        nextPlayer=self.tourNumber%len(self.playerList)
        actualPlayer=(self.tourNumber-1)%len(self.playerList)
    
        if len(self.question.reponses)>1:
            if verif_reponse(reponseJoueur,self.bonneReponse,self.question.reponses)==True:
                for widget in self.reponsesFrame.winfo_children():
                    widget.destroy()
                tk.Label(self.reponsesFrame,text="Bravo :)").pack()
                
                self.playerList[actualPlayer].score[self.actualTheme]=True
                if False not in self.playerList[actualPlayer].score:
                    self.continueGame=False
                    self.winner=self.playerList[actualPlayer]
                nextPlayer=actualPlayer
                self.tourNumber=self.tourNumber-1
                tk.Button(self.reponsesFrame,text="Joueur Suivant",command=partial(self.affichageQuestions,self.tourNumber,self.playerList[nextPlayer])).pack()
            
              
            else:
                for widget in self.reponsesFrame.winfo_children():
                    widget.destroy()
                tk.Label(self.reponsesFrame,text="Dommage :(").pack()
                tk.Button(self.reponsesFrame,text="Joueur Suivant",command=partial(self.affichageQuestions,self.tourNumber,self.playerList[nextPlayer])).pack()

                
                
        else:
            if verif_reponse(str(self.reponseJoueur.get()),self.bonneReponse,self.question.reponses)==True:
                for widget in self.reponsesFrame.winfo_children():
                    widget.destroy()
                tk.Label(self.reponsesFrame,text="Bravo :)").pack()
                self.playerList[actualPlayer].score[self.actualTheme]=True
                if False not in self.playerList[actualPlayer].score:
                    self.continueGame=False
                    self.winner=self.playerList[actualPlayer]
                nextPlayer=actualPlayer
                self.tourNumber=self.tourNumber-1
                tk.Button(self.reponsesFrame,text="Joueur Suivant",command=partial(self.affichageQuestions,self.tourNumber,self.playerList[nextPlayer])).pack()
                
                
            else:
                for widget in self.reponsesFrame.winfo_children():
                    widget.destroy()
                tk.Label(self.reponsesFrame,text="Dommage :(").pack()
                tk.Button(self.reponsesFrame,text="Joueur Suivant",command=partial(self.affichageQuestions,self.tourNumber,self.playerList[nextPlayer])).pack()
                
            


    def affichage_joueurs_scores(self, liste_joueurs):
        self.frameScore = tk.Frame(self.jeuFrame2)
        self.frameScore.pack()
        tk.Label(self.frameScore,text="Scores :").pack()   

        #Boucle qui crée un bloc par joueur grâce à la liste de joueurs passée en paramètre de la fonction
        numero_de_joueur = 1
        for joueur in liste_joueurs:
            tk.Label(self.frameScore,text="Joueur : {}".format(joueur.prenom)).pack(pady=12)
            for theme in joueur.score.keys():
                tk.Label(self.frameScore,text = "Thème ={}".format(theme.libelle)).pack()
                print(id(joueur.score))
                if joueur.score[theme] == True:
                    tk.Label(self.frameScore,text="OK").pack()
                else:
                    tk.Label(self.frameScore,text="Pas OK").pack()
            numero_de_joueur += 1

            
def dataPursuit():

        app=Application()
        app.mainloop()


        
dataPursuit()


