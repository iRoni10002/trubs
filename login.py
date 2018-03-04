#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit, QComboBox)
from main import Main
from PyQt5.QtGui import *
import pickle
import sqlite3


class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        okButton = QPushButton('Log in')
        okButton.clicked.connect(self.login)

        email = QLabel('E-mail:')
        password = QLabel('Password:')
        self.emailEdit = QLineEdit('dima')
        self.passwordEdit = QLineEdit('123')
        self.chose_expansion = QComboBox()
        self.chose_expansion.addItem('600*400')
        self.chose_expansion.addItem('800*600')
        self.chose_expansion.addItem('1200*800')

        #shadow = Q(self)
        #shadow.setColor(QColor(50,200,200))
        #shadow.setBlurRadius(30)
        #shadow.setOffset(4,-3)

        okButton.setStyleSheet("background-color: rgba(100, 0, 100, 100); color: white;"
                               "font-family: Verdana; font-size: 16px;"
                               "margin: 0px 10px 0px 10px;"
                               "border-radius: 20px;")
        email.setStyleSheet("color: #334761;"
                            "font-family: Verdana; font-size: 16px;"
                            "margin: 0px 40px 0px 0px;"
                            "border: 3px solid transparent; border-left-color: red")
        password.setStyleSheet("color: #334761;"
                               "font-family: Verdana; font-size: 16px;"
                               "margin: 0px 15px 0px 0px;"
                               "border: 3px solid transparent; border-left-color: red")
        self.emailEdit.setStyleSheet("color: #334761;"
                                "font-family: Verdana; font-size: 14px;"
                                "border-radius: 20px;"
                                "border: 3px solid transparent; border-right-color: red")
        self.passwordEdit.setStyleSheet("color: #334761;"
                                   "font-family: Verdana; font-size: 14px;"
                                   "border-radius: 100px;"
                                   "border: 3px solid transparent; border-right-color: red")


        hmail = QHBoxLayout()
        hmail.addWidget(email)
        hmail.addWidget(self.emailEdit)
        hpass = QHBoxLayout()
        hpass.addWidget(password)
        hpass.addWidget(self.passwordEdit)

        hbox = QHBoxLayout()
        hbox.addWidget(okButton)

        vbox = QVBoxLayout()
        vbox.addLayout(hmail)
        vbox.addLayout(hpass)
        vbox.addWidget(self.chose_expansion)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Log in')
        self.setFixedSize(300, 150)
        self.show()

    def login(self):
        email = self.emailEdit.text()
        password = self.passwordEdit.text()
        conn = sqlite3.connect('mydatabase.db')
        print('good')
        #conn.row_factory = sqlite3.Row
        #Создание курсора
        c = conn.cursor()
        print('good')
        c.execute("SELECT * FROM users")
        print('good')
        y = c.fetchall()
        x = y[0]
        print('good')
        name = x[0]
        pas = x[1]
        print(name, pas)
        if str(email) == str(name):
            if str(password) == str(pas):
                number = self.chose_expansion.currentIndex()
                print("()")
                expansion = self.chose_expansion.itemText(number)
                print("!")
                self.main = Main(expansion)
                print("!!")
                self.close()
                print("!!!")
    def login_old(self):
        email = self.emailEdit.text()
        password = self.passwordEdit.text()
        d = {'email':email, 'pass':password}
        f = open('login.txt', 'rb')
        data_new = pickle.load(f)
        print("d:", d, data_new)
        s = set(data_new.keys())
        print(s)

        if str(d['email']) in data_new:
            number = self.chose_expansion.currentIndex()
            expansion = self.chose_expansion.itemText(number)
            print(expansion)
            print('good')
            self.main = Main(expansion)
            self.close()
            print("good")
        else:
            print("no", d['email'])
        f.close()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())
