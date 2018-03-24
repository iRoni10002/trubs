#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QDockWidget, QLabel,
                             QScrollArea, QDialog)
from PyQt5 import QtGui
from PyQt5.QtGui import *
from reg_form import Reg
from city import City, ListCity
from institution import ListInstitution
import sqlite3
from peewee import *
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
            self.setFixedSize(800, 600)
        self.setWindowTitle('Menubar')
        self.show()

class MainCity(QWidget):

    def __init__(self, expansion):
        super().__init__()
        self.expansion = expansion
        self.initUI()

    def initUI(self):
        addInstitutionButton = QPushButton('')
        addInstitutionButton.setIcon(QIcon('image/plus_2.png'))
        addInstitutionButton.setIconSize(QSize(75, 75))
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
        
        self.next_city = str()
        #backButton.clicked.connect()
        
        db = SqliteDatabase('mydb.db')
        db.connect()
        j = 0
        g = 0
        h_city = QHBoxLayout()
        v_city = QVBoxLayout()
        v_city.setSpacing(10)
        for i in City.select():
            if j == 3:
                v_city.addLayout(h_city)
                h_city = QHBoxLayout()
                count = Institution.select().where(Institution.owner == i.name)
                city = ListCity(i.name, len(count), self.expansion)
                city.setObjectName(i.name)
                #city.clicked.connect(self.get_button_name)
                #city.clicked.connect(self.next)
                #city.clicked.connect(self.objectName())
                city.move(-300, -300)
                
                v_city.addLayout(h_city)
                j = 0
            else:
                count = Institution.select().where(Institution.owner == i.name)
                city = ListCity(i.name, len(count), self.expansion)
                city.setObjectName(i.name)
                print(city.objectName())
                #city.clicked.connect(self.get_button_name)
                #city.clicked.connect(self.next)
                city.move(-300, -300)
            h_city.addWidget(city)
            j += 1
            g += 1
        if g < 4:
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
        
        self.title = QLabel("Веберите город")
        
        buttons_left = QHBoxLayout()
        buttons_left.addWidget(backButton)
        buttons_left.addWidget(addInstitutionButton)
        buttons_right = QHBoxLayout()
        buttons_right.addWidget(updateButton)
        buttons_right.addWidget(exitButton)
        
        tit_h = QHBoxLayout()
        tit_h.addLayout(buttons_left)
        tit_h.addStretch(1)
        tit_h.addWidget(self.title)
        tit_h.addStretch(1)
        tit_h.addLayout(buttons_right)
        
        vv = QVBoxLayout()
        vv.addLayout(tit_h)
        vv.addWidget(self.scroll)
        
        self.title.setStyleSheet("background-color: rgba(255, 255, 255, 0.5); color: black;"
                                 "border: 3px solid transparent;"
                                 "padding: 10px 300% 10px 300%;"
                                 "margin-top: 0px;"
                                 "font-size: 30px; font-family: Verdana;")
        addInstitutionButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); padding: 12px;")
        updateButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); padding: 12px;")
        backButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); padding: 12px;")
        exitButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); padding: 12px;")
        #tit.setStyleSheet("background-color: rgba(255, 255, 255, 0.5); border-radius: 7px;")
        
        self.setLayout(vv)
        self.update()
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
    def back(self):
        self.close()
    def exit(self):
        quit()
    '''def get_button_name(self):
        #self.next_city = ListCity.next(self)
        #print('ss', self)
        #print(self.objectName())'''
    def next(self):
        self.up = UpdateScreen(self.expansion)
        #name = self.next_city
        #print("name: ", name)
        #self.main = MainNew(self.expansion, name)
        self.close()
        self.up.close()
    def update_window(self):
        self.main = MainCity(self.expansion)
        self.close()
    def open_reg(self):
        self.reg = Reg(400, 600)
    def draw_city(self, name):
        self.btn = QPushButton(name)
        self.btn.clicked.connect(self.open_city)
        return self.btn
    def addCity(self):
        from city import CreateCity
        self.city = CreateCity()
    def open_city(self):
        self.text = self
        self.city = City('gg')
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main('1')
    sys.exit(app.exec_())
