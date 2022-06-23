from Beans.PWManager import PWManager
class PWManagerService:
    def __init__(self,dbconnection):
            self.dbCursor=dbconnection.cursor()
            self.dbconnection=dbconnection
            self.get = "select * from PWmanager where personID="
            # self.post="insert into urlmanager (ID, url,descprtion) values (%s,%s,%s)"
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