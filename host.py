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
                             QScrollArea, QDialog, QFrame, QLineEdit, QFormLayout)
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
import pickle
import sqlite3
from conclusions import *
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

class IconScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        icon = QPushButton()
        icon.setIcon(QIcon('image/icon.png'))
        icon.setIconSize(QSize(400, 400))
        icon.setStyleSheet("border: none;")
        self.setCentralWidget(icon)
        self.setFixedSize(500, 500)
        self.setWindowTitle('Menubar')
        self.show()
        self.setWindowTitle('Menubar')
        self.show()

class MainHost(QWidget):

    def __init__(self, expansion, s_number):
        super().__init__()
        self.expansion = expansion
        print('otladka', s_number)
        self.s_number = s_number
        print(self.s_number)
        self.initUI()

    def initUI(self):
        addInstitutionButton = QPushButton('')
        addInstitutionButton.setIcon(QIcon('image/plus_2.png'))
        addInstitutionButton.setIconSize(QSize(75, 75))
        addInstitutionButton.clicked.connect(self.addHost)
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
    
        j = 0
        h_host = QHBoxLayout()
        v_host = QVBoxLayout()
        v_host.setSpacing(0)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("border: 1px solid transparent; background-color: transparent;")
      
        self.w = self.width()
        
        form = QFormLayout()
        
        db = SqliteDatabase('mydb.db')
        db.connect()
        for i in Hosts.select().where(Hosts.owner == self.s_number):
            arr = [i.owner, i.number, i.name, i.mark, i.icon, i.period, i.mark_of_steel]
            print(arr)
            if j%2 == 0:
                host = ListHost('1', self.w, arr, self.expansion)
                host.setObjectName(i.number)
            else:
                host = ListHost('0', self.w, arr, self.expansion)
                host.setObjectName(i.number)
            host.move(-300, -300)
            form.addRow(host)
            j += 1
        
        db.close()
        
        host_list = QWidget()
        host_list.setLayout(form)
        
        self.scroll.setWidget(host_list)
        
        title = QLabel(self.s_number)
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
        
        number = QLabel('Номер')
        number.setAlignment(Qt.AlignCenter)
        #number.setStyleSheet("color: red; background-color: green; font-size: 10px; margin: 100px;")
        name = QLabel('Название')
        name.setAlignment(Qt.AlignCenter)
        mark = QLabel('Марка')
        mark.setAlignment(Qt.AlignCenter)
        icon = QLabel('Схема')
        icon.setAlignment(Qt.AlignCenter)
        period = QLabel('Наработка')
        period.setAlignment(Qt.AlignCenter)
        mark_of_steel = QLabel('Марка стали')
        mark_of_steel.setAlignment(Qt.AlignRight)

        block_h = QHBoxLayout()
        block_h.setAlignment(Qt.AlignCenter)
        block_h.addWidget(number)
        block_h.addStretch(1)
        block_h.addWidget(name)
        block_h.addStretch(1)
        block_h.addWidget(mark)
        block_h.addStretch(1)
        block_h.addWidget(period)
        block_h.addStretch(1)
        block_h.addWidget(mark_of_steel)
        block_h.addStretch(1)
        block_h.addWidget(icon)
        block_h.addStretch(1)
        
        h = QHBoxLayout()
        h.setAlignment(Qt.AlignCenter)
        h.addLayout(block_h)
     
        arr = ['ff', 'Номер', 'Имя', 'Марка', 'Схема', 'Наработка', 'Марка стали']
        dd = ListHost('1', self.w, arr, self.expansion)
        dd.setStyleSheet("QLabel {font-size: 14px; font-family: Verdana; "
                         "color: black;}"
                         "QPushButton {font-size: 14px; font-family: Verdana; "
                         "color: black; background-color: rgba(255, 255, 255, 0.9);}")
        
        scroll_mini = QScrollArea()
        scroll_mini.setFixedHeight(45)
        scroll_mini.setWidgetResizable(True)
        scroll_mini.setStyleSheet("border: 1px solid transparent; background-color: transparent;")
        scroll_mini.setWidget(dd)
        
        vv = QVBoxLayout()
        vv.addLayout(tit_h)
        vv.addWidget(scroll_mini)
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
        
        if self.expansion == '1':
            self.showFullScreen()
        else:
            self.setGeometry(0, 30, 800, 600)
            
        self.setWindowTitle('Menubar')
        self.show()
    def addHost(self):
        self.add = CreateHost(self.s_number)
    def back(self):
        self.close()
    def exit(self):
        quit()
    def update_window(self):
        self.screen = UpdateScreen(self.expansion)
        self.main = MainHost(self.expansion, self.s_number)
        self.close()
        self.screen.close()

