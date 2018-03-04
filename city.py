#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit, QComboBox, QDialog)
from PyQt5.QtGui import *
from units import CreateUnit, Unit
import pickle
import sqlite3


class CreateCity(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        okButton = QPushButton('+')
        okButton.clicked.connect(self.create_city)
        #okButton.clicked.connect(self.main.update())

        name = QLabel('Название:')
        self.nameEdit = QLineEdit()

        okButton.setStyleSheet("background-color: rgba(100, 0, 100, 100); color: white;"
                               "font-family: Verdana; font-size: 16px;"
                               "margin: 0px 10px 0px 10px;"
                               "border-radius: 20px;")
        name.setStyleSheet("color: #334761;"
                            "font-family: Verdana; font-size: 16px;"
                            "margin: 0px 40px 0px 0px;"
                            "border: 3px solid transparent; border-left-color: red")
        self.nameEdit.setStyleSheet("color: #334761;"
                                "font-family: Verdana; font-size: 14px;"
                                "border-radius: 20px;"
                                "border: 3px solid transparent; border-right-color: red")

        hmail = QHBoxLayout()
        hmail.addWidget(name)
        hmail.addWidget(self.nameEdit)
        hbox = QHBoxLayout()
        hbox.addWidget(okButton)
        hbox.addStretch(1)
        vbox = QVBoxLayout()
        vbox.addLayout(hmail)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Добавление города')
        self.setFixedSize(300, 150)
        self.show()

    def create_city(self):
        name = self.nameEdit.text()
        conn = sqlite3.connect('mydatabase.db')
        print('good')
        cursor = conn.cursor()
        print('good')
        jj = str(name)
        city = [jj]
        cursor.execute("INSERT INTO city VALUES (?)", city)
        print('good')
        cursor.execute("SELECT * FROM city")
        print('good')
        y = cursor.fetchall()
        print('good-length', len(y))
        conn.commit()
        self.close()

class City(QWidget):
    def __init__(self, name_city):
        super().__init__()
        self.name_city = name_city
        self.initUI()

    def initUI(self):

        addButton = QPushButton('+')
        addButton.clicked.connect(self.open_unit)
        print("ffoodd")
        name = QLabel(self.name_city)
        imag = QLabel()
        pixar = QPixmap('city.png')
        pixmap = pixar.scaled(64, 64)
        imag.setPixmap(pixmap)
        print("ffoodd")

        header = QHBoxLayout()
        header.addWidget(imag)
        header.addStretch(1)
        header.addWidget(addButton)
        header.addWidget(name)
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(header)
        self.vbox.addStretch(1)
        conn = sqlite3.connect('mydatabase.db')
        print('good')
        cursor = conn.cursor()
        print('good')
        cursor.execute("SELECT * FROM units")
        print('good')
        y = cursor.fetchall()
        #print('good-length', len(y), y[0], y[1])
        for i in range(len(y)):
            x = y[i]
            print('x = ', x[0])
            brand_ = QLabel(x[0])
            type_ = QLabel(x[1])
            station_number_ = QLabel(x[2])
            reg_number_ = QLabel(x[3])
            btn = QPushButton('Список узлов')
            print(btn)
            h = QHBoxLayout()
            h.addWidget(brand_)
            h.addWidget(type_)
            h.addWidget(station_number_)
            h.addWidget(reg_number_)
            h.addWidget(btn)
            self.vbox.addLayout(h)
        self.setLayout(self.vbox)
        print("ffoodd")

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Добавление города')
        self.show()

    def open_unit(self):
        self.unit = CreateUnit()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = City('rr')
    sys.exit(app.exec_())
