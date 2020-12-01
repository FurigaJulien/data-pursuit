# from Fonctions import *
# from BDD import *
# from Application import *


# def dataPursuit():

#     nb_of_player=getNumberOfPlayer()
#     liste_joueur=getAndCreatePlayers(nb_of_player)
#     themeList=BDD.getAllTheme()
#     question_list=BDD.getAllResponses(BDD.getAllQuestions(BDD.getAllTheme()))


#     victory=False
#     testvar=False
#     tour=0
    
#     app=Application()
#     #Ajout du score 
#     for joueur in liste_joueur:
#         for theme in themeList:
#             joueur.score[theme]=False

#     while victory==False:
#         tour=tour+1
#         print("Tour n°"+str(tour))


#         for joueur in liste_joueur:
#             if victory!=True:
#                 print(joueur.prenom + " c'est ton tour")
#                 # Choix du thème
#                 app.affichageQuestions(tour,joueur)
#                 app.mainloop()


#                 #Vérification de la condition de victoire
#                 if testvar not in joueur.score.values():
#                     victory=True
#                     winner=joueur
#                     print("Bravo {}, tu es notre champion !".format(winner.prenom))
                    
    
# dataPursuit()