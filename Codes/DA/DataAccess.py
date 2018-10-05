import sqlite3

class AccessData(object):
    
    
    def __init__(self):
        self.connection = sqlite3.connect('../DA/MainDB.db')
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
    
    def readCold(self):
        self.items = self.dl.execute('SELECT * FROM Items WHERE Type = "Cold" ')
        return self.items
    
    def readHard(self):
        self.items = self.dl.execute('SELECT * FROM Items WHERE Type = "Hard" ')
        return self.items
    
    def writeKitchen(self,name,price,tayp,stock):
        self.dl.execute("INSERT INTO Items (Name,Price,Type,Stock,Sales) values(?,?,?,?,0)",(name,price,tayp,stock))
        self.dl.execute("COMMIT")
    
    def countKitchen(self):
        self.dl.execute('SELECT COUNT(FoodID) FROM Items WHERE Type = "Kitchen"')
        self.count = self.dl.fetchone()[0]
        return self.count
    
    def countCold(self):
        self.dl.execute('SELECT COUNT(FoodID) FROM Items WHERE Type = "Cold"')
        self.count = self.dl.fetchone()[0]
        return self.count
    
    def countHard(self):
        self.dl.execute('SELECT COUNT(FoodID) FROM Items WHERE Type = "Hard"')
        self.count = self.dl.fetchone()[0]
        return self.count
    
    def deleteItem(self, index):
        self.dl.execute('DELETE FROM Items WHERE FoodID = %s' % (index))
        self.dl.execute("COMMIT")
        
    def readKitchenSales(self):
        self.items = self.dl.execute('SELECT Name, Sales, Stock FROM Items WHERE Type = "Kitchen" ')
        return self.items
    
    def readColdSales(self):
        self.items = self.dl.execute('SELECT Name, Sales FROM Items WHERE Type = "Cold" ')
        return self.items
    
    def readHardSales(self):
        self.items = self.dl.execute('SELECT Name, Sales FROM Items WHERE Type = "Hard" ')
        return self.items
    
    def writeNewSale(self, value, stock, name):
        self.dl.execute("UPDATE Items SET Sales = ?, Stock = ? WHERE Name = ?",(value, stock, name))
        self.dl.execute("COMMIT")
