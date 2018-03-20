#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QDockWidget, QLabel,
                             QScrollArea, QDialog, QFrame, QLineEdit)
from PyQt5 import QtGui
from PyQt5.QtGui import *
from units import CreateUnit, ListUnit,MainUnit
import pickle
import sqlite3
from db_manger import *

class UpdateScreen(QDialog):
    def __init__(self, expansion):
        super().__init__()
        self.expansion = expansion
        self.initUI()

    def initUI(self):
        vv = QVBoxLayout()
        self.setLayout(vv)
        p = QPalette()
        gradient = QLinearGradient(0, 0, 120, 400)
        gradient.setColorAt(0.0, QColor(117,160,252))
        gradient.setColorAt(1.0, QColor(193,203,253))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
        if self.expansion == '1':
            self.showFullScreen()
        else:
            self.setGeometry(0, 30, 800, 600)
        self.setWindowTitle('Menubar')
        self.show()

class MainInstitution(QWidget):

    def __init__(self, expansion, city):
        super().__init__()
        print('xrp')
        self.expansion = expansion
        self.city_name = city
        print(self.city_name)
        self.initUI()

    def initUI(self):
        addInstitutionButton = QPushButton('')
        addInstitutionButton.setIcon(QIcon('image/plus_2.png'))
        addInstitutionButton.setIconSize(QSize(55, 55))
        addInstitutionButton.clicked.connect(self.addCity)
        updateButton = QPushButton('')
        updateButton.setIcon(QIcon('image/update_2.png'))
        updateButton.setIconSize(QSize(75, 75))
        updateButton.clicked.connect(self.update_window)
        backButton = QPushButton('')
        backButton.setIcon(QIcon('image/back_2.png'))
        backButton.setIconSize(QSize(75, 75))
        backButton.clicked.connect(self.back)
        exitButton = QPushButton('')
        exitButton.setIcon(QIcon('image/exit_2.png'))
        exitButton.setIconSize(QSize(75, 75))
        exitButton.clicked.connect(self.exit)
        #backButton.clicked.connect()
        
        db = SqliteDatabase('mydb.db')
        db.connect()
        j = 0
        g = 0
        h_city = QHBoxLayout()
        v_city = QVBoxLayout()
        v_city.setSpacing(10)
        for i in Institution.select().where(Institution.owner == self.city_name):
            if j == 4:
                v_city.addLayout(h_city)
                h_city = QHBoxLayout()
                count = Units.select().where(Units.owner == i.name)
                institution = ListInstitution(i.owner, i.name, self.expansion, len(count))
                institution.setObjectName(i.name)
                institution.move(-300, -300)
                v_city.addLayout(h_city)
                j = 0
            else:
                print("fggg")
                count = Units.select().where(Units.owner == i.name)
                institution = ListInstitution(i.owner, i.name, self.expansion, len(count))
                print("fgggd")
                institution.setObjectName(i.name)
                institution.move(-300, -300)
            h_city.addWidget(institution)
            j += 1
            g += 1
        if g < 5:
            v_city.addLayout(h_city)
        db.close()
        
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("border: 1px solid transparent; background-color: transparent;")
        #tt = MainWindow()
        gg = QWidget()
        gg.setLayout(v_city)
        self.scroll.setWidget(gg)
        
        title = QLabel(self.city_name)
        
        buttons_left = QHBoxLayout()
        buttons_left.addWidget(backButton)
        buttons_left.addWidget(addInstitutionButton)
        buttons_right = QHBoxLayout()
        buttons_right.addWidget(updateButton)
        buttons_right.addWidget(exitButton)
        
        tit_h = QHBoxLayout()
        tit_h.addLayout(buttons_left)
        tit_h.addStretch(1)
        tit_h.addWidget(title)
        tit_h.addStretch(1)
        tit_h.addLayout(buttons_right)
        
        vv = QVBoxLayout()
        vv.addLayout(tit_h)
        vv.addWidget(self.scroll)
        
        print("fgggdsgsg")
        
        title.setStyleSheet("background-color: rgba(255, 255, 255, 0.5); color: black;"
                            "border: 3px solid transparent;"
                            "padding: 10px 300% 10px 300%;"
                            "margin-top: 0px;"
                            "font-size: 30px; font-family: Verdana;")
        addInstitutionButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.3); padding: 12px;")
        updateButton.setStyleSheet("background-color: transparent;")
        backButton.setStyleSheet("background-color: transparent")
        exitButton.setStyleSheet("background-color: transparent")
        
        self.setLayout(vv)
        print("2")
        self.update()
        p = QPalette()
        gradient = QLinearGradient(0, 0, 120, 400)
        gradient.setColorAt(0.0, QColor(117,160,252))
        gradient.setColorAt(1.0, QColor(193,203,253))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
        print("3")
        print(self.expansion)
        if self.expansion == '1':
            self.showFullScreen()
        else:
            self.setGeometry(0, 30, 800, 600)
        print("4")
        self.setWindowTitle('Menubar')
        print("5")
        self.show()
        print("6")
    def back(self):
        self.close()
    def exit(self):
        quit()
    def update_window(self):
        self.screen = UpdateScreen(self.expansion)
        self.main = MainInstitution(self.expansion, self.city_name)
        self.close()
        self.screen.close()
    def update_(self):
        pass
    def draw_city(self, name):
        print("start")
        self.btn = QPushButton(name)
        self.btn.clicked.connect(self.open_city)
        print("end")
        return self.btn
    def addCity(self):
        from city import CreateCity
        self.add = CreateInstitution(self.city_name)
        print("ALL GOOD, KIDDO")
    def open_city(self):
        self.text = self
        print("xep: ", self.text)
        self.city = City('gg')

