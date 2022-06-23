from Beans.URLManager import URLManager
class URLManagerService:
    def __init__(self,dbconnection):
            self.dbCursor=dbconnection.cursor()
            self.dbconnection=dbconnection
            self.get = "select * from urlmanager where personID="
            self.post="insert into urlmanager (personID,url,descprtion) values (%s,%s,%s)"
            # self.put = "update person set user_login = %s,user_password=%s,first_name=%s,last_name=%s where ID="
            # self.delete = "delete from person where ID="
    
    def getURLsByPersonID(self,id):
        self.dbCursor.execute(self.get+str(id))
        url=self.dbCursor.fetchall()
        if url!=None:
            urls=[]
            for i in url:
                urls.append(URLManager(i[3],i[2],i[1],i[0]))
            return urls
        else:
            return url
    
    def createUrl(self,url):
        self.dbCursor.execute(self.post,(str(url.personID),url.URL,url.description))
        self.dbconnection.commit()
        print("URL has been saved")