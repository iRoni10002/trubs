#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit, QComboBox)
from PyQt5.QtGui import *
import sqlite3
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QDockWidget, QLabel,
                             QScrollArea, QDialog, QFrame, QLineEdit)
from PyQt5 import QtGui
from PyQt5.QtGui import *
import pickle
import sqlite3
from db_manger import *
from host import *

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

class MainUnit(QWidget):

    def __init__(self, expansion, institution):
        super().__init__()
        print('xrp')
        self.expansion = expansion
        self.institution_name = institution
        print(self.institution_name)
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
        #backButton.clicked.connect()
        
        db = SqliteDatabase('mydb.db')
        db.connect()
        j = 0
        g = 0
        h_city = QHBoxLayout()
        v_city = QVBoxLayout()
        v_city.setSpacing(0)
        for i in Units.select().where(Units.owner == self.institution_name):
            if j == 3:
                v_city.addLayout(h_city)
                h_city = QHBoxLayout()
                unit = ListUnit(i.owner, i.brand, self.expansion)
                unit.setObjectName(i.s_number)
                unit.move(-300, -300)
                v_city.addLayout(h_city)
                j = 0
            else:
                unit = ListUnit(i.owner, i.brand, self.expansion)
                unit.setObjectName(i.s_number)
                unit.move(-300, -300)
            h_city.addWidget(unit)
            j += 1
            g += 1
        if g < 4:
            v_city.addLayout(h_city)
        print("bbbbbbbb-------bbbb")
        db.close()
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("border: 1px solid transparent; background-color: transparent;")
        #tt = MainWindow()
        gg = QWidget()
        gg.setLayout(v_city)
        self.scroll.setWidget(gg)
        
        title = QLabel(self.institution_name)
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
        
        title.setStyleSheet("background-color: rgba(255, 255, 255, 0.5); color: black;"
                            "border: 3px solid transparent;"
                            "padding: 10px 300% 10px 300%;"
                            "margin-top: 0px;"
                            "font-size: 30px; font-family: Verdana;")
        addInstitutionButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); padding: 12px;")
        updateButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); padding: 12px;")
        backButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); padding: 12px;")
        exitButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); padding: 12px;")
        
        self.setLayout(vv)
        self.update()
        p = QPalette()
        gradient = QLinearGradient(0, 0, 120, 400)
        gradient.setColorAt(0.0, QColor(117,160,252))
        gradient.setColorAt(1.0, QColor(193,203,253))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
        print(self.expansion)
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
    def update_window(self):
        self.screen = UpdateScreen(self.expansion)
        self.main = CreateUnit(self.institution_name)
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
        self.add = CreateUnit(self.institution_name)
        print("ALL GOOD, KIDDO")
    def open_city(self):
        self.text = self
        self.city = City('gg')

class ListUnit(QPushButton):
    def __init__(self, institution, brand, expansion):
        super().__init__()
        self.institution = institution
        self.brand = brand
        self.expansion = expansion
        self.initUI()

    def initUI(self):

        self.okButton = QPushButton('+')
        #okButton.clicked.connect(self.create_city)
        #okButton.clicked.connect(self.main.update())
        
        pixmap = QPixmap('image/kotel_2.png')
        pixmap_new = pixmap.scaled(100, 100)
        icon = QLabel()
        icon.setPixmap(pixmap_new)
        self.city = QLabel(self.institution)
        title = QLabel(self.brand)
        count = QLabel('кол-во агрегатов')
        
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
        print('otladka----', self.objectName())
        x = self.expansion
        print('otladka--')
        y = self.objectName()
        print('otladka-')
        self.hosts = MainHost(x, y)
    def open_unit(self):
        self.unit = CreateUnit(self.institution)

class CreateUnit(QWidget):

    def __init__(self, institution):
        super().__init__()
        self.institution_name = institution
        print("[uy")
        self.initUI()

    def initUI(self):

        addInstitutionButton = QPushButton('')
        addInstitutionButton.setIcon(QIcon('image/plus_2.png'))
        addInstitutionButton.setIconSize(QSize(55, 55))
        addInstitutionButton.clicked.connect(self.create_unit)
        
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
        button_h = QHBoxLayout()
        button_h.addStretch(1)
        button_h.addWidget(addInstitutionButton)
        button_h.addStretch(1)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Добавление города')
        self.setFixedSize(300, 150)
        self.show()

        style = "QLabel {" \
                "color: black; font-family: Verdana; font-size: 20px;" \
                "}" \
                "QLineEdit {" \
                "color: black; background-color: rgb(193,203,253); font-family: Verdana; font-size: 20px;" \
                "border-radius: 0px; " \
                "}" \
                "QPushButton {" \
                "background-color: rgba(255, 255, 255, 0.3);" \
                "margin: 0px -2px 0px -2px; border-radius: 20px;" \
                "}"

        
        self.setStyleSheet(style)
        
        vbox = QVBoxLayout()
        vbox.addLayout(brand_h)
        vbox.addLayout(type_h)
        vbox.addLayout(station_number_h)
        vbox.addLayout(reg_number_h)
        vbox.addLayout(button_h)
        
        self.setLayout(vbox)

        p = QPalette()
        gradient = QLinearGradient(0, 0, 120, 400)
        gradient.setColorAt(0.0, QColor(117,160,252))
        gradient.setColorAt(1.0, QColor(193,203,253))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Log in')
        self.setFixedSize(500, 250)
        self.show()

    def create_unit(self):
        brand = self.brandEdit.text()
        type = self.typeEdit.text()
        r_number = self.reg_numberEdit.text()
        s_number = self.station_numberEdit.text()
        
        db = SqliteDatabase('mydb.db')
        db.connect()
        
        unit = Units.create(owner=self.institution_name, brand=brand, type=type, s_number=s_number, r_number=r_number, count_hosts=0, is_relative=True)
        
        db.close()
        
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ListInstitution('', '')
    sys.exit(app.exec_())

