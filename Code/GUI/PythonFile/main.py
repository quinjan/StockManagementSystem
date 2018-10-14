import sys
sys.path.append("../../")
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from GUI.PythonFile.mainWindow import Ui_MainWindow
from GUI.PythonFile.LoginUI import Ui_LoginWindow
from GUI.PythonFile.AddWindow import Ui_Dialog

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
