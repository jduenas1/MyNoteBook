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
person1= Person("pikapika",123456789,0,"pika","chu")

val= (0,person1.username,person1.pwd,person1.firstName,person1.lastName)
personService.createPerson(val,dbCursor,dbconnection)
