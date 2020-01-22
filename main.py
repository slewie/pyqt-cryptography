import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QTableWidgetItem
import data
USERNAME = ''


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("CryptoPy")
        MainWindow.setFixedSize(571, 623)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(248, 248, 255)")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 140, 575, 491))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 571, 52))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)

        self.file_to_crypto = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.file_to_crypto.setEnabled(True)
        self.file_to_crypto.setMinimumSize(QtCore.QSize(0, 50))
        self.file_to_crypto.setFont(font)
        self.file_to_crypto.setObjectName("file_to_crypto")
        self.file_to_crypto.setStyleSheet("border: 1px solid black;")
        self.file_to_crypto.setToolTip("Зашифрованный файл добавляется в директорию\n"
                                       "к изначальному")

        self.horizontalLayout.addWidget(self.file_to_crypto)
        self.fil_to_decrypto = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.fil_to_decrypto.setMinimumSize(QtCore.QSize(0, 50))
        self.fil_to_decrypto.setFont(font)
        self.fil_to_decrypto.setObjectName("fil_to_decrypto")
        self.fil_to_decrypto.setStyleSheet("border: 1px solid black;")
        self.fil_to_decrypto.setToolTip("Для расшифровки потребуется файл с расширением .encrypt.txt\n"
                                        "и ключ")
        self.horizontalLayout.addWidget(self.fil_to_decrypto)
        self.del_file = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.del_file.setMinimumSize(QtCore.QSize(0, 50))
        self.del_file.setStyleSheet("border: 1px solid black;")
        self.del_file.setFont(font)
        self.del_file.setObjectName("del_file")
        self.del_file.setToolTip('Выберите файл из списка, который вы хотите удалить')
        self.horizontalLayout.addWidget(self.del_file)

        font.setPointSize(10)
        self.show_message = QtWidgets.QLabel(self.centralwidget)
        self.show_message.setGeometry(QtCore.QRect(10, 60, 561, 61))
        self.show_message.setFont(font)
        self.show_message.setStyleSheet("color: rgb(240, 128, 128);")
        self.show_message.setText("")
        self.show_message.setObjectName("show_message")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 21))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("background-color: rgb(248, 248, 255);"
                                   "border: 1px solid rgb(0, 0, 0)")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu.setStyleSheet("color: rgb(0, 0, 0)")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.setStyleSheet("border: 1px solid rgb(0, 0, 0);"
                                "color: rgb(0, 0, 0);")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CryptoPy"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.action.setText(_translate("MainWindow", "Настройки"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Логин"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название файла"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Хэш"))
        self.file_to_crypto.setText(_translate("MainWindow", "Зашифровать файл"))
        self.fil_to_decrypto.setText(_translate("MainWindow", "Расшифровать файл"))
        self.del_file.setText(_translate("MainWindow", "Удалить файл"))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(625, 324)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.set_dir_label = QtWidgets.QLabel(Dialog)
        self.set_dir_label.setGeometry(QtCore.QRect(10, 40, 201, 41))
        self.set_dir_label.setFont(font)
        self.set_dir_label.setObjectName("set_dir_label")

        self.set_dir = QtWidgets.QPushButton(Dialog)
        self.set_dir.setGeometry(QtCore.QRect(460, 40, 91, 31))
        self.set_dir.setFont(font)
        self.set_dir.setObjectName("set_dir")

        self.change_pass = QtWidgets.QLabel(Dialog)
        self.change_pass.setGeometry(QtCore.QRect(10, 100, 151, 41))
        self.change_pass.setFont(font)
        self.change_pass.setObjectName("change_pass")

        self.apply = QtWidgets.QPushButton(Dialog)
        self.apply.setGeometry(QtCore.QRect(230, 250, 141, 31))
        self.apply.setFont(font)
        self.apply.setObjectName("apply")

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.old_pass = QtWidgets.QLineEdit(Dialog)
        self.old_pass.setGeometry(QtCore.QRect(220, 110, 160, 30))
        self.old_pass.setFont(font)
        self.old_pass.setStatusTip("")
        self.old_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.old_pass.setObjectName("old_pass")

        self.new_pass = QtWidgets.QLineEdit(Dialog)
        self.new_pass.setGeometry(QtCore.QRect(220, 150, 160, 30))
        self.new_pass.setFont(font)
        self.new_pass.setObjectName("new_pass")
        self.new_pass.setEchoMode(QtWidgets.QLineEdit.Password)

        self.new_pass_sec = QtWidgets.QLineEdit(Dialog)
        self.new_pass_sec.setGeometry(QtCore.QRect(220, 190, 160, 30))
        self.new_pass_sec.setFont(font)
        self.new_pass_sec.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pass_sec.setObjectName("new_pass_sec")

        self.set_dit_edit = QtWidgets.QLineEdit(Dialog)
        self.set_dit_edit.setGeometry(QtCore.QRect(220, 40, 201, 31))
        self.set_dit_edit.setFont(font)
        self.set_dit_edit.setText("")
        self.set_dit_edit.setObjectName("set_dit_edit")

        self.show_message = QtWidgets.QLabel(Dialog)
        self.show_message.setGeometry(QtCore.QRect(420, 120, 151, 141))
        self.show_message.setFont(font)
        self.show_message.setText("")
        self.show_message.setObjectName("show_message")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.set_dir_label.setText(_translate("Dialog", "Установить директорию\n"
                                      "по умолчанию"))
        self.set_dir.setText(_translate("Dialog", "Выбрать"))
        self.change_pass.setText(_translate("Dialog", "Изменить пароль"))
        self.old_pass.setPlaceholderText(_translate("Dialog", "Старый пароль"))
        self.new_pass.setPlaceholderText(_translate("Dialog", "Новый пароль"))
        self.new_pass_sec.setPlaceholderText(_translate("Dialog", "Повторите пароль"))
        self.apply.setText(_translate("Dialog", "Применить"))


