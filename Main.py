from Fonctions import *
from BDD import *

"""def dataPursuit():

    nb_of_player=getNumberOfPlayer()
    liste_joueur=getAndCreatePlayers(nb_of_player)
    themeList=BDD.getAllTheme()
    question_list=BDD.getAllResponses(BDD.getAllQuestions(BDD.getAllTheme()))


    victory=False
    testvar=False
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

            question,reponse_attendue=get_question(themeChoosen,questionList)



            #Vérification de la réponse
            if verif_reponse(,reponse_attendue)==True:
                joueur.score[themeChoosen]=True



            #Vérification de la condition de victoire
            if testvar not in joueur.score:
                victory=True
                winner=joueur"""





themeList=BDD.getAllTheme()
question_list=BDD.getAllResponses(BDD.getAllQuestions(BDD.getAllTheme()))

themeChoosen=chooseTheme(themeList)

question,reponse_attendue=get_question(themeChoosen,question_list)