from Beans.PWManager import PWManager
class PWManagerService:
    def __init__(self,dbconnection):
            self.dbCursor=dbconnection.cursor()
            self.dbconnection=dbconnection
            self.get = "select * from PWmanager where personID="
            self.post="insert into pwmanager (personID,passwrd,accnt,descprtion,URL) values (%s,%s,%s,%s,%s)"
            # self.put = "update person set user_login = %s,user_password=%s,first_name=%s,last_name=%s where ID="
            # self.delete = "delete from person where ID="
    
    def getPWsByPersonID(self,id):
        self.dbCursor.execute(self.get+str(id))
        pw=self.dbCursor.fetchall()
        if pw!=None:
            pws=[]
            for i in pw:
                pws.append(PWManager(i[2],i[4],i[5],i[3],i[1],i[0]))
            return pws
        else:
            return pw
            
    def createPW(self,pw):
        self.dbCursor.execute(self.post,(str(pw.personID),pw.pwd,pw.accnt,pw.description,pw.URL))
        self.dbconnection.commit()
        print("Password has been saved")