class ListHost(QPushButton):
    def __init__(self, color, width, data, expansion):
        super().__init__()
        self.color = color
        self.w = width
        self.expansion = expansion
        
        self.owner = data[0]
        self.number = data[1]
        self.name = data[2]
        self.mark = data[3]
        self.icon = data[4]
        self.period = data[5]
        self.mark_of_steel = data[6]
        
        self.initUI()

    def initUI(self):

        self.okButton = QPushButton('+')
        #okButton.clicked.connect(self.create_city)
        #okButton.clicked.connect(self.main.update())
        
        #pixmap = QPixmap('image/uch.png')
        #pixmap_new = pixmap.scaled(100, 100)
        #icon = QLabel()
        #icon.setPixmap(pixmap_new)
        #self.city = QLabel(self.institution)
        #title = QLabel(self.brand)
        #count = QLabel('кол-во агрегатов')
        
        number = QLabel(self.number)
        number.setAlignment(Qt.AlignCenter)
        name = QLabel(self.name)
        name.setAlignment(Qt.AlignCenter)
        mark = QLabel(self.mark)
        mark.setAlignment(Qt.AlignCenter)
        icon = QPushButton()
        icon.setFixedWidth(50)
        icon.setContentsMargins(0,0,0,0)
        icon.setIcon(QIcon('image/icon.png'))
        icon.setIconSize(QSize(43, 25))
        icon.clicked.connect(self.open_icon)
        period = QLabel(self.period)
        period.setAlignment(Qt.AlignCenter)
        mark_of_steel = QLabel(self.mark_of_steel)
        mark_of_steel.setAlignment(Qt.AlignCenter)

        block_h = QHBoxLayout()
        #block_h.setAlignment(Qt.AlignLeft)
        block_h.addWidget(number)
        #block_h.addStretch(1)
        block_h.addWidget(name)
        #block_h.addStretch(1)
        block_h.addWidget(mark)
        #block_h.addStretch(1)
        #block_h.addStretch(1)
        block_h.addWidget(period)
        #block_h.addStretch(1)
        block_h.addWidget(mark_of_steel)
        block_h.addWidget(icon)
        #block_h.setSpacing(50)

        self.okButton.setStyleSheet("background-color: rgba(100, 0, 100, 100); color: white;"
                                    "font-family: Verdana; font-size: 16px;"
                                    "margin: 0px 10px 0px 10px;"
                                    "border-radius: 20px;")
        
        if self.color == '1':
            style = "QPushButton {background-color: rgba(255, 255, 255, 0.9);}"
        else:
            style = "QPushButton {background-color: rgba(255, 255, 255, 0.6)};"
        
        style_label = "QLabel {font-size: 14px; font-family: Verdana; " \
                      "color: black; border: 3px solid transparent; border-right-color: rgba(0, 0, 0, 0.5);}" \
                      "QPushButton {font-size: 14px; font-family: Verdana; " \
                      "color: black;}"
                
        style_label = style_label + style
        
        self.setStyleSheet(style_label)
        
        icon.setStyleSheet("background-color: transparent;")
        
        self.clicked.connect(self.next)
        
        self.setLayout(block_h)
        self.setFixedHeight(43)
        self.setWindowTitle('Добавление города')
        self.show()
    def open_icon(self):
        self.icon = IconScreen()
    def next(self):
        self.concl = Concls(self.expansion, self.objectName())
    def open_unit(self):
        self.unit = CreateHost(self.institution)

class CreateHost(QWidget):

    def __init__(self, unit):
        super().__init__()
        self.unit_name = unit
        self.initUI()

    def initUI(self):

        addInstitutionButton = QPushButton('')
        addInstitutionButton.setIcon(QIcon('image/plus_2.png'))
        addInstitutionButton.setIconSize(QSize(55, 55))
        addInstitutionButton.clicked.connect(self.create_host)
        
        self.number = QLineEdit()
        self.name = QLineEdit()
        self.mark = QLineEdit()
        self.icon = QPushButton()
        self.icon.setFixedWidth(50)
        self.icon.setContentsMargins(0,0,0,0)
        self.icon.setIcon(QIcon('image/icon.png'))
        self.icon.setIconSize(QSize(43, 25))
        self.icon.clicked.connect(self.open_icon)
        self.period = QLineEdit()
        self.mark_of_steel = QLineEdit()
        print("gg")
        form = QFormLayout()
        print("gg")
        form.addRow(QLabel('Агрегат №'), QLabel(self.unit_name))
        form.addRow(QLabel('Номер'), self.number)
        form.addRow(QLabel('Название'), self.name)
        form.addRow(QLabel('Марка'), self.mark)
        form.addRow(QLabel('Схема'), self.icon)
        form.addRow(QLabel('Период'), self.period)
        form.addRow(QLabel('Марка стали'), self.mark_of_steel)
        
        button_h = QHBoxLayout()
        button_h.addStretch(1)
        button_h.addWidget(addInstitutionButton)
        button_h.addStretch(1)
        
        form.addRow(button_h)
        
        self.setLayout(form)

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

        p = QPalette()
        gradient = QLinearGradient(0, 0, 120, 400)
        gradient.setColorAt(0.0, QColor(117,160,252))
        gradient.setColorAt(1.0, QColor(193,203,253))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Log in')
        self.show()

    def open_icon(self):
        self.icon = IconScreen()
    def create_host(self):
        number = self.number.text()
        name = self.name.text()
        mark = self.mark.text()
        icon = 'g'
        period = self.period.text()
        mark_of_steel = self.mark_of_steel.text()
        db = SqliteDatabase('mydb.db')
        db.connect()
        host = Hosts.create(owner=self.unit_name, number=number, name=name, mark=mark, icon=icon, period=period, mark_of_steel=mark_of_steel)
        
        db.close()
        
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ListInstitution('', '')
    sys.exit(app.exec_())

