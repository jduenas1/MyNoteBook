from Beans.URLManager import URLManager
class URLManagerService:
    def __init__(self,dbconnection):
            self.dbCursor=dbconnection.cursor()
            self.dbconnection=dbconnection
            # self.post="insert into urlmanager (ID, url,descprtion) values (%s,%s,%s)"
            # self.get = "select * from urlmanager where "
            # self.put = "update person set user_login = %s,user_password=%s,first_name=%s,last_name=%s where ID="
            # self.delete = "delete from person where ID="