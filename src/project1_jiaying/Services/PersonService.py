from Beans.Person import Person
class PersonService:
    post ="insert into person (ID, user_login,user_password, first_name,last_name) values (%s,%s,%s,%s,%s)"
    def createPerson(self,val,dbCursor,dbconnection):
        dbCursor.execute(PersonService.post,val)
        dbconnection.commit()
        print(val)
    
    def deletePerson(person):
        print("delete")
