import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QWidget,
							 QDockWidget, QLabel,
							 QScrollArea, QDialog, QTabWidget, QFormLayout, QLineEdit)
from PyQt5 import QtGui
from PyQt5.QtGui import *
from peewee import *
from db_manger import *

from city import *


class Search(QWidget):
	def __init__(self, expansion):
		super().__init__()
		self.expansion = expansion
		self.initUI()
	
	def initUI(self):
		
		backButton = QPushButton('')
		backButton.setIcon(QIcon('image/back_2.png'))
		backButton.setIconSize(QSize(75, 75))
		backButton.clicked.connect(self.back)
		
		tab = QTabWidget()
		tab.setTabPosition(QTabWidget.South)
		
		self.city_name = QLineEdit()
		
		cities = QWidget()
		form_cities = QFormLayout()
		form_cities.setAlignment(Qt.AlignVCenter)
		form_cities.addRow(QLabel('Название города'), self.city_name)
		cities.setLayout(form_cities)
		
		tab.addTab(cities, 'Города')
		
		btn = QPushButton('xii')
		btn.clicked.connect(self.search_city)
		
		btn_h = QHBoxLayout()
		btn_h.addStretch(3)
		btn_h.addWidget(backButton)
		
		hh = QHBoxLayout()
		hh.addStretch(1)
		hh.addWidget(tab, 3)
		hh.addStretch(1)
		
		vv = QVBoxLayout()
		vv.addLayout(btn_h)
		vv.addStretch(1)
		vv.addLayout(hh)
		vv.addStretch(1)
		vv.addWidget(btn)
		
		self.setLayout(vv)
		
		style = "QTabWidget {background-color: rgb(117, 160, 252); font-size: 30px;}" \
				"QLabel {background-color: transparent; font-size: 20px;}" \
				"QLineEdit {background-color: white; font-size: 20px; border: 1px solid transparent; margin: 0px;}"
		backButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); padding: 12px;")
		
		self.setStyleSheet(style)
		tab.setStyleSheet("background-color: rgb(117, 160, 252);")
		
		p = QPalette()
		gradient = QLinearGradient(0, 0, 120, 400)
		gradient.setColorAt(0.0, QColor(117, 160, 252))
		gradient.setColorAt(1.0, QColor(193, 203, 253))
		p.setBrush(QPalette.Window, QBrush(gradient))
		self.setPalette(p)
		if self.expansion == '1':
			self.showFullScreen()
		else:
			self.setGeometry(0, 30, 800, 600)
			self.setFixedSize(800, 600)
		self.setWindowTitle('Menubar')
		self.show()
		
	def back(self):
		self.close()
	def search_city(self):
		self.city = SearchCity(self.expansion, self.city_name.text())
		
class SearchCity(QWidget):
	def __init__(self, expansion, name):
		super().__init__()
		self.expansion = expansion
		self.city_name = name
		self.initUI()
	
	def initUI(self):
		
		backButton = QPushButton('')
		backButton.setIcon(QIcon('image/back_2.png'))
		backButton.setIconSize(QSize(75, 75))
		backButton.clicked.connect(self.back)
		
		db = SqliteDatabase('mydb.db')
		db.connect()
		j = 0
		g = 0
		h_city = QHBoxLayout()
		v_city = QVBoxLayout()
		v_city.setSpacing(10)
		for i in City.select().where(City.name == self.city_name):
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
		
		self.title = QLabel("Результаты поиска")
		tit_h = QHBoxLayout()
		tit_h.addWidget(self.title, 20)
		tit_h.addWidget(backButton, 1)
		
		vv = QVBoxLayout()
		vv.addLayout(tit_h)
		vv.addWidget(self.scroll)
		
		self.title.setStyleSheet("background-color: rgba(255, 255, 255, 0.5); color: black;"
								 "border: 3px solid transparent;"
								 "padding: 10px 0px 10px 0px;"
								 "margin-top: 0px;"
								 "font-size: 30px; font-family: Verdana;")
		backButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); padding: 12px;")
		
		self.setLayout(vv)
		
		p = QPalette()
		gradient = QLinearGradient(0, 0, 120, 400)
		gradient.setColorAt(0.0, QColor(117, 160, 252))
		gradient.setColorAt(1.0, QColor(193, 203, 253))
		p.setBrush(QPalette.Window, QBrush(gradient))
		self.setPalette(p)
		if self.expansion == '1':
			self.showFullScreen()
		else:
			self.setGeometry(0, 30, 800, 600)
			self.setFixedSize(800, 600)
		self.setWindowTitle('Menubar')
		self.show()
		
	def back(self):
		self.close()
	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Search('1')
	sys.exit(app.exec_())
