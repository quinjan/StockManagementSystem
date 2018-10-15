import sys
sys.path.append("../")
from DataLogic.DataAccess import AccessData


class Items(object):
    
    def __init__(self):
        self.dataReader = AccessData()
        self.FoodID = []
        self.Name = []
        self.Price = []
        self.Type = []
        self.Stock = []
        self.Sales = []
        
    def readItems(self):
        data = self.dataReader.readItems()
        for data_out in data:
            self.FoodID.append(data_out[0])
            self.Name.append(data_out[1])
            self.Price.append(data_out[2])
            self.Type.append(data_out[3])
            self.Stock.append(data_out[4])
            self.Sales.append(data_out[5])
    
    def showKitchenItems(self):
        data = self.dataReader.readKitchen()
        return data
    
    def showColdItems(self):
        data = self.dataReader.readCold()
        return data
    
    def showHardItems(self):
        data = self.dataReader.readHard()
        return data
    
    def writeKitchen(self,name,price,tayp,stock):
        self.dataReader.writeKitchen(name,price,tayp,stock)
        
    def deleteItem(self, index):
        self.dataReader.deleteItem(index)
        
    def readHardSales(self):
        data = self.dataReader.readHardSales()
        return data
    
    def readColdSales(self):
        data = self.dataReader.readColdSales()
        return data
    
    def readKitchenSales(self):
        data = self.dataReader.readKitchenSales()
        return data
        
    def writeNewSale(self, value, stock, name):
        self.dataReader.writeNewSale(value, stock, name)
    
    def countKitchen(self):
        count = self.dataReader.countKitchen()
        return count
    
    def countCold(self):
        count = self.dataReader.countCold()
        return count
    
    def countHard(self):
        count = self.dataReader.countHard()
        return count