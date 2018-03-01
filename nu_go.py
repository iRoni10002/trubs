#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QMainWindow, QPushButton, QInputDialog)

class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        email = QLabel('E-mail:')
        password = QLabel('Password')
        emailEdit = QLineEdit()
        passwordEdit = QTextEdit()
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(email, 1, 1)
        grid.addWidget(password, 2, 1)
        grid.addWidget(emailEdit, 1, 2)
        grid.addWidget(passwordEdit, 2, 2)

        self.setLayout(grid)

        self.setGeometry(200, 100, 400, 200)
        self.setWindowTitle('Review')
        self.show()

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        log = Login()
        log.move(100, 100)


        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showLog)


        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Log')
        self.show()

    def showLog(self):
        self.log = Login()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
