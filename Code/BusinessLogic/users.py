import sys
sys.path.append("../")
from DataLogic.DataAccess import AccessData

class Users(object):
    
    def __init__(self):
        self.dataReader = AccessData()
        self.userList = []
        
    def readUsers(self):
        data = 