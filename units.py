#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit, QComboBox)
from PyQt5.QtGui import *
import sqlite3


class CreateUnit(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        okButton = QPushButton('+')
        okButton.clicked.connect(self.create_unit)
        #okButton.clicked.connect(self.main.update())

        brand = QLabel('Марка')
        self.brandEdit = QLineEdit()
        type = QLabel('Тип')
        self.typeEdit = QLineEdit()
        station_number = QLabel('Станционный номер')
        self.station_numberEdit = QLineEdit()
        reg_number = QLabel('Регистрационный номер')
        self.reg_numberEdit = QLineEdit()
        brand_h = QHBoxLayout()
        brand_h.addWidget(brand)
        brand_h.addWidget(self.brandEdit)
        type_h = QHBoxLayout()
        type_h.addWidget(type)
        type_h.addWidget(self.typeEdit)
        station_number_h = QHBoxLayout()
        station_number_h.addWidget(station_number)
        station_number_h.addWidget(self.station_numberEdit)
        reg_number_h = QHBoxLayout()
        reg_number_h.addWidget(reg_number)
        reg_number_h.addWidget(self.reg_numberEdit)

        vbox = QVBoxLayout()
        vbox.addLayout(brand_h)
        vbox.addLayout(type_h)
        vbox.addLayout(station_number_h)
        vbox.addLayout(reg_number_h)
        vbox.addWidget(okButton)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Добавление города')
        self.setFixedSize(300, 150)
        self.show()

    def create_unit(self):

        print('good_u')
        brand = str(self.brandEdit.text())
        type = str(self.typeEdit.text())
        station_number = str(self.station_numberEdit.text())
        reg_number = str(self.reg_numberEdit.text())
        print('good_u')
        conn = sqlite3.connect('mydatabase.db')
        print('good_u')
        cursor = conn.cursor()
        print('good_U')
        unit = [brand, type, station_number, reg_number]
        cursor.execute("INSERT INTO units VALUES (?,?,?,?)", unit)
        print('good_u')
        cursor.execute("SELECT * FROM units")
        print('good_U')
        y = cursor.fetchall()
        print('good-length', len(y))
        conn.commit()
        self.close()

class Unit(QWidget):
    def __init__(self, name_city):
        super().__init__()
        self.name_city = name_city
        self.initUI()

    def initUI(self):

        #okButton = QPushButton('+')

        print("ffoodd")
        name = QLabel(self.name_city)
        imag = QLabel()
        pixar = QPixmap('city.png')
        imag.setPixmap(pixar)
        print("ffoodd")

        header = QHBoxLayout()
        header.addWidget(imag)
        header.addStretch(1)
        header.addWidget(name)
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(header)
        self.vbox.addStretch(1)



        self.setLayout(self.vbox)
        print("ffoodd!!")

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Добавление города')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = CreateUnit()
    sys.exit(app.exec_())
