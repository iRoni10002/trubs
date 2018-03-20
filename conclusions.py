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
							 QScrollArea, QDialog, QFrame, QLineEdit, QGridLayout)
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
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

class MainConclusion(QWidget):

	def __init__(self, expansion, s_number):
		super().__init__()
		print('xrp')
		self.expansion = expansion
		print('otladka', s_number)
		self.s_number = s_number
		print(self.s_number)
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
		
				
		layout = QGridLayout()
		
		
		
		self.scroll = QScrollArea()
		self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.scroll.setWidgetResizable(True)
		self.scroll.setStyleSheet("border: 1px solid transparent; background-color: transparent;")
		#tt = MainWindow()
		#gg = QWidget()
		#gg.setLayout(v_host)
		self.w = self.width()
		for i in Hosts.select().where(Hosts.owner == self.s_number):
			if j%2 == 0:
				host = ListConclusion('1', self.w)
			else:
				host = ListConclusion('0', self.w)
			host.move(-300, -300)
			h_host.addWidget(host)
			v_host.addLayout(h_host)
			#v_host.setSpacing(0)
			j += 1
			h_host = QHBoxLayout()
		
		db.close()
		gg = QWidget()
		gg_h = QHBoxLayout()
		gg_h.setSpacing(0)
		gg_h.addLayout(v_host)
		gg.setLayout(gg_h)
		self.scroll.setWidget(gg)
		#self.scroll.setLayout(v_host)
		print('otladka')
		title = QLabel(self.s_number)
		buttons_left = QHBoxLayout()
		buttons_left.addWidget(backButton)
		buttons_left.addWidget(addInstitutionButton)
		buttons_right = QHBoxLayout()
		buttons_right.addWidget(updateButton)
		buttons_right.addWidget(exitButton)
		print('otladka0')
		tit_h = QHBoxLayout()
		tit_h.addLayout(buttons_left)
		tit_h.addStretch(1)
		tit_h.addWidget(title)
		tit_h.addStretch(1)
		tit_h.addLayout(buttons_right)
		
		vv = QVBoxLayout()
		vv.setAlignment(Qt.AlignTop)
		vv.addLayout(tit_h)
		ff = QWidget()
		
		number = QLabel('number')
		#number.setStyleSheet("color: red; background-color: green; font-size: 10px; margin: 100px;")
		name = QLabel('name')
		mark = QLabel('mark')
		icon = QLabel('icon')
		period = QLabel('period')
		mark_of_steel = QLabel('mark of steel')

		block_h = QHBoxLayout()
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
		lbl = QLabel('')
		lbl.setFixedWidth(10)
		block_h.setSpacing(1)
		#block_h.addWidget(lbl)
		
		hh = QVBoxLayout()
		hh.addLayout(block_h)
		
		m_host = ListConclusion('1', self.w)
		ff.setStyleSheet("border: 1px solid transparent; font-size: 14px; font-family: Verdana; background-color: white;")
		ss = "QLabel {border: 1px solid black;}"
		ff.setFixedWidth(865)
		print('otladka0')
		m_host.setFixedHeight(60)
		print('otladka0')
		m_host_h = QHBoxLayout()
		m_host_h.addWidget(m_host)
		lbl.setStyleSheet("background-color: transparent;")
		print('otladka0')
		ff.setLayout(hh)
		h = QHBoxLayout()
		h.setAlignment(Qt.AlignHCenter)
		h.addWidget(ff)
		h.addWidget(lbl)
		#ff.setStyleSheet(ss)
		vv.addLayout(h)
		vv.addWidget(self.scroll)
		print('otladka')
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
		self.main = CreateConclusion(self.institution_name)
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
		self.add = CreateConclusion(self.institution_name)
		print("ALL GOOD, KIDDO")
	def open_city(self):
		self.text = self
		print("xxxxx: ", self.text)
		self.city = City('gg')

class ListConclusion(QPushButton):
	def __init__(self, color, width):
		super().__init__()
		#self.institution = institution
		#self.brand = brand
		self.color = color
		self.w = width
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
		
		number = QLabel('number')
		number.setFixedWidth(80)
		#number.setStyleSheet("color: red; background-color: green; font-size: 10px; margin: 100px;")
		name = QLabel('name')
		mark = QLabel('mark')
		icon = QPushButton('icon')
		icon.setFixedWidth(40)
		period = QLabel('period')
		mark_of_steel = QLabel('mark of steel')

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
		block_h.setSpacing(50)

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
		
		frame = QFrame()
		frame.setFrameShape(QFrame.Panel)
		frame.setFrameShadow(QFrame.Sunken)
		frame.setLayout(block_h)
		#frame.setStyleSheet("padding: 10px;")
		x = QVBoxLayout()
		x.addWidget(frame)
		self.setLayout(x)
		#self.setLayout(self.city_h)
		self.setFixedSize(900, 65)
		self.setWindowTitle('Добавление города')
		self.show()
	def open_unit(self):
		self.unit = CreateConclusion(self.institution)

class CreateConclusion(QWidget):

	def __init__(self, institution):
		super().__init__()
		self.institution_name = institution
		print("[ojl")
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
		print("ggghhhggg")
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

	def create_host(self):
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
	ex = ListInstitution('jopa', 'jpa')
	sys.exit(app.exec_())

