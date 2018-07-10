class HelperLibrary:
    def list_to_html_table(self, data):
        table_html = "<table class='table table-bordered table-striped table-responsive'><tr><th>Email</th><th>Salt</th><th>Hashed</th></tr>{}</table>"""
        table_data = ""    
        for user in data:        
            table_data += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(user["email"],user["salt"],user["hashed"])
        return table_html.format(table_data)
    
                 
