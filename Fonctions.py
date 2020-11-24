from Classes import Joueur
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

