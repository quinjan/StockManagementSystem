from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(331, 151)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setSizeGripEnabled(False)
        LoginWindow.setModal(True)
        self.login_PushButton = QtWidgets.QPushButton(LoginWindow)
        self.login_PushButton.setGeometry(QtCore.QRect(170, 110, 75, 23))
        self.login_PushButton.setObjectName("login_PushButton")
        self.username_Label = QtWidgets.QLabel(LoginWindow)
        self.username_Label.setGeometry(QtCore.QRect(10, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.username_Label.setFont(font)
        self.username_Label.setObjectName("username_Label")
        self.password_Label = QtWidgets.QLabel(LoginWindow)
        self.password_Label.setGeometry(QtCore.QRect(10, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.password_Label.setFont(font)
        self.password_Label.setObjectName("password_Label")
        self.lineEdit = QtWidgets.QLineEdit(LoginWindow)
        self.lineEdit.setGeometry(QtCore.QRect(130, 30, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(LoginWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 70, 171, 20))
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.login_PushButton.setText(_translate("LoginWindow", "Login"))
        self.username_Label.setText(_translate("LoginWindow", "Username"))
        self.password_Label.setText(_translate("LoginWindow", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QDialog()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

