class Joueur():

    """Création de la classe joueur"""

    def __init__(self, prenom, score, couleur):
        self.prenom=prenom
        self.score=score
        self.couleur=couleur
        # Le score sera stocké dans un dictionnaire, ou les clés seront tout les thèmes, récupéré en BDD, et ou la valeur sera :
        # True : Le joueur a déja répondu bon a une question de ce thème, il possède donc le "camembert"
        # False : Le joueur n'a pas encore répondu bon a une question de ce thème, il ne possède pas encore le camembert
        # On aura également une clé ajouté qui sera FINAL_QUESTION=False, et qui sera utilisé en condition de victoire.

class Theme():
    
    def __init__(self,id,libelle):
        self.id=id
        self.libelle=libelle

    def __repr__(self):
        return self.libelle


class Question():

    def __init__(self,id,libelle,theme,difficulte,reponses=[]):
        self.id=id
        self.libelle=libelle
        self.theme=theme
        self.difficulte=difficulte
        self.reponses=reponses

    def __repr__(self):
        return self.libelle
class Reponses():

    def __init__(self,id_question,libelle,valeur_reponse):
        self.id_question=id_question
        self.libelle=libelle
        self.valeur_reponse=valeur_reponse

    def __repr__(self):
        return self.libelle