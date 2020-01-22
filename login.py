import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import data
import signup
import main
USERNAME = ''


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(795, 457)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usern_label = QtWidgets.QLabel(self.centralwidget)
        self.usern_label.setGeometry(QtCore.QRect(190, 122, 100, 50))
        self.centralwidget.setStyleSheet("background-color: rgb(248, 248, 255)")

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)

        self.usern_label.setFont(font)
        self.usern_label.setObjectName("usern_label")
        self.passw_label = QtWidgets.QLabel(self.centralwidget)
        self.passw_label.setGeometry(QtCore.QRect(190, 180, 100, 50))
        self.passw_label.setFont(font)
        self.passw_label.setObjectName("passw_label")

        self.show_message = QtWidgets.QLabel(self.centralwidget)
        self.show_message.setGeometry(QtCore.QRect(190, 40, 371, 51))
        self.show_message.setFont(font)
        self.show_message.setStyleSheet("color: rgb(240, 128, 128);")
        self.show_message.setText("")
        self.show_message.setObjectName("show_message")

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)

        self.usern_text_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.usern_text_edit.setGeometry(QtCore.QRect(340, 122, 200, 30))
        self.usern_text_edit.setFont(font)
        self.usern_text_edit.setObjectName("usern_text_edit")

        self.passw_text_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.passw_text_edit.setGeometry(QtCore.QRect(340, 180, 200, 30))
        self.passw_text_edit.setObjectName("passw_text_edit")
        self.passw_text_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(330, 270, 110, 30))
        self.login_btn.setFont(font)
        self.login_btn.setObjectName("login_btn")

        self.signUp_btn = QtWidgets.QPushButton(self.centralwidget)
        self.signUp_btn.setGeometry(QtCore.QRect(450, 270, 110, 30))
        self.signUp_btn.setFont(font)
        self.signUp_btn.setObjectName("signUp_btn")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("background-color: rgb(248, 248, 255)")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Авторизация"))
        self.usern_label.setText(_translate("MainWindow", "Логин"))
        self.passw_label.setText(_translate("MainWindow", "Пароль"))
        self.login_btn.setText(_translate("MainWindow", "Войти"))
        self.signUp_btn.setText(_translate("MainWindow", "Регистрация"))


class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.login_btn.clicked.connect(self.authorization)
        self.signUp_btn.clicked.connect(self.sign_up_show)

    def authorization(self):
        res = data.login(self.usern_text_edit.text(), self.passw_text_edit.text())
        if res:
            if res == 'emptyString':
                self.show_message.setText('Пустые строки')
            elif res == 'unknownLogin':
                self.show_message.setText('Неизвестный логин')
            else:
                self.show_message.setText('Неправильный пароль')
        else:
            USERNAME = self.usern_text_edit.text()
            self.close()
            self.show_main = main.MyWidget(USERNAME)
            self.show_main.show()

    def sign_up_show(self):
        # вызов окна регистрации
        self.close()
        self.show_sign_up = signup.MyWidget()
        self.show_sign_up.show()


app = QtWidgets.QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

