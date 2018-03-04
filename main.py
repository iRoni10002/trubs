#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *
from reg_form import Reg
from city import City
import sqlite3

class MainWidget(QWidget):

    def __init__(self, expansion):
        super().__init__()
        self.expansion = expansion
        self.initUI()

    def initUI(self):
        add_city = QPushButton('+')
        add_city.clicked.connect(self.addCity)
        #add_city.clicked.connect(self.update)
        #exitAction = QAction('&Exit', self)
        #exitAction.setShortcut('Ctrl+Q')
        #exitAction.setStatusTip('Exit application')
        #exitAction.triggered.connect(qApp.quit)
        #self.statusBar()
        ##print("gg")
        #menubar = self.menuBar()
        #regMenu = menubar.addMenu('&Регистрация')
        #viewMenu = menubar.addMenu('&Просмотр')
        #redMenu = menubar.addMenu('&Исправления')
       # svdMenu = menubar.addMenu('&Сводки')
        #sprMenu = menubar.addMenu('&Справочники')
        #srvMenu = menubar.addMenu('&Сервис')
        #qMenu = menubar.addMenu('&Выход')
       # qMenu.addAction(exitAction)
      #  regMenu.addAction('&REg', self.open_reg)
       # #ggMenu.addAction("jjj")

       # menubar.setStyleSheet("background-color: white;")

        self.w = self.calc_expansion_w(self.expansion)
        self.h = self.calc_expansion_h(self.expansion)

        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 400)
        gradient.setColorAt(0.0, QColor(240, 240, 240))
        gradient.setColorAt(1.0, QColor(240, 2, 27))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        conn = sqlite3.connect('mydatabase.db')
        print('good')
        cursor = conn.cursor()
        print('good')
        cursor.execute("SELECT * FROM city")
        print('good')
        y = cursor.fetchall()
        print('good-length', len(y), y[0], y[1])
        h = QHBoxLayout()
        btn_h = QHBoxLayout()
        btn_h.addStretch(1)
        btn_h.addWidget(add_city)
        for i in range(len(y)):
            x = y[i]
            btn = self.draw_city(x[0])
            print(btn)
            h.addWidget(btn)

        blocv = QVBoxLayout()
        blocv.addStretch(1)
        blocv.addLayout(h)
        blocv.addStretch(1)
        blocv.addLayout(btn_h)
        self.setLayout(blocv)
        self.update()
        self.setGeometry(0, 30, self.w, self.h)
        self.setWindowTitle('Menubar')
        self.show()

    def open_reg(self):
        self.reg = Reg(self.w, self.h)
    def calc_expansion_w(self, expansion):
        w = expansion.split('*')
        W = int(w[0])
        return W
    def calc_expansion_h(self, expansion):
        h = expansion.split('*')
        H = int(h[1])
        return H
    def draw_city(self, name):
        print("start")
        self.btn = QPushButton(name)
        self.btn.clicked.connect(self.open_city)
        print("end")
        return self.btn
    def addCity(self):
        from city import CreateCity
        self.city = CreateCity()
        self.update()
    def open_city(self):
        self.text = self
        print("xep: ", self.text)
        self.city = City('gg')

class Main(QMainWindow):

    def __init__(self, expansion):
        super().__init__()
        self.expansion = expansion
        self.initUI()

    def initUI(self):
        self.w = self.calc_expansion_w(self.expansion)
        self.h = self.calc_expansion_h(self.expansion)
        self.btn = QPushButton('jmyak')
        self.g = QVBoxLayout()
        self.g.addWidget(self.btn)
        self.severniy = MainWidget(self.expansion)
        print("1")
        self.btn.resize(100, 100)
        self.btn.move(100, 100)
        self.btn.show()
        self.setCentralWidget(self.severniy)
        self.setLayout(self.g)
        print("2")
        self.update()
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 400)
        gradient.setColorAt(0.0, QColor(240, 240, 240))
        gradient.setColorAt(1.0, QColor(240, 2, 27))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
        print("3")
        self.setGeometry(0, 30, self.w, self.h)
        print("4")
        self.setWindowTitle('Menubar')
        print("5")
        self.show()
        print("6")

    def calc_expansion_w(self, expansion):
        w = expansion.split('*')
        W = int(w[0])
        return W
    def calc_expansion_h(self, expansion):
        h = expansion.split('*')
        H = int(h[1])
        return H
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
