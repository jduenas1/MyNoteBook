from Utils.Secret import Secret
from Beans.Person import Person
from Beans.PersonData import PersonData
from Beans.PWManager import PWManager
from Beans.URLManager import URLManager
from Services.PersonService import PersonService
import mysql.connector

personService=PersonService()
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

dbCursor=dbconnection.cursor()
exit=None
# person1= Person("pikapika",123456789,0,"pika","chu")
loginOn=None
# val= (0,person1.username,person1.pwd,person1.firstName,person1.lastName)
# personService.createPerson(val,dbCursor,dbconnection)

while exit != "exit":
    if loginOn == "Invalid username or password" or loginOn ==None:
        input1=input("Do you need to login or are you a new user")
    if "exit" in input1.lower():
        exit="exit"
    if "login" in input1.lower():
        while (loginOn == "Invalid username or password" or loginOn ==None) and exit != "exit":
            username=input("What is your user name?").strip().lower()
            password=input("What is your password?").strip()
            loginOn=personService.auth(username,password)
            print(loginOn)
    if loginOn != "Invalid username or password" and loginOn !=None and exit != "exit":
        action=input("What would you like to do today? Retrieve passwords or saved urls?")       


