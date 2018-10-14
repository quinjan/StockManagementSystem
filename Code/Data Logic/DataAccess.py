import sqlite3

class AccessData(object):
    
    
    def __init__(self):
        self.connection = sqlite3.connect('../Database/MainDB.db')
        self.dl = self.connection.cursor()