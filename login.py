#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit, QComboBox, QCheckBox)
from main import *
from PyQt5.QtGui import *
import pickle
import sqlite3
from peewee import *
from db_manger import *

class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        okButton = QPushButton('Войти')
        okButton.clicked.connect(self.login)

        email = QLabel('Логин')
        password = QLabel('Пароль')
        self.emailEdit = QLineEdit('dima')
        self.passwordEdit = QLineEdit('123')
        #self.chose_expansion = QComboBox()
        #self.chose_expansion.addItem('600*400')
        #self.chose_expansion.addItem('800*600')
        #self.chose_expansion.addItem('1200*800')
        self.chose_fullscrin = QCheckBox('Полный экран')

        okButton.setStyleSheet("background-color: rgb(117,160,252); color: black;"
                               "font-family: Verdana; font-size: 20px;"
                               "margin: 0px 60px 0px 0px;"
                               "border-radius: 20px;"
                               "width: 230px;")
        self.chose_fullscrin.setStyleSheet("margin-left: 65px;"
                                           "font-size: 12px; font-family: Verdana;")
        email.setStyleSheet("color: black;"
                            "font-family: Verdana; font-size: 20px;"
                            "margin: 0px 47px 0px 60px;"
                            "padding-bottom: 0px;")
        password.setStyleSheet("color: black;"
                               "font-family: Verdana; font-size: 20px;"
                               "margin: 0px 37px 0px 60px;"
                               "padding-top: 0px;")
        self.emailEdit.setStyleSheet("color: black; background-color: rgb(193,203,253);"
                                     "font-family: Verdana; font-size: 16px;"
                                     "border-radius: 20px;"
                                     "margin: 0px 60px 0px 0px;")
        self.passwordEdit.setStyleSheet("color: black; background-color: rgb(193,203,253);"
                                        "font-family: Verdana; font-size: 16px;"
                                        "border-radius: 100px;"
                                        "margin: 0px 60px 0px 0px;")
        #self.chose_expansion.setStyleSheet("margin: 0px 80px 0px 80px;")
        
        style = "drop-down {margin: 0px 80px 0px 80px;}"
        self.setStyleSheet(style)
        


        hmail = QHBoxLayout()
        hmail.addWidget(email)
        hmail.addWidget(self.emailEdit)
        hpass = QHBoxLayout()
        hpass.addWidget(password)
        hpass.addWidget(self.passwordEdit)
        vexpansion = QVBoxLayout()
        vexpansion.addWidget(self.chose_fullscrin)
        hsubmit = QHBoxLayout()
        hsubmit.addLayout(vexpansion)
        hsubmit.addWidget(okButton)

        hbox = QHBoxLayout()
        hbox.addWidget(okButton)

        vbox = QVBoxLayout()
        vbox.addLayout(hmail)
        vbox.addLayout(hpass)
        vbox.addLayout(hsubmit)
        
        p = QPalette()
        gradient = QLinearGradient(0, 0, 120, 400)
        gradient.setColorAt(0.0, QColor(117,160,252))
        gradient.setColorAt(1.0, QColor(193,203,253))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
        
        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Log in')
        self.setFixedSize(500, 250)
        self.show()
    
    def login(self):
        db = SqliteDatabase('mydb.db')
        db.connect()
        
        #grandma_ = Institution.get(Institution.name == 'ТЭЦ-5')
        #print("===========================================",grandma_.name)
    
        for i in Users.select():
            name = self.emailEdit.text()
            password = self.passwordEdit.text()
            print(i.name, i.password)
            name_right = i.name
            password_right = i.password
            print(name_right, password_right)
            if str(name) == str(name_right):
                if str(password) == str(password_right):
                    if self.chose_fullscrin.isChecked():
                        expansion = '1'
                        self.main = MainCity('1')
                        self.close()
                    else:
                        expansion = '2'
                        self.main = MainCity(expansion)
                        self.close()
            else:
                print("nea")
        db.close()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())
