import mysql.connector
from Classes import Theme,Question,Reponses
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
        cls.cursor.execute(query)
        
        for row in cls.cursor.fetchall():
            id=int(row[0])
            libelle=str(row[1])
            theme=Theme(id,libelle)
            themeList.append(theme)
        cls.close()
        return themeList

    @classmethod
    def getAllQuestions(cls,themeList):
        cls.connect()
        
        query="SELECT * from questions where theme_question={}"
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



