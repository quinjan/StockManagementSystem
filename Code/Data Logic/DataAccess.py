import sqlite3

class AccessData(object):
    
    
    def __init__(self):
        self.connection = sqlite3.connect('../Database/MainDB.db')
        self.dl = self.connection.cursor()

    def readUser(self, username, password):
        self.dl.execute('SELECT * FROM "Users" WHERE "Username"="%s" AND "Password"="%s"' % (username, password))
        if self.dl.fetchone() is not None:
            return True
        else:
            return False
        
    def readAllItems(self):
        self.dl.execute('SELECT * FROM Items')
        self.items = self.dl.fetchall()
        return self.items
    
    def readKitchen(self):
        self.items = self.dl.execute('SELECT * FROM Items WHERE Type = "Kitchen" ')
        return self.items    