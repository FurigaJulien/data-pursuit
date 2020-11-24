class Joueur():

    """Création de la classe joueur"""

    def __init__(self,prenom,score={}):
        self.prenom=prenom
        self.score=score
        # Le score sera stocké dans un dictionnaire, ou les clés seront tout les thèmes, récupéré en BDD, et ou la valeur sera :
        # True : Le joueur a déja répondu bon a une question de ce thème, il possède donc le "camembert"
        # False : Le joueur n'a pas encore répondu bon a une question de ce thème, il ne possède pas encore le camembert
        # On aura également une clé ajouté qui sera FINAL_QUESTION=False, et qui sera utilisé en condition de victoire.