import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import database
import signup


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 457)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usern_label = QtWidgets.QLabel(self.centralwidget)
        self.usern_label.setGeometry(QtCore.QRect(190, 122, 100, 50))

        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)

        self.usern_label.setFont(font)
        self.usern_label.setObjectName("usern_label")
        self.passw_label = QtWidgets.QLabel(self.centralwidget)
        self.passw_label.setGeometry(QtCore.QRect(190, 180, 100, 50))
        self.passw_label.setFont(font)
        self.passw_label.setObjectName("passw_label")

        self.show_message = QtWidgets.QLabel(self.centralwidget)
        self.show_message.setGeometry(QtCore.QRect(190, 40, 351, 51))
        self.show_message.setFont(font)
        self.show_message.setText("")
        self.show_message.setObjectName("show_message")

        font = QtGui.QFont()
        font.setFamily("Georgia")
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
        self.login_btn.setGeometry(QtCore.QRect(340, 270, 90, 30))
        self.login_btn.setFont(font)

        self.login_btn.setObjectName("login_btn")
        self.signUp_btn = QtWidgets.QPushButton(self.centralwidget)
        self.signUp_btn.setGeometry(QtCore.QRect(450, 270, 90, 30))
        self.signUp_btn.setFont(font)
        self.signUp_btn.setObjectName("signUp_btn")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.usern_label.setText(_translate("MainWindow", "Username"))
        self.passw_label.setText(_translate("MainWindow", "Password"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.signUp_btn.setText(_translate("MainWindow", "Sign Up"))


class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.login_btn.clicked.connect(self.authorization)
        self.signUp_btn.clicked.connect(self.sign_up_show)

    def authorization(self):
        res = database.login(self.usern_text_edit.text(), self.passw_text_edit.text())
        if res:
            if res == 'unknownLogin':
                self.show_message.setText('Неизвестный логин')
            else:
                self.show_message.setText('Неправильный пароль')
        else:
            pass

    def sign_up_show(self):
        self.close()
        self.a = signup.MyWidget()
        self.a.show()


app = QtWidgets.QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