class ListInstitution(QPushButton):
    def __init__(self, city, title, expansion, count):
        super().__init__()
        self.city = city
        self.title = title
        self.expansion = expansion
        self.count = count
        print("fgggdsgsg")
        self.initUI()

    def initUI(self):

        self.okButton = QPushButton('+')
        #okButton.clicked.connect(self.create_city)
        #okButton.clicked.connect(self.main.update())
        
        pixmap = QPixmap('image/uch.png')
        pixmap_new = pixmap.scaled(100, 100)
        icon = QLabel()
        icon.setPixmap(pixmap_new)
        self.city = QLabel(self.city)
        title = QLabel(self.title)
        s1 = 'агрегатов: '
        s = str(self.count)
        s = s1 + s
        count = QLabel(s)
        
        self.clicked.connect(self.next)
        
        self.okButton.setStyleSheet("background-color: rgba(100, 0, 100, 100); color: white;"
                                    "font-family: Verdana; font-size: 16px;"
                                    "margin: 0px 10px 0px 10px;"
                                    "border-radius: 20px;")

        style_label = "padding-left: 10px;" \
                      "font-size: 14px; font-family: Verdana;}" \
                      "QFrame {background-color: rgba(255, 255, 255, 0.4); border-radius: 10px;}" \
                      "QLabel {color: black; background-color: transparent;"
        
        self.info_v = QVBoxLayout()
        self.info_v.addWidget(self.city)
        self.info_v.addWidget(title)
        self.info_v.addWidget(count)
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
        x = self.expansion
        y = self.objectName()
        self.new = MainUnit(x, y)
        print('xepo4ek')
    def open_unit(self):
        self.unit = CreateUnit()

class CreateInstitution(QWidget):

    def __init__(self, city):
        super().__init__()
        self.city_name = city
        self.initUI()

    def initUI(self):

        addInstitutionButton = QPushButton('')
        addInstitutionButton.setIcon(QIcon('image/plus_2.png'))
        addInstitutionButton.setIconSize(QSize(55, 55))
        addInstitutionButton.clicked.connect(self.create_city)
        
        city = QLabel("Город")
        title = QLabel("Название Учреждения")
        self.cityEdit = QLabel(self.city_name)
        self.titleEdit = QLineEdit()

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
        city_h.addStretch(1)
        city_h.addWidget(self.cityEdit)
        title_h = QHBoxLayout()
        title_h.addWidget(title)
        title_h.addStretch(1)
        title_h.addWidget(self.titleEdit)
        button_h = QHBoxLayout()
        button_h.addStretch(1)
        button_h.addWidget(addInstitutionButton)
        button_h.addStretch(1)
        vbox = QVBoxLayout()
        vbox.addLayout(city_h)
        vbox.addLayout(title_h)
        vbox.addStretch(1)
        vbox.addLayout(button_h)
        
        self.setLayout(vbox)

        p = QPalette()
        gradient = QLinearGradient(0, 0, 120, 400)
        gradient.setColorAt(0.0, QColor(117,160,252))
        gradient.setColorAt(1.0, QColor(193,203,253))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        self.setGeometry(300, 300, 300, 150)
        self.setFixedSize(500, 250)
        self.setWindowTitle('Log in')
        self.show()

    def create_city(self):
        city = self.cityEdit.text()
        title = self.titleEdit.text()
        
        db = SqliteDatabase('mydb.db')
        db.connect()
        
        institution = Institution.create(name=title, owner=city, count_units=0, is_relative=True)
        
        db.close()
        
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
    ex = ListInstitution('jopa', 'jpa')
    sys.exit(app.exec_())
