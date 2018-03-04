#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit)
from login import Login
import pickle
import sqlite3


class Registr(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        okButton = QPushButton("Submit")
        okButton.clicked.connect(self.sent_registr)

        email = QLabel('E-mail:')
        password = QLabel('Password:')
        self.emailEdit = QLineEdit('')
        self.passwordEdit = QLineEdit()
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        password_again = QLabel('Password again:')
        self.passwordEdit_again = QLineEdit()
        self.passwordEdit_again.setEchoMode(QLineEdit.Password)
        self.passwordEdit_again.returnPressed.connect(self.sent_registr)

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
        hpass_again = QHBoxLayout()
        hpass_again.addWidget(password_again)
        hpass_again.addWidget(self.passwordEdit_again)

        hbox = QHBoxLayout()
        hbox.addWidget(okButton)

        vbox = QVBoxLayout()
        vbox.addLayout(hmail)
        vbox.addLayout(hpass)
        vbox.addLayout(hpass_again)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Registration')
        self.setFixedSize(300, 150)
        self.show()
    def sent_registr(self):
        email = self.emailEdit.text()
        password = self.passwordEdit.text()
        password_again = self.passwordEdit_again.text()
        if password == password_again:
            conn = sqlite3.connect("mydatabase.db") # или :memory: чтобы сохранить в RAM
            cursor = conn.cursor()

            login = [(email, password)]

            cursor.execute("INSERT INTO users (name,password) VALUES (email,password)")
            conn.commit()
            print(cursor.fetchall())
            #print(email, password, password_again)
            #f = open('login.txt', 'rb')
            #Data = pickle.load(f)
            #print(Data)
            #f.close()
            #f = open('login.txt', 'ab')
            #print("D: ", Data)
            #d = {email:password}
            #print("d: ", d)
            #Data_new = {**d, **Data}
            #print("D_new: ", Data_new)
            #pickle.dump(Data_new, f)
            #f.close()
            #self.login = Login()
            #self.close()
        else:
            print('gg')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Registr()
    sys.exit(app.exec_())
