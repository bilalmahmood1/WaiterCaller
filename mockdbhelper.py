import datetime

class MockDBHelper:
    def __init__(self):
        self.id_table = 1
        self.id_request = 1

        self.MOCK_USERS = [{"email": "test@example.com",
						    "salt": "8Fb23mMNHD5Zb8pr2qWA3PE9bH0=", 
						    "hashed":"1736f83698df3f8153c1fbd6ce2840f8aace4f200771a46672635374073cc876cf0aa6a31f780e576578f791b5555b50df46303f0c3a7f2d21f91aa1429ac22e"},
						    {"email":"bmahmood328@gmail.com",
						     "salt" : '',
						     "hashed": "4dff4ea340f0a823f15d3f4f01ab62eae0e5da579ccb851f8db9dfe84c58b2b37b89903a740e1ee172da793a6e79d560e5f7f9bd058a12a280433ed6fa46510a"}]
        
        self.MOCK_TABLES = [{"_id" : self.id_table, "number": 1,"owner":'test@example.com', "url": "Mockurl"}]
        self.MOCK_REQUESTS = [{"_id_request": self.id_request, "_id": self.id_table, "datetime": datetime.datetime.now(), "number": 1, "owner": 'test@example.com'}]
        



    def add_table(self, tablename, username):
        self.id_table += 1
        self.MOCK_TABLES.append({"_id" : self.id_table, "number": tablename,"owner":username, "url": None})
        return self.id_table
            
    
    def get_tables(self,username):
        result = []
        for table in self.MOCK_TABLES:
            if table.get("owner") == username:
                result.append(table)            
        return result
    
    def get_table_id(self,table_id):
        table_number = None
        for table in self.MOCK_TABLES:
            if table.get("_id") == table_id:
                return table
        return table_number 
        


    def delete_table(self, tableid):        
        for i, table in enumerate(self.MOCK_TABLES):
            if table.get("_id") == tableid:
                self.MOCK_TABLES.pop(i)
                break


    def update_table(self, tableid, new_url):
        for table in self.MOCK_TABLES:
            if table["_id"] == tableid:
                table["url"] = new_url
                break
            
        
    def get_user(self, email):
        for user in self.MOCK_USERS:
            if user["email"] == email:
                return user
        return None

    def add_user(self, email, salt, hashed):
        self.MOCK_USERS.append({"email":email,
								"salt": salt,
								"hashed": hashed})
            
            
    def add_request(self, tid, time, table_number, username):
        self.id_request += 1
        self.MOCK_REQUESTS.append({"_id_request": self.id_request,"_id":tid,"datetime":time, "number": table_number, "owner": username})
        return self.id_request
    
    def get_requests(self,username):
        result = []
        for request in self.MOCK_REQUESTS:
            if request.get("owner") == username:
                result.append(request)            
        return result
    

    def delete_request(self, requestid):        
        for i, request in enumerate(self.MOCK_REQUESTS):
            if request.get("_id_request") == requestid:
                self.MOCK_REQUESTS.pop(i)
                break
