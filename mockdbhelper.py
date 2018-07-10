
class MockDBHelper:
    def __init__(self):
        self.id = 0
        self.MOCK_USERS = [{"email": "test@example.com",
						    "salt": "8Fb23mMNHD5Zb8pr2qWA3PE9bH0=", 
						    "hashed":"1736f83698df3f8153c1fbd6ce2840f8aace4f200771a46672635374073cc876cf0aa6a31f780e576578f791b5555b50df46303f0c3a7f2d21f91aa1429ac22e"},
						    {"email":"bmahmood328@gmail.com",
						     "salt" : '',
						     "hashed": "4dff4ea340f0a823f15d3f4f01ab62eae0e5da579ccb851f8db9dfe84c58b2b37b89903a740e1ee172da793a6e79d560e5f7f9bd058a12a280433ed6fa46510a"}]
        
        self.MOCK_TABLES = []
        
    def add_table(self, tablename, username):
        self.id += 1
        self.MOCK_TABLES.append({"_id" : self.id, "number": tablename,"owner":username, "url": None})
        return self.id
            
    
    
    def get_tables(self,username):
        result = []
        for table in self.MOCK_TABLES:
            if table.get("owner") == username:
                result.append(table)            
        return result
    

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
            
            
            
