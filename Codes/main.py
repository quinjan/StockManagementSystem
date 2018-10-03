import sys
from DA.DataAccess import AccessData
from PyQt5 import QtCore, QtGui, QtWidgets
from UI.LoginUI import Ui_LoginWindow
from PyQt5.QtWidgets import QMessageBox
from UI.mainWindow import Ui_MainWindow
from UI.AddWindow import Ui_Dialog

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.statusBar().setSizeGripEnabled(False)
        self.addDialog = addWindow(self)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.data = AccessData()
        self.showSummary()
        self.pushButton.clicked.connect(self.showKitchen)
        self.pushButton_2.clicked.connect(self.showCold)
        self.pushButton_3.clicked.connect(self.showHard)
        self.pushButton_9.clicked.connect(self.showSummary)
        self.pushButton_5.clicked.connect(self.showKitchenSales)
        self.pushButton_4.clicked.connect(self.showColdSales)
        self.pushButton_6.clicked.connect(self.showHardSales)
        self.pushButton_7.clicked.connect(self.addDialog.show)
        self.pushButton_10.clicked.connect(self.delete)
        
    
    
    def hideAll(self):
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.pushButton_7.hide()
        self.tableWidget.hide()
        self.pushButton_8.hide()
        self.pushButton_10.hide()
        
    def showKitchen(self):
        self.hideAll()
        self.pushButton_7.show()
        self.pushButton_10.show()
        self.tableWidget.show()
        self.label_3.setText("Kitchen Summary")
        self.readKitchen()
        self.addDialog.setWindowTitle(self.label_3.text())
        self.flag = "Kitchen"
        
    def showCold(self):
        self.hideAll()
        self.pushButton_7.show()
        self.pushButton_10.show()
        self.tableWidget.show()
        self.label_3.setText("Cold Drinks Summary")
        self.pushButton_7.setText("Add New Cold Drink")
        self.readCold()
        self.addDialog.setWindowTitle(self.label_3.text())
        self.flag = "Cold"
    
    def showHard(self):
        self.hideAll()
        self.pushButton_7.show()
        self.pushButton_10.show()
        self.tableWidget.show()
        self.label_3.setText("Hard Drinks Summary")
        self.pushButton_7.setText("Add New Hard Drink")
        self.readHard()
        self.addDialog.setWindowTitle(self.label_3.text())
        self.flag = "Hard"
        
    def showSummary(self):
        self.hideAll()
        self.label_4.show()
        self.label_5.show()
        self.label_6.show()
        self.label_3.setText("Admin Summary")
        self.label_4.setText("Kitchen: " + str(self.data.countKitchen()))
        self.label_5.setText("Cold Drink: " + str(self.data.countCold()))
        self.label_6.setText("Hard Drink: " + str(self.data.countHard()))
        
    def showKitchenSales(self):
        self.hideAll()
        self.label_4.show()
        self.label_5.show()
        self.label_4.setText("Item: ")
        self.label_5.setText("Quantity: ")
        self.label_3.setText("Kitchen Sales")
        self.pushButton_8.show()

    
    def showColdSales(self):
        self.hideAll()
        self.label_4.show()
        self.label_5.show()
        self.label_4.setText("Item: ")
        self.label_5.setText("Quantity: ")
        self.label_3.setText("Cold Drink Sales")
        self.pushButton_8.show()
        
    def showHardSales(self):
        self.hideAll()
        self.label_4.show()
        self.label_5.show()
        self.label_4.setText("Item: ")
        self.label_5.setText("Quantity: ")
        self.label_3.setText("Hard Drink Sales")
        self.pushButton_8.show()
        
    def readKitchen(self):
        self.dataRead = self.data.readKitchen()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["FOOD ID", "NAME", "PRICE", "TYPE", "STOCK"])
        for row, form in enumerate(self.dataRead):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
    
    def readCold(self):
        self.dataRead = self.data.readCold()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["FOOD ID", "NAME", "PRICE", "TYPE", "STOCK"])
        for row, form in enumerate(self.dataRead):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
    
    def readHard(self):
        self.dataRead = self.data.readHard()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["FOOD ID", "NAME", "PRICE", "TYPE", "STOCK"])
        for row, form in enumerate(self.dataRead):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
    
    def delete(self):
        self.item = 0
        if self.tableWidget.currentRow() >= 0:
            self.item = int(self.tableWidget.item(self.tableWidget.currentRow(),0).text())
        self.data.deleteItem(self.item)
        if (self.flag == "Kitchen"):
            self.readKitchen()
        elif (self.flag == "Cold"):
            self.readCold()
        else:
            self.readHard()

class LoginWindow(QtWidgets.QDialog, Ui_LoginWindow):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.data = AccessData()
        self.login_PushButton.clicked.connect(self.verifyUser)
        self.dialog = MainWindow(self)
        
    def verifyUser(self):
        if self.data.readUser(self.lineEdit.text(), self.lineEdit_2.text()):
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
        self.data = AccessData()
        self.pushButton.clicked.connect(self.write)
        
    def write(self):
        self.data.writeKitchen(self.lineEdit.text(),float(self.lineEdit_2.text()),self.parent().flag,int(self.lineEdit_3.text()))
        if (self.parent().flag == "Kitchen"):
            self.parent().readKitchen()
        elif (self.parent().flag == "Cold"):
            self.parent().readCold()
        else:
            self.parent().readHard()
        QMessageBox.about(self, self.parent().flag, "Add Successful!")
        self.hide()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = LoginWindow()
    main.show()
    sys.exit(app.exec_())