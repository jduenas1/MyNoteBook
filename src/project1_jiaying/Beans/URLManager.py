class URLManager:
        def __init__(self, description, URL, personID,id = 0):
                self.id = id
                self.description = description
                self.URL = URL
                self.personID=personID

        def __str__(self):
                return "URL: "+self.URL +" Description: "+self.description