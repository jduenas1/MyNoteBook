from Beans.Person import Person
class PersonService:
    def __init__(self,dbconnection):
            self.dbCursor=dbconnection.cursor()
            self.dbconnection=dbconnection
            self.post="insert into person (ID, user_login,user_password, first_name,last_name) values (%s,%s,%s,%s,%s)"
            self.get = "select * from person where "
            self.put = "update person set user_login = %s,user_password=%s,first_name=%s,last_name=%s where ID="
            self.delete = "delete from person where ID="
    
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
    
    def updatePerson(self,person):
        self.dbCursor.execute(self.put+str(person.id),(person.username,person.pwd,person.firstName,person.lastName))
        self.dbconnection.commit()
        user=self.getPersonByID(person.id)
        if user!=None:
            print("Update sucess")
            print(str(user)+" password: "+user.pwd)
            return user
        else:
            print("An error occured please try again")
            return self.getPersonByID(person.id)