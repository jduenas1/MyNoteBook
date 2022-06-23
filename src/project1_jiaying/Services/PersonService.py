from Beans.Person import Person
class PersonService:
    post ="insert into person (ID, user_login,user_password, first_name,last_name) values (%s,%s,%s,%s,%s)"
    get = ""
    put = ""
    delete = ""
    def createPerson(self,val,dbCursor,dbconnection):
        dbCursor.execute(PersonService.post,val)
        dbconnection.commit()
        print(val)
    
    def deletePerson(self,person):
        print("delete")

    def auth(self,username,password):
        print("Welcome ")
        if password=="123456789" and username=="jiaying":
            return 0
        else:
            return "Invalid username or password" 

    def getPersonByID(self):
        print("get person by id")
    
    def updatePerson(self):
        print("updated profile")