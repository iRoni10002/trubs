#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit, QComboBox, QDialog, QMainWindow, QFrame)
from PyQt5.QtGui import *
from units import CreateUnit
from institution import MainInstitution
import pickle
import sqlite3
from db_manger import *

class ListCity(QPushButton):
    def __init__(self, city, count, expansion):
        super().__init__()
        self.city = city
        self.count = count
        self.expanation = expansion
        self.setObjectName(city)
        print(self.objectName())
        self.initUI()

    def initUI(self):

        self.okButton = QPushButton('+')
        #okButton.clicked.connect(self.create_city)
        #okButton.clicked.connect(self.main.update())
        
        pixmap = QPixmap('image/city.png')
        pixmap_new = pixmap.scaled(100, 100)
        icon = QPushButton()
        icon.setIcon(QIcon('image/city.png'))
        icon.setIconSize(QSize(110, 110))
        self.clicked.connect(self.next)
        self.city = QLabel(self.city)
        s = str(self.count)
        s1 = 'учреждений: '
        s = s1 + s
        self.counter = QLabel(s)

        self.okButton.setStyleSheet("background-color: rgba(100, 0, 100, 100); color: white;"
                                    "font-family: Verdana; font-size: 16px;"
                                    "margin: 0px 10px 0px 10px;"
                                    "border-radius: 20px;")

        style_label = "padding-left: 0px;" \
                      "font-size: 14px; font-family: Verdana;}" \
                      "QFrame {background-color: rgba(255, 255, 255, 0.4); border-radius: 10px;}" \
                      "QLabel {color: black; background-color: transparent;"
        
        self.info_v = QVBoxLayout()
        self.info_v.addWidget(self.city)
        self.info_v.addWidget(self.counter)
        self.city_h = QHBoxLayout()
        self.city_h.addWidget(icon)
        self.city_h.addLayout(self.info_v)
        frame = QFrame()
        frame.setFrameShape(QFrame.Panel)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setStyleSheet(style_label)
        frame.setLayout(self.city_h)
        x = QHBoxLayout()
        x.addWidget(frame)
        self.setLayout(x)
        #self.setLayout(self.city_h)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Добавление города')
        self.setFixedSize(300, 150)
        self.show()
    def next(self):
        print("xxxx: ",self.objectName())
        x = self.expanation
        y = self.objectName()
        self.new = MainInstitution(x, y)
    def open_unit(self):
        self.unit = CreateUnit()

class CreateCity(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        addInstitutionButton = QPushButton('')
        addInstitutionButton.setIcon(QIcon('image/plus_2.png'))
        addInstitutionButton.setIconSize(QSize(55, 55))
        addInstitutionButton.clicked.connect(self.create_city)
        
        city = QLabel("Город")
        self.cityEdit = QLineEdit()

        style = "QLabel {" \
                "color: black; font-family: Verdana; font-size: 20px;" \
                "margin-top: 40px;" \
                "}" \
                "QLineEdit {" \
                "color: black; background-color: rgb(193,203,253); font-family: Verdana; font-size: 20px;" \
                "border-radius: 0px; margin-top: 40px;" \
                "}" \
                "QPushButton {" \
                "background-color: rgba(255, 255, 255, 0.3);" \
                "margin: 0px -2px 0px -2px; border-radius: 20px;" \
                "}"
        
        self.setStyleSheet(style)
        
        city_h = QHBoxLayout()
        city_h.addWidget(city)
        city_h.addWidget(self.cityEdit)
        button_h = QHBoxLayout()
        button_h.addStretch(1)
        button_h.addWidget(addInstitutionButton)
        button_h.addStretch(1)
        vbox = QVBoxLayout()
        vbox.addLayout(city_h)
        vbox.addLayout(button_h)
        
        self.setLayout(vbox)
        
        p = QPalette()
        gradient = QLinearGradient(0, 0, 120, 400)
        gradient.setColorAt(0.0, QColor(117,160,252))
        gradient.setColorAt(1.0, QColor(193,203,253))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Добавление города')
        self.setFixedSize(500, 250)
        self.show()

    def create_city(self):
        city = self.cityEdit.text()
        
        db = SqliteDatabase('mydb.db')
        db.connect()
        
        institution = City.create(name=city, count_institution=0, is_relative=True)
        
        db.close()
        
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = CreateCity()
    sys.exit(app.exec_())
