from Beans.Person import Person
class PersonService:
    def __init__(self,dbconnection):
            self.dbCursor=dbconnection.cursor()
            self.dbconnection=dbconnection
            self.post="insert into person (ID, user_login,user_password, first_name,last_name) values (%s,%s,%s,%s,%s)"
            self.get = "select * from person where "
            self.put = ""
            self.delete = "delete from person where ID="
    # post ="insert into person (ID, user_login,user_password, first_name,last_name) values (%s,%s,%s,%s,%s)"
    # get = "select * from person where user_login='"
    # put = ""
    # delete = "delete from person where ID="
    # val= (0,person1.username,person1.pwd,person1.firstName,person1.lastName)
    
    def getPersonByID(self,id):
        self.dbCursor.execute(self.get+"ID="+str(id))
        user=self.dbCursor.fetchone()
        if user!=None:
            user=Person(user[1],user[2],user[0],user[3],user[4])
            return user
        else:
            return user            

    def getPersonByUsername(self,username):
        self.dbCursor.execute(self.get+"user_login='"+username+"'")
        user=self.dbCursor.fetchone()
        if user!=None:
            user=Person(user[1],user[2],user[0],user[3],user[4])
            return user
        else:
            return user    

    def createPerson(self,person):
        self.dbCursor.execute(self.post,(str(person.id),person.username,person.pwd,person.firstName,person.lastName))
        self.dbconnection.commit()
        user=self.getPersonByID(self.dbCursor.lastrowid)
        if user!=None:
            print("Welcome "+user.firstName+" "+user.lastName)
            return user
        else:
            print("An error occured please try again")
            return user
    
    def deletePerson(self,person):
        self.dbCursor.execute(self.delete+str(person.id))
        self.dbconnection.commit()
        print("Profile was deleted")

    def auth(self,username,password):
        user=self.getPersonByUsername(username)
        if user!=None and user.pwd==password:
            print("Welcome "+user.firstName+" "+user.lastName)
            return user
        else:
            print("Invalid username or password")
            return user 
    
    def updatePerson(self):
        print("updated profile")