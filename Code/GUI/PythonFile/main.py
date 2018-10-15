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
        self.addDialog = addWindow(self)
        self.Items = Items()
        self.Items.readItems()
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
        self.pushButton_8.clicked.connect(self.addSales)
    
    def hideAll(self):
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.pushButton_7.hide()
        self.tableWidget.hide()
        self.pushButton_8.hide()
        self.pushButton_10.hide()
        self.lineEdit.hide()
        self.lineEdit2.hide()
        self.comboBox.hide()
        
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
        self.label_4.setText("Kitchen: " + str(self.Items.countKitchen()))
        self.label_5.setText("Cold Drink: " + str(self.Items.countCold()))
        self.label_6.setText("Hard Drink: " + str(self.Items.countHard()))
    
    def showKitchenSales(self):
        self.hideAll()
        self.label_4.show()
        self.label_5.show()
        self.label_4.setText("Item: ")
        self.label_5.setText("Quantity: ")
        self.label_3.setText("Kitchen Sales")
        self.pushButton_8.show()
        self.lineEdit2.show()
        self.lineEdit2.clear()
        self.comboBox.show()
        self.readSalesKitchen()

    
    def showColdSales(self):
        self.hideAll()
        self.label_4.show()
        self.label_5.show()
        self.label_4.setText("Item: ")
        self.label_5.setText("Quantity: ")
        self.label_3.setText("Cold Drink Sales")
        self.pushButton_8.show()
        self.lineEdit2.show()
        self.lineEdit2.clear()
        self.comboBox.show()
        self.readSalesCold()
        
    def showHardSales(self):
        self.hideAll()
        self.label_4.show()
        self.label_5.show()
        self.label_4.setText("Item: ")
        self.label_5.setText("Quantity: ")
        self.label_3.setText("Hard Drink Sales")
        self.pushButton_8.show()
        self.lineEdit2.show()
        self.lineEdit2.clear()
        self.comboBox.show()
        self.readSalesHard()
        
    def readKitchen(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["FOOD ID", "NAME", "PRICE", "TYPE", "STOCK"])
        for row, form in enumerate(self.Items.showKitchenItems()):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
    
    def readCold(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["FOOD ID", "NAME", "PRICE", "TYPE", "STOCK"])
        for row, form in enumerate(self.Items.showColdItems()):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
    
    def readHard(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["FOOD ID", "NAME", "PRICE", "TYPE", "STOCK"])
        for row, form in enumerate(self.Items.showHardItems()):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
    
    def delete(self):
        self.item = 0
        if self.tableWidget.currentRow() >= 0:
            self.item = int(self.tableWidget.item(self.tableWidget.currentRow(),0).text())
        self.Items.deleteItem(self.item)
        if (self.flag == "Kitchen"):
            self.readKitchen()
        elif (self.flag == "Cold"):
            self.readCold()
        else:
            self.readHard()
            
    def readSalesHard(self):
        self.comboBox.clear()
        self.mylist = [row[0] for row in self.Items.readHardSales()]
        self.mylistSales = [row[1] for row in self.Items.readHardSales()]
        self.mylistStock = [row[2] for row in self.Items.readHardSales()]
        self.comboBox.addItems(self.mylist)
        self.flag = "Hard"
        print(self.mylistSales)

    def readSalesCold(self):
        self.comboBox.clear()
        self.mylist = [row[0] for row in self.Items.readColdSales()]
        self.mylistSales = [row[1] for row in self.Items.readColdSales()]
        self.mylistStock = [row[2] for row in self.Items.readColdSales()]
        self.comboBox.addItems(self.mylist)
        self.flag = "Cold"
        print(self.mylistSales)
        
    def readSalesKitchen(self):
        self.comboBox.clear()
        self.mylist = [row[0] for row in self.Items.readKitchenSales()]
        self.mylistSales = [row[1] for row in self.Items.readKitchenSales()]
        self.mylistStock = [row[2] for row in self.Items.readKitchenSales()]
        self.comboBox.addItems(self.mylist)
        self.flag = "Kitchen"
        print(self.mylistStock)
        
    def addSales(self):
        index = self.comboBox.currentIndex()
        self.mylistSales[index] += int(self.lineEdit2.text())
        self.mylistStock[index] -= int(self.lineEdit2.text())
        print(self.mylistStock[index])
        self.Items.writeNewSale(self.mylistSales[index], self.mylistStock[index], self.comboBox.currentText())
        QMessageBox.about(self, "Sales", "Added " + self.lineEdit2.text() + " Sales!")
        
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
