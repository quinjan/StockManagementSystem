import sys
sys.path.append("../")
from DataLogic.DataAccess import AccessData

class Users(object):
    
    def __init__(self):
        self.dataReader = AccessData()
        self.Username = []
        self.Password = []
        self.Firstname = []
        self.Lastname = []
        self.UserID = []
        
        
    def readUsers(self):
        data = self.dataReader.readUser()
        for data_out in data:
            self.UserID.append(data_out[0])
            self.Firstname.append(data_out[1])
            self.Lastname.append(data_out[2])
            self.Username.append(data_out[3])
            self.Password.append(data_out[4])
    
    def verifyUser(self, username, password):
        if username in self.Username:
            if password == self.Password[self.Username.index(username)]:
                return True
        else:
            return False
