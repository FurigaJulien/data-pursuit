import mysql.connector
from Classes import Theme,Question,Reponses
import random
class BDD():


    @classmethod
    def connect(cls):
        cls.link = mysql.connector.connect(**{
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'database': 'data-pursuit'
            })
        cls.cursor=cls.link.cursor()

    @classmethod
    def close(cls):
        cls.cursor.close()
        cls.link.close()

    @classmethod
    def getAllTheme(cls):
        cls.connect()
        themeList=[]
        query="SELECT * FROM theme"
        listeColor=["#a2c7bf","#ff8b94","#6e2c35","#98ddb5","#00b1e7"]
        cls.cursor.execute(query)
        
        for row in cls.cursor.fetchall():
            id=int(row[0])
            libelle=str(row[1])
            color=random.choice(listeColor)
            listeColor.remove(color)
            theme=Theme(id,libelle,color)
            themeList.append(theme)
        cls.close()
        return themeList

    @classmethod
    def getAllQuestions(cls,themeList):
        cls.connect()
        
        query="SELECT * from questions where id_theme={}"
        questionDict={}
        for theme in themeList:

            cls.cursor.execute(query.format(theme.id))
            questionList=[]

            for row in cls.cursor.fetchall():
                id=int(row[0])
                libelle=str(row[1])
                difficulte=int(row[3])
                question=Question(id,libelle,theme,difficulte)
                questionList.append(question)
                
            questionDict[theme.libelle]=questionList
        cls.close()
        return questionDict

    @classmethod
    def getAllResponses(cls,questionDict):
        cls.connect()
        query="SELECT * FROM reponses where id_question={}"
        for cle in questionDict.keys():
            for question in questionDict[cle]:
                cls.cursor.execute(query.format(question.id))
                listeReponse=[]
                for row in cls.cursor.fetchall():
                    libelle=str(row[2])
                    valeur_reponse=int(row[3])
                    reponse=Reponses(question.id,libelle,valeur_reponse)
                    listeReponse.append(reponse)
                    question.reponses=listeReponse
                   


        cls.close()
        return questionDict



