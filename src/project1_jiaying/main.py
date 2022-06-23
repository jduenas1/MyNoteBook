from Utils.Secret import Secret
from Beans.Person import Person
from Beans.PersonData import PersonData
from Beans.PWManager import PWManager
from Beans.URLManager import URLManager
from Services.PersonService import PersonService
import mysql.connector

secret=Secret()
pw=secret.getPassword()
db=secret.getDataBase()
host=secret.getHost()
dbconnection = mysql.connector.connect(
    host=host,
    user="root",
    password=pw,
    database=db
)
personService=PersonService(dbconnection)

exit="-"
# person1= Person("pikapika",123456789,0,"pika","chu")
loginOn=None
# val= (0,person1.username,person1.pwd,person1.firstName,person1.lastName)
# personService.createPerson(val,dbCursor,dbconnection)

while exit != "exit":
    if (loginOn == "Invalid username or password" or loginOn ==None) and exit.find("exit")==-1:
        input1=input("Do you need to login or are you a new user? ").lower().strip()
        exit="exit" if "exit" in input1 else "-"
    if "new" in input1:
        username=input("Please enter a user name ")
        password=input("Please enter a password ")
        firstname=input("What is your first name ")
        lastname=input("What is your last name ")
        loginOn=personService.createPerson(Person(username,password,0,firstname,lastname))
    if "login" in input1:
        while (loginOn == "Invalid username or password" or loginOn ==None) and exit.find("exit")==-1:
            username=input("What is your user name? ").strip().lower()
            exit=username
            password=input("What is your password? ").strip()
            exit="exit" if "exit" in username+password.lower() else "-"
            if exit =="exit":
                continue
            loginOn=personService.auth(username,password)
    if loginOn != "Invalid username or password" and loginOn !=None and exit.find("exit")==-1:
        action=input("What would you like to do today? Password manager, url manager,  update account, or, delete account? ").lower().strip()
        if "update" in action and exit.find("exit")==-1:
            print("If you would like not to update something please put no")
            update=input("What is the new first name. ")
            loginOn.firstName=loginOn.firstName if "no" in update else update
            update=input("What is the new last name. ")
            loginOn.lastName=loginOn.lastName if "no" in update else update
            update=input("What is the new username. ")
            loginOn.username=loginOn.username if "no" in update else update
            update=input("What is the new password. ")
            loginOn.pwd=loginOn.pwd if "no" in update else update
            loginOn=personService.updatePerson(loginOn)
        if "delete" in action and exit.find("exit")==-1:
            personService.deletePerson(loginOn)
            loginOn=None
        exit="exit" if "exit" in action else "-"


