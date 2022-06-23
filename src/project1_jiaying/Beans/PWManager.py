class PWManager:
        def __init__(self,pwd, description, URL, accnt,personID, id = 0):
                self.accnt=accnt
                self.id = id
                self.pwd = pwd
                self.description = description
                self.URL = URL
                self.personID=personID

        def __str__(self):
                return "URL: "+self.URL +" Password: "+self.pwd+" Description: "+self.description