# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 01:41:20 2018

@author: Quinjan
"""
import sys
sys.path.append("..")
from PyQt5 import QtCore, QtGui, QtWidgets
from mainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.statusBar().setSizeGripEnabled(False)
        self.showSummary()
        self.pushButton.clicked.connect(self.showKitchen)
        self.pushButton_2.clicked.connect(self.showCold)
        self.pushButton_3.clicked.connect(self.showHard)
        self.pushButton_9.clicked.connect(self.showSummary)
        self.pushButton_5.clicked.connect(self.showKitchenSales)
        self.pushButton_4.clicked.connect(self.showColdSales)
        self.pushButton_6.clicked.connect(self.showHardSales)
        
    def hideAll(self):
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.pushButton_7.hide()
        self.tableView.hide()
        self.pushButton_8.hide()
        
    def showKitchen(self):
        self.hideAll()
        self.pushButton_7.show()
        self.tableView.show()
        self.label_3.setText("Kitchen Summary")
        
    def showCold(self):
        self.hideAll()
        self.pushButton_7.show()
        self.tableView.show()
        self.label_3.setText("Cold Drinks Summary")
        self.pushButton_7.setText("Add New Cold Drink")
    
    def showHard(self):
        self.hideAll()
        self.pushButton_7.show()
        self.tableView.show()
        self.label_3.setText("Hard Drinks Summary")
        self.pushButton_7.setText("Add New Hard Drink")
        
    def showSummary(self):
        self.hideAll()
        self.label_4.show()
        self.label_5.show()
        self.label_6.show()
        self.label_3.setText("Admin Summary")
        
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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())