#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit, QComboBox)
from PyQt5.QtGui import *
import sqlite3


class CreateHost(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        okButton = QPushButton('+')
        okButton.clicked.connect(self.create_unit)
        #okButton.clicked.connect(self.main.update())


        number = QLabel('Марка стали')
        self.numberEdit = QLineEdit()
        name = QLabel('Название')
        self.nameEdit = QLineEdit()
        mark = QLabel('Отметка')
        self.markEdit = QLineEdit()
        scheme = QLabel('Схема')
        self.schemeEdit = QLineEdit()
        period = QLabel('Наработка')
        self.periodEdit = QLineEdit()
        brand_steel = QLabel('Марка стали')
        self.brand_steelEdit = QLineEdit()

        number_h = QHBoxLayout()
        number_h.addWidget(number)
        number_h.addWidget(self.numberEdit)
        name_h = QHBoxLayout()
        name_h.addWidget(name)
        name_h.addWidget(self.nameEdit)
        mark_h = QHBoxLayout()
        mark_h.addWidget(mark)
        mark_h.addWidget(self.markEdit)
        scheme_h = QHBoxLayout()
        scheme_h.addWidget(scheme)
        scheme_h.addWidget(self.schemeEdit)
        period_h = QHBoxLayout()
        period_h.addWidget(period)
        period_h.addWidget(self.periodEdit)
        brand_steel_h = QHBoxLayout()
        brand_steel_h.addWidget(brand_steel)
        brand_steel_h.addWidget(self.brand_steelEdit)

        vbox = QVBoxLayout()
        vbox.addLayout(number_h)
        vbox.addLayout(name_h)
        vbox.addLayout(mark_h)
        vbox.addLayout(scheme_h)
        vbox.addLayout(period_h)
        vbox.addLayout(brand_steel_h)
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

class Host(QWidget):
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
    ex = CreateHost()
    sys.exit(app.exec_())
