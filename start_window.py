#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QComboBox,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit)
from PyQt5.QtGui import QColor
from main import Main

class StartWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        bg = QLabel()
        bg.setGeometry(0, 0, 300, 150)
        bg.show()
        bg.setStyleSheet("background-color: red;")

        login_button = QPushButton('Войти')
        reg_button = QPushButton('Зарегистрироваться')

        login_button.clicked.connect(self.login)
        reg_button.clicked.connect(self.registr)

        style = "QPushButton { background-color: rgb(102, 102, 102); color: white; " \
                "font-family: Verdana; font-size: 24px; " \
                "margin: 0px 10px 0px 10px; " \
                "border-radius: 20px 20px 20px 20px;" \
                "border-radius: 20px;}"

        self.setStyleSheet(style)


        vbox = QVBoxLayout()
        vbox.addWidget(login_button)
        vbox.addWidget(reg_button)
        self.setLayout(vbox)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(192, 192, 192))
        self.setPalette(p)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Добро пожаловать!')
        self.setFixedSize(300, 150)
        self.show()

    def Submit(self):
        self.mainWindow = Main()
        ex.close()
    def login(self):
        print("ff")
    def registr(self):
        print("ff")



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = StartWindow()

    sys.exit(app.exec_())
