import sqlite3

class AccessData(object):
    
    
    def __init__(self):
        self.connection = sqlite3.connect('../Database/MainDB.db')
        self.dl = self.connection.cursor()

    def readUser(self, username, password):
        self.dl.execute('SELECT * FROM "Users"')
        items = self.dl.fetchall()
        return items