class MyDialog(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, username):
        super().__init__()
        super().setupUi(self)
        self.user = username
        self.set_dir.clicked.connect(self.set_direct)
        self.apply.clicked.connect(self.apply_true)
        res = data.check_default_folder(self.user)
        self.set_dit_edit.setText(res)

    def set_direct(self):

        direr = QFileDialog.getExistingDirectory()
        self.set_dit_edit.setText(direr)

    def apply_true(self):
        old_pass = self.old_pass.text()
        new_pass = self.new_pass.text()
        new_pass_second = self.new_pass_sec.text()
        set_dir = self.set_dit_edit.text()
        if (old_pass == '' or new_pass == '' or new_pass_second == '') and \
                set_dir == '':
            self.close()
        elif old_pass == '' or new_pass == '' or new_pass_second == '':
            data.set_default_folder(set_dir, self.user)
            self.close()
        elif set_dir == '':
            res = data.check_old_pass(self.old_pass.text(), self.user)
            if res:
                self.show_message.setStyleSheet('color: rgb(255, 0, 0)')
                self.show_message.setText('Неправильно введен\nстарый пароль')
            else:
                if new_pass == old_pass:
                    self.show_message.setStyleSheet('color: rgb(255, 0, 0)')
                    self.show_message.setText('Вы ввели тот же\nпароль')
                elif new_pass == new_pass_second:
                    data.set_new_pass(new_pass, self.user)
                    self.close()
                else:
                    self.show_message.setStyleSheet('color: rgb(255, 0, 0)')
                    self.show_message.setText('Введенные пароли\nне совпадают')
        else:
            data.set_default_folder(set_dir, self.user)
            res = data.check_old_pass(self.old_pass.text(), self.user)  # проверяет на совпадение старый пароль
            if res:
                self.show_message.setStyleSheet('color: rgb(255, 0, 0)')
                self.show_message.setText('Неправильно введен\nстарый пароль')
            else:
                if new_pass == old_pass:
                    self.show_message.setStyleSheet('color: rgb(255, 0, 0)')
                    self.show_message.setText('Вы ввели тот же\nпароль')
                elif new_pass == new_pass_second:
                    data.set_new_pass(new_pass, self.user)
                    self.close()
                else:
                    self.show_message.setStyleSheet('color: rgb(255, 0, 0)')
                    self.show_message.setText('Введенные пароли\nне совпадают')


