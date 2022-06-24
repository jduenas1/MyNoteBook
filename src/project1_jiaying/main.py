from Utils.Secret import Secret
from Beans.Person import Person
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
        input1=input("Do you want to login or register an account? (login/register)").lower().strip()
        exit="exit" if "exit" in input1 else "-"
    if "register" in input1:
        username=input("Please enter a user name ")
        password=input("Please enter a password ")
        firstname=input("What is your first name ")
        lastname=input("What is your last name ")
        loginOn=personService.createPerson(Person(username,password,0,firstname,lastname))
        input1="loggedon"
    if "login" in input1:
        while (loginOn == "Invalid username or password" or loginOn ==None) and exit.find("exit")==-1:
            username=input("What is your user name? ").strip().lower()
            exit=username
            password=input("What is your password? ").strip()
            exit="exit" if "exit" in username+password.lower() else "-"
            if exit =="exit":
                continue
            loginOn=personService.auth(username,password)
            input1="loggedon"
    if loginOn != "Invalid username or password" and loginOn !=None and exit.find("exit")==-1:
        action=input("What would you like to do today? Password Manager, url Manager,  update account, or, delete account? ").lower().strip()
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
        if "url" in action and exit.find("exit")==-1:
            action=input("Do you want to add a URL or view all URLs")
            if "view" in action:
                urls=personService.getURLs(loginOn)
                if urls!=None:
                    for i in urls:
                        print(i)
                else:
                        print("no URLs stored")
            if "add" in action:
                url=URLManager(input("Please enter a description"),input("Please enter the URL"),loginOn.id)        
                personService.addURL(url)
        if "password" in action and exit.find("exit")==-1:
            action=input("Do you want to add a password or view all passwords")
            if "view" in action:
                pws=personService.getPasswords(loginOn)
                if pws!=None:
                    for i in pws:
                        print(i)
                else:
                    print("no passwords stored")
            if "add" in action:
                pw=PWManager(input("Please enter a password"),input("Please enter a description"),input("Please enter the URL"),input("Please enter the account"),loginOn.id)
                personService.addPW(pw)        
        if "delete" in action and exit.find("exit")==-1:
            personService.deletePerson(loginOn)
            loginOn=None
        exit="exit" if "exit" in action else "-"


