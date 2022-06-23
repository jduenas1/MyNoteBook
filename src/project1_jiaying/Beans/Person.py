class Person:
        def __init__(self,username,pwd,id = 0,firstName = "NA", lastName = "NA"):
                self.firstName=firstName
                self.lastName=lastName
                self.username=username
                self.pwd=pwd
                self.id=id
        
        def __str__(self):
                return "First Name: "+self.firstName+" Last Name: "+self.lastName + " UserName: "+ self.username