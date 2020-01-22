import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import data
import main
USERNAME = ''


class Ui_MainWindow_SignUp(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(795, 457)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(248, 248, 255)")
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)

        self.usern_label = QtWidgets.QLabel(self.centralwidget)
        self.usern_label.setGeometry(QtCore.QRect(190, 120, 100, 50))
        self.usern_label.setFont(font)
        self.usern_label.setObjectName("usern_label")

        self.passw_label = QtWidgets.QLabel(self.centralwidget)
        self.passw_label.setGeometry(QtCore.QRect(190, 200, 100, 50))
        self.passw_label.setFont(font)
        self.passw_label.setObjectName("passw_label")

        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setGeometry(QtCore.QRect(190, 160, 100, 50))
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")

        self.show_message = QtWidgets.QLabel(self.centralwidget)
        self.show_message.setGeometry(QtCore.QRect(170, 20, 521, 81))
        self.show_message.setFont(font)
        self.show_message.setStyleSheet("color: rgb(240, 128, 128);")
        self.show_message.setText("")
        self.show_message.setObjectName("show_message")

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)

        self.usern_text_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.usern_text_edit.setGeometry(QtCore.QRect(340, 130, 200, 30))
        self.usern_text_edit.setFont(font)
        self.usern_text_edit.setObjectName("usern_text_edit")

        self.email_text_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.email_text_edit.setGeometry(QtCore.QRect(340, 170, 200, 30))
        self.email_text_edit.setFont(font)
        self.email_text_edit.setObjectName("email_text_edit")

        self.passw_text_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.passw_text_edit.setGeometry(QtCore.QRect(340, 210, 200, 30))
        self.passw_text_edit.setObjectName("passw_text_edit")
        self.passw_text_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.signUp_btn = QtWidgets.QPushButton(self.centralwidget)
        self.signUp_btn.setGeometry(QtCore.QRect(320, 310, 110, 30))
        self.signUp_btn.setFont(font)
        self.signUp_btn.setObjectName("signUp_btn")
        self.signUp_btn.setStyleSheet("border: 1px solid rgb(0, 0, 0)")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("background-color: rgb(248, 248, 255)")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Регистрация"))
        self.usern_label.setText(_translate("MainWindow", "Логин"))
        self.passw_label.setText(_translate("MainWindow", "Пароль"))
        self.signUp_btn.setText(_translate("MainWindow", "Регистрация"))
        self.email_label.setText(_translate("MainWindow", "Email"))


class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow_SignUp):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.signUp_btn.clicked.connect(self.registration)

    def registration(self):
        res = data.sign_up(self.usern_text_edit.text(), self.email_text_edit.text(), self.passw_text_edit.text())
        if res:
            if 'secondAccount' in res:
                self.show_message.setText('Аккаунт с таким логином или почтой существует')
            elif 'lenError_user' in res:
                self.show_message.setText('Длина логина должна быть больше 3')
            elif 'lenError_email' in res:
                self.show_message.setText('Длина email должна быть больше 4')
            elif 'lenError_pass' in res:
                self.show_message.setText('Длина пароля должна быть больше 4')
            elif 'wrongEmail' in res:
                self.show_message.setText('Неправильный формат почты')
        else:
            USERNAME = self.usern_text_edit.text()
            self.close()
            self.show_main = main.MyWidget(USERNAME)
            self.show_main.show()
