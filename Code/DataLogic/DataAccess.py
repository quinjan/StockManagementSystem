import sqlite3

class AccessData(object):
    
    
    def __init__(self):
        self.connection = sqlite3.connect('../Database/MainDB.db')
        self.dl = self.connection.cursor()
        
    def readUser(self):
        self.dl.execute('SELECT * FROM Users')
        return self.dl.fetchall()
        
    def readItems(self):
        self.dl.execute('SELECT * FROM Items')
        return self.dl.fetchall()
    
    def readKitchen(self):
        self.items = self.dl.execute('SELECT * FROM Items WHERE Type = "Kitchen" ')
        return self.items
    
    def readCold(self):
        self.items = self.dl.execute('SELECT * FROM Items WHERE Type = "Cold" ')
        return self.items
