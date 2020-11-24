from Classes import Joueur
import random

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


def getAndCreatePlayers(nb_joueur):

    """Fonction permettant de creer les joueurs et de retourner ces derniers stockés dans une liste"""
    listeJoueurs=[]
    for i in range(nb_joueur): 

        nom_joueur=input("Saisissez le nom du joueur {} : ".format(i+1))
        nom_joueur=str(nom_joueur)
        joueur=Joueur(nom_joueur)
        listeJoueurs.append(joueur)

    return listeJoueurs


def chooseTheme(themeList):
    """Fonctions permettant a l'utilisateur de choisir parmis 2 themes pris au hasard dans une liste de theme disponibles"""

    randomThemeChoice = random.choices(themeList, k=2)

    print("Vous avez le choix entre les deux thèmes suivant : \n Theme n°1 : {} \n Theme n°2 :{}".format(randomThemeChoice[0],randomThemeChoice[1]))

    #Selection du thème par l'utilisateur
    verif=False
    while verif==False:
        try:
            theme_selected=input("Selectionnez votre thème (1 ou 2) :")
            theme_selected=int(theme_selected)
            if theme_selected<1 or theme_selected>2:
                print("Le thème choisi doit être 1 ou 2")
            else:
                verif=True
        except:
            print("Veuillez saisir un chiffre ( 1 ou 2)")

    print("Vous avez choisi le thème : {}".format(randomThemeChoice[theme_selected-1]))

    return randomThemeChoice[theme_selected-1]

chooseTheme(["bleu","rouge","vert"])

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
        
