import sys
sys.path.append("../../")
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from GUI.PythonFile.mainWindow import Ui_MainWindow
from GUI.PythonFile.LoginUI import Ui_LoginWindow
from GUI.PythonFile.AddWindow import Ui_Dialog
from BusinessLogic.items import Items
from BusinessLogic.users import Users


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.statusBar().setSizeGripEnabled(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.lineEdit2.setValidator(QtGui.QIntValidator())
        
class LoginWindow(QtWidgets.QDialog, Ui_LoginWindow):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.login_PushButton.clicked.connect(self.verifyUser)
        self.dialog = MainWindow(self)
        self.users = Users()
        self.users.readUsers()
        
    def verifyUser(self):     
        if self.users.verifyUser(self.lineEdit.text(), self.lineEdit_2.text())  == True:
            QMessageBox.about(self, "Login", "User Logged In!")
            self.dialog.show()
            self.hide()
        else:
            QMessageBox.about(self, "Login", "Error Username or Password")

class addWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(addWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.lineEdit_3.setValidator(QtGui.QIntValidator())
        self.lineEdit_2.setValidator(QtGui.QDoubleValidator())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = LoginWindow()
    main.show()
    sys.exit(app.exec_())
