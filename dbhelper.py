import pymongo
from bson.objectid import ObjectId

DATABASE = "waitercaller"

class DBHelper:
    def __init__(self):
        client = pymongo.MongoClient()
        self.db = client[DATABASE]   
    def get_user(self, email):
        
        return self.db.users.find_one({"email": email})

    def add_user(self, email, salt, hashed):
        	self.db.users.insert({"email":email, "salt": salt, "hashed": hashed})
        
    def add_table(self, tablename, username):
        _id = self.db.tables.insert({"number": tablename,"owner":username})
        return str(_id)
            
    def update_table(self, tableid, new_url):
        self.db.tables.update({"_id":ObjectId(tableid)}, {"$set" : {"url": new_url}})
    	
    def get_tables(self,username):
        return list(self.db.tables.find({"owner":username}))
  
    def get_table_id(self,table_id):
        return self.db.tables.find_one({"_id":ObjectId(table_id)})
 
    def delete_table(self, tableid):    
        self.db.tables.remove({"_id":ObjectId(tableid)})

    def add_request(self, table_id, time, table_number, username):
        request_id = self.db.requests.insert({"table_id":table_id,"datetime":time, "number": table_number, "owner": username})
        return str(request_id)
    
    def get_requests(self,username):
        return list(self.db.requests.find({"owner": username}))

    def delete_request(self, requestid):   
        self.db.requests.remove({"_id":ObjectId(requestid)})