class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, username):
        super().__init__()
        super().setupUi(self)
        self.action.triggered.connect(self.setup)
        self.file_to_crypto.clicked.connect(self.open_file)
        self.fil_to_decrypto.clicked.connect(self.decrypt_file)
        self.del_file.clicked.connect(self.delete_file)
        self.user = username
        # заполняет таблицу с файлами
        res = data.take_from_bd(self.user)
        self.tableWidget.setHorizontalHeaderLabels(('Логин', "Название файла", "Хэш"))
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                cellinfo = QTableWidgetItem(elem)
                if j != 0:
                    cellinfo.setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # запрещает изменять ячейки
                self.tableWidget.setItem(i, j, cellinfo)
        self.tableWidget.resizeColumnsToContents()

    def open_file(self):  # пользователь выбирает файл для шифровки
        res = data.check_default_folder(self.user)
        file_directory = QFileDialog.getOpenFileName(self, '', res)[0]
        res = data.encrypto(self.user, file_directory)
        if res == 'secondFilename':
            self.show_message.setStyleSheet("color: rgb(255, 0, 0);")
            self.show_message.setText('Файл с таким названием уже был загружен')
        elif res == 'emptyDir':
            self.show_message.setStyleSheet("color: rgb(255, 0, 0);")
            self.show_message.setText('Файл не выбран')
        else:
            self.show_message.setStyleSheet("color: rgb(0, 0, 0);")
            self.show_message.setText('В папку с вашим файлом добавлен зашифрованный файл с расширением\n'
                                      '".encrypted.txt" и ключ для расшифровки, у которого вначале\n'
                                      'написано "cipher_key" и название вашего файла')
        # при добавлении элемента таблица обновляется
        res = data.take_from_bd(self.user)
        self.tableWidget.setRowCount(len(res))
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                cellinfo = QTableWidgetItem(str(val))
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, j, cellinfo)

    def decrypt_file(self):  # пользователь выбирает файл для дешифровки
        res = data.check_default_folder(self.user)
        files = QFileDialog.getOpenFileName(self, 'Выберете файл для расшифровки', res, 'Text(*.encrypted.txt)')[0]
        if files:
            cipher = QInputDialog.getText(self, 'Ввод ключа', 'Введите ключ')[0]
            if cipher:
                result = data.decrypto(files, cipher)
                if result == 'changedFile':
                    self.show_message.setStyleSheet("color: rgb(255, 0, 0);")
                    self.show_message.setText('Файл был изменен')
                elif result == 'unknownCipherKey':
                    self.show_message.setStyleSheet("color: rgb(255, 0, 0);")
                    self.show_message.setText('Нет файла или неправильный ключ')
                else:
                    self.show_message.setStyleSheet("color: rgb(0, 0, 0);")
                    self.show_message.setText('Успешная расшифровка')
        else:
            self.show_message.setStyleSheet("color: rgb(255, 0, 0);")
            self.show_message.setText('Файл не выбран')

    def delete_file(self):  # пользователь удаляет ненужный файл
        res_del = list(map(lambda x: x[1], data.take_from_bd(self.user)))
        file_for_del = QInputDialog.getItem(self, '', 'Выберите файл для удаления', res_del, 0, False)[0]
        data.delete_file(self.user, file_for_del)
        res = data.take_from_bd(self.user)
        self.tableWidget.setRowCount(len(res))
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                cellinfo = QTableWidgetItem(str(val))
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, j, cellinfo)

    def setup(self):
        self.a = MyDialog(self.user)
        self.a.show()


def my_excepthook(type, value, tback):
    # функция для отлова ошибок
    sys.__excepthook__(type, value, tback)


sys.excepthook = my_excepthook


