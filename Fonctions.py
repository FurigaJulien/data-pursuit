from Classes import Joueur
import random
import unidecode as ud

def getNumberOfPlayer():
    """Fonction permettant de récuperer le nombre de joueur, puis de creer ses derniers et de les retourner sous forme de liste"""
    #Récupération de l'input saisie & Vérification de la valeur récupérée
    verif=False
    while verif==False:
        nb_joueur=input("Saisissez un nombre de joueur (entre 1 et 4) : ")
        try:
            nb_joueur=int(nb_joueur)
            if nb_joueur<1 or nb_joueur>4:
                print("Vous n'avez pas saisi un nombre de joueur valide")
            else:
                verif=True
        except:
            print("La valeur saisie doit être un chiffre compris en 1 et 4")

    return nb_joueur


# def getAndCreatePlayers(nb_joueur):

#     """Fonction permettant de creer les joueurs et de retourner ces derniers stockés dans une liste"""
#     listeJoueurs=[]
#     for i in range(nb_joueur): 
        
#         nom_joueur=input("Saisissez le nom du joueur {} : ".format(i+1))
#         nom_joueur=str(nom_joueur)
#         score={}
#         joueur=Joueur(nom_joueur,score=score)
        
#         listeJoueurs.append(joueur)

#     return listeJoueurs


def chooseTheme(themeList):
    """Fonctions permettant a l'utilisateur de choisir parmis 2 themes pris au hasard dans une liste de theme disponibles"""

    randomThemeChoice = random.choices(themeList, k=2)

    #print("Vous avez le choix entre les deux thèmes suivant : \n Theme n°1 : {} \n Theme n°2 :{}".format(randomThemeChoice[0].libelle,randomThemeChoice[1].libelle))

    #Selection du thème par l'utilisateur
    #verif=False
    #while verif==False:
        #try:
            #theme_selected=input("Selectionnez votre thème (1 ou 2) :")
            #theme_selected=int(theme_selected)
    #         if theme_selected<1 or theme_selected>2:
    #             print("Le thème choisi doit être 1 ou 2")
    #         else:
    #             verif=True
    #     except:
    #         print("Veuillez saisir un chiffre ( 1 ou 2)")

    # print("Vous avez choisi le thème : {}".format(randomThemeChoice[theme_selected-1]))
    return randomThemeChoice
  
  

def verif_reponse (reponse_choisie, reponse_attendue,reponses):
    """Comparer la réponse donnée à la réponse attendue et renvoyer True ou False selon qu'elle est juste ou pas."""
    
    if len(reponses)==1:
        #Toute les ponctuations qu'on va pouvoir ignorer :
        ponctuation_gerable = ('!','.',':','?',',',';','_')

        #Transformer la réponse attendue en string au cas où elle serait numérique:
        reponse_attendue = str(reponses[0].libelle)
        
        #Retrait des ponctuations :
        reponse_choisie = "".join(x for x in reponse_choisie if x not in ponctuation_gerable)
        reponse_attendue = "".join(x for x in reponse_attendue if x not in ponctuation_gerable)

        #Retrait des majuscules, espaces et accents :
        reponse_choisie = ud.unidecode(reponse_choisie.lower().strip())
        reponse_attendue = ud.unidecode(reponse_attendue.lower().strip())

    #Comparaison des deux strings nettoyés :
    if reponse_choisie == reponse_attendue:
        return True
    else :
        return False

    

def showPlayersScore(playerList):
    """Affichage du score des joueurs en direct"""
    print("Petit point sur les scores !")
    for player in playerList:
        print(player.prenom + " :")
        for cle in player.score.keys():
            if player.score[cle]==True:
                string="Validé"
            else:
                string="Pas encore validé"
            print("cle : "+string)
        

def get_question(theme, liste_question):
    """Fonction qui choisit une question en fonction du thème"""
    choix_question = liste_question[theme]
    question = random.choices(choix_question, k=1)[0]
    print(question.libelle)
    if len(question.reponses)>1:
        for i in range(len(question.reponses)):
            print('choix n°{}: {}'.format(i+1,question.reponses[i].libelle))
            if question.reponses[i].valeur_reponse == 1:
                reponse = question.reponses[i]
    else:
        reponse=question.reponses[0]
    choix_question.remove(question)
    liste_question[theme] = choix_question
    return question, reponse


def choisir_reponse (reponse):
    """Le joueur saisit la réponse à la question posée précedemment"""

    verif = False
    while verif == False:
        reponse_choisie = str(input(f"Quelle est votre réponse : "))
        if type(reponse_choisie) == str:
            if len(reponse) == 1:
                verif = True
                return reponse_choisie
            if len(reponse) > 1 and reponse_choisie.isnumeric():
                if int(reponse_choisie) >= 1 and int(reponse_choisie) <= len(reponse):
                    verif = True
                else: print(f"on souhaite que la réponse choisie soit entre 1 et {len(reponse)}")
            else : print("warning la réponse attendue est numérique, on souhaite que la réponse choisie soit entre 1 et {len(reponse)} ")

    return(reponse[int(reponse_choisie)-1])
