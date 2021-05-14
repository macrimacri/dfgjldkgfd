import sqlite3 
class User:
    def __init__(self):
        self.username = " "
        self.password = " "

    def get_username(self):
        return self.username
    def set_username(self, username):
        self.username = username
    
    def get_password(self):
        return self.password
    def set_password(self, password):
        self.password = password

    def print(self):
        print(self.username, self.password)
    
    def verifyLogin(self):
        with sqlite3.connect("movies.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM Users WHERE Username = ? AND Password = ?")
        cursor.execute(find_user,[(self.username), (self.password)])
        results = cursor.fetchall()

        if results:
            return True
        else:
            return False
