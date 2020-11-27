from Fonctions import *
from BDD import *

def dataPursuit():

    nb_of_player=getNumberOfPlayer()
    liste_joueur=getAndCreatePlayers(nb_of_player)
    themeList=BDD.getAllTheme()
    questionList=BDD.getAllResponses(BDD.getAllQuestions)


    victory=False
    
    tour=0

    #Ajout du score 
    for joueur in liste_joueur:
        for theme in themeList:
            joueur.score[theme]=False

    while victory==False:
        tour=tour+1
        print("Tour n°"+str(tour))


        for joueur in liste_joueur:
            print(joueur.prenom + " c'est ton tour")
            # Choix du thème
            themeChoosen=chooseTheme(themeList)




            #Vérification de la réponse
            if verif_reponse()==True:
                joueur.score[themeChoosen]=True



            #Vérification de la condition de victoire
            if False not in joueur.score:
                victory=True
                winner=joueur
            



