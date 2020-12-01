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
            
            if i == 0:
                position=(0,0)
            if i == 1:
                position=(9,0)
            if i == 2:
                position=(9,10)
            if i == 3:
                position=(0,10)
            joueur=Joueur(self.liste_joueurs[i].get(),score=score,position=position)
            self.playerList.append(joueur)

        for joueur in self.playerList:
            for theme in self.themeList:
                joueur.score[theme]=0

        self.affichageQuestions(self.tourNumber,self.playerList[0])
        
        




    """def affichageQuestions(self):"""
    def affichageQuestions(self,tourNumber,playerTurn):

        for widget in self.resultats.winfo_children():
            widget.forget()

        if self.continueGame==True:

            
            self.plateau()
            self.nombreDeTour=self.nombreDeTour+1
            self.jeuFrame2=tk.Frame(self.resultats,borderwidth="1",relief="solid",width=250,height=1200)
            self.jeuFrame2.pack(side="right",expand="yes",fill="both")
            self.affichage_joueurs_scores(self.playerList)
            self.tourNumber=self.tourNumber+1
            self.jeuFrame=tk.Frame(self.resultats,width=250,height=1200)
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
            


            tk.Button(self.gameFrame,text="Lancer le dé",command=self.rollDice).grid(row=1,column=0)


        else:
            tk.Label(self.resultats,text="Bravo {}, tu remporte cette partie !".format(self.winner.prenom)).pack()
            #Appeler ici fonction de derniere question

    def rollDice(self):
        self.dice=random.choice([1,2,3,4,5,6])
        tk.Label(self.gameFrame,text=self.dice).grid(row=1,column=1)

       
        tk.Button(self.gameFrame,text="sens horaire",command=self.movePlayerRight).grid(row=2,column=0)
        tk.Button(self.gameFrame,text="sens anti horaire",command=self.movePlayerLeft).grid(row=2,column=1)


    def movePlayerRight(self):
        x=self.playerList[(self.tourNumber-1)%len(self.playerList)].position[0]
        y=self.playerList[(self.tourNumber-1)%len(self.playerList)].position[1]
        
        if x!=9 and x+self.dice<10 and y==0:
            x=x+self.dice
            self.playerList[(self.tourNumber-1)%len(self.playerList)].position=(x,y)
        elif x!=9 and x+self.dice>9 and y==0:
            x1=9-x
            x=9
            y=self.dice-x1
            self.playerList[(self.tourNumber-1)%len(self.playerList)].position=(x,y)
        elif x==9 and  y+self.dice<11:
            y=y+self.dice
            self.playerList[(self.tourNumber-1)%len(self.playerList)].position=(x,y)
        elif x==9 and x+self.dice>10:
            y1=10-y
            y=10
            x=x-(self.dice-y1)
            self.playerList[(self.tourNumber-1)%len(self.playerList)].position=(x,y)
        elif y==10 and x-self.dice>=0:
            x=x-self.dice
            self.playerList[(self.tourNumber-1)%len(self.playerList)].position=(x,y)
        elif x!=0 and x-self.dice<0 and y==10:
            x1=x
            x=0
            y=10-(self.dice-x1)
            self.playerList[(self.tourNumber-1)%len(self.playerList)].position=(x,y)
        elif x==0 and y-self.dice>=0:
            y=y-self.dice
            self.playerList[(self.tourNumber-1)%len(self.playerList)].position=(x,y)
        elif x==0 and y-self.dice<0:
            y1=y
            y=0
            x=self.dice-y1
            self.playerList[(self.tourNumber-1)%len(self.playerList)].position=(x,y)

        

        self.updatePlateau()
        self.afficherQuestionReponses(self.themeList[0])

        
   
        

    
    def movePlayerLeft(self):
    def movePlayerRight(self):
        x=self.playerList[(self.tourNumber-1)%len(self.playerList)].position[0]
        y=self.playerList[(self.tourNumber-1)%len(self.playerList)].position[1]
        
        if x!=9 and x-self.dice<10 and y==0:
            x=x+self.dice
            self.playerList[(self.tourNumber-1)%len(self.playerList)].position=(x,y)
        elif x!=9 and x+self.dice>9 and y==0:
            x1=9-x
            x=9
            y=self.dice-x1
            self.playerList[(self.tourNumber-1)%len(self.playerList)].position=(x,y)
        elif x==9 and  y+self.dice<11:
            y=y+self.dice
            self.playerList[(self.tourNumber-1)%len(self.playerList)].position=(x,y)
        elif x==9 and x+self.dice>10:
            y1=10-y
            y=10
            x=x-(self.dice-y1)
            self.playerList[(self.tourNumber-1)%len(self.playerList)].position=(x,y)
        elif y==10 and x-self.dice>=0:
            x=x-self.dice
            self.playerList[(self.tourNumber-1)%len(self.playerList)].position=(x,y)
        elif x!=0 and x-self.dice<0 and y==10:
            x1=x
            x=0
            y=10-(self.dice-x1)
            self.playerList[(self.tourNumber-1)%len(self.playerList)].position=(x,y)
        elif x==0 and y-self.dice>=0:
            y=y-self.dice
            self.playerList[(self.tourNumber-1)%len(self.playerList)].position=(x,y)
        elif x==0 and y-self.dice<0:
            y1=y
            y=0
            x=self.dice-y1 
            print("coucou")
            self.playerList[(self.tourNumber-1)%len(self.playerList)].position=(x,y)

        

        self.updatePlateau()
        self.afficherQuestionReponses(self.themeList[0])


        

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
                if len(self.question.reponses[i].libelle)>40 and len(self.question.reponses[i].libelle)<120 :
                    self.question.reponses[i].libelle=self.question.reponses[i].libelle[:40]+"\n"+self.question.reponses[i].libelle[41:]
                if len(self.question.reponses[i].libelle)>120 :
                    self.question.reponses[i].libelle=self.question.reponses[i].libelle[:40]+"\n"+self.question.reponses[i].libelle[41:80]+"\n"+self.question.reponses[i].libelle[81:]
   
                tk.Button(self.reponsesFrame,text=self.question.reponses[i].libelle,width=35,height=5,command=partial(self.recupAndCheckReponses,self.question.reponses[i])).grid(row=i%2,column=i//2)
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
                
                self.playerList[actualPlayer].score[self.actualTheme]=self.playerList[actualPlayer].score[self.actualTheme]+1
                #Verification condition de victoires
                if 0 not in self.playerList[actualPlayer].score.values() and 1 not in self.playerList[actualPlayer].score.values() and 2 not in self.playerList[actualPlayer].score.values() :
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
                self.playerList[actualPlayer].score[self.actualTheme]=self.playerList[actualPlayer].score[self.actualTheme]+1
                #Verification condition de victoires
                if 0 not in self.playerList[actualPlayer].score.values() and 1 not in self.playerList[actualPlayer].score.values() and 2 not in self.playerList[actualPlayer].score.values() :
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
        """Fonction qui gère l'affichage des scores de chaque joueur pour chaque thème"""
        #On crée le label titre de la frame de droite du jeu : 
        tk.Label(self.jeuFrame2,text="Scores :").pack()

        #On crée une liste de frames qui accueillera les frames des différents joueurs (taille variable) :
        liste_frames = []

        #On itère sur notre liste de joueur pour ajouter le bon nombre de frames dans une liste de frames :
        for joueur in liste_joueurs:
            liste_frames.append(tk.Frame(self.jeuFrame2))

        #On crée un numero de joueur qui commence à zéro et sera incrémenté pour prendre le bon prénom dans la liste d'objets joueurs.
        num_joueur = 0

        #On itère sur nos frames dans la liste afin de remplir chacune comme il faut :
        for frame in liste_frames :

            #on crée un label joueur :
            tk.Label(frame, text = "Joueur :").grid(row = 0, column = 0)
            #on crée un label pour le prénom du joueur pris dans la liste d'objets joueurs et dont la couleur correspond à l'attribut couleur de cet objet joueur :
            tk.Label(frame, text = liste_joueurs[num_joueur].prenom, fg = liste_joueurs[num_joueur].couleur,).grid(row = 0, column = 1)

            #On boucle sur les thèmes pour les afficher sous le nom du joueur et ce quel que soit le nombre de thèmes
            for theme in self.themeList :
                #On crée le label qui affichera le nom du thème pour le joueur en cours :
                tk.Label(frame, text = theme.libelle+" :").grid(row = 1+self.themeList.index(theme), column = 0)
                #On remplit une variable score avec le score de thème pour le thème sur lequel on itère et pour le joueur en cours 
                score = liste_joueurs[num_joueur].score[theme]
                #On vérifie si le score est suffisant pour valider le thème :
                if score > 2 :
                    tk.Label(frame,text="OK").grid(row = 1+0, column = 1)
                else :
                    tk.Label(frame,text="{}/3".format(str(score))).grid(row = 1+self.themeList.index(theme), column = 1)
            #On pack la frame pour le joueur et on peut passer à la création de la frame suivante ou sortir si tous les joueurs sont traités.
            frame.pack()
            
            #On incrémente la variable numéro de joueur pour passer au joueur suivant dans le prochain tour de boucle sur la liste de frames
            num_joueur += 1

    def plateau(self):
        self.plateauFrame=tk.Frame(self.resultats,borderwidth="1",relief="solid",width=400)
        self.plateauFrame.pack(side="bottom")
        tk.Label(self.plateauFrame,text="lancer le dé").pack()
        self.plateauJeu=tk.Frame(self.plateauFrame)
        self.plateauJeu.pack()
        listeColor=["Blue","white","red","green","yellow"]
        dictionnaireTheme={"Blue":[],"white":[],"red":[],"green":[],"yellow":[]}
        for i in range(10):
            color=random.choice(listeColor)
            dictionnaireTheme[color].append((0,i))
            tk.Frame(self.plateauJeu,width=50,height=50,borderwidth="1",relief="solid",bg=color).grid(row=0,column=i)
        for i in range(9):
            color=random.choice(listeColor)
            dictionnaireTheme[color].append((0,i))
            tk.Frame(self.plateauJeu,width=50,height=50,borderwidth="1",relief="solid",bg=color).grid(row=i+1,column=0)
        for i in range(9):
            color=random.choice(listeColor)
            dictionnaireTheme[color].append((0,i))
            tk.Frame(self.plateauJeu,width=50,height=50,borderwidth="1",relief="solid",bg=color).grid(row=i+1,column=9)
        for i in range(9):
            color=random.choice(listeColor)
            dictionnaireTheme[color].append([0,i])
            tk.Frame(self.plateauJeu,width=50,height=50,borderwidth="1",relief="solid",bg=color).grid(row=10,column=i+1)

        self.updatePlateau()



    def updatePlateau(self):
        for widget in self.plateauJeu.winfo_children():
                    if isinstance(widget, tk.Label):
                        widget.destroy()
    
        for player in self.playerList:
            tk.Label(self.plateauJeu,borderwidth="1",relief="solid",text=player.prenom).grid(row=player.position[1],column=player.position[0])
        
            
            
def dataPursuit():

        app=Application()
        app.mainloop()


        
dataPursuit()


