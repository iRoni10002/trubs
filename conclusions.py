import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QWidget,
							 QDockWidget, QLabel,
							 QScrollArea, QDialog, QFrame, QLineEdit, QGridLayout, QFormLayout, QTabWidget)
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
		gradient.setColorAt(0.0, QColor(117, 160, 252))
		gradient.setColorAt(1.0, QColor(193, 203, 253))
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

class Concl(QWidget):
	def __init__(self, data, expansion):
		super().__init__()
		self.expansion = expansion
		
		self.owner = data[0]
		self.number = data[1]
		self.type = data[2]
		self.name = data[3]
		self.reason = data[4]
		self.recommendation = data[5]
		self.photo = data[6]
		self.concls = data[7]
		self.date_z = data[8]
		self.date_v = data[9]
		self.date_d = data[10]
		self.text = data[11]
		
		self.initUI()
	
	def initUI(self):
		
		addHost = QPushButton()
		addHost.setFixedSize(40, 40)
		addHost.setIcon(QIcon('image/plus.png'))
		addHost.setIconSize(QSize(30, 30))
		textConcl = QPushButton()
		textConcl.setFixedSize(40, 40)
		textConcl.setIcon(QIcon('image/photo.png'))
		textConcl.setIconSize(QSize(30, 30))
		photoConcl = QPushButton()
		photoConcl.setFixedSize(40, 40)
		photoConcl.setIcon(QIcon('image/text.png'))
		photoConcl.setIconSize(QSize(30, 30))
		
		number = QLabel(self.number)
		number.setAlignment(Qt.AlignCenter)
		number.setFixedHeight(40)
		type = QLabel(self.type)
		type.setAlignment(Qt.AlignCenter)
		type.setFixedHeight(40)
		name = QLabel(self.name)
		name.setAlignment(Qt.AlignCenter)
		name.setFixedHeight(40)
		date_z = QLabel(self.date_z)
		date_z.setAlignment(Qt.AlignCenter)
		date_z.setFixedHeight(40)
		date_v = QLabel(self.date_v)
		date_v.setAlignment(Qt.AlignCenter)
		date_v.setFixedHeight(40)
		date_d = QLabel(self.date_d)
		date_d.setAlignment(Qt.AlignCenter)
		date_d.setFixedHeight(40)
		
		reason = QPushButton('Причина')
		reason.setFixedHeight(40)
		recommendation = QPushButton('Рекомендации')
		recommendation.setFixedHeight(40)
		conc = QPushButton('Выводы')
		conc.setFixedHeight(40)
		
		description1 = QLabel(self.reason)
		description1.setFixedHeight(50)
		description2 = QLabel(self.recommendation)
		description2.setFixedHeight(50)
		description3 = QLabel(self.concls)
		description3.setFixedHeight(50)
		
		form = QFormLayout()
		
		description_h1 = QHBoxLayout()
		description_h1.addWidget(description1)
		description_h2 = QHBoxLayout()
		description_h2.addWidget(description2)
		description_h3 = QHBoxLayout()
		description_h3.addWidget(description3)
		
		top_h = QHBoxLayout()
		top_h.addWidget(number)
		top_h.addWidget(type)
		top_h.addWidget(name)
		top_h.addWidget(date_z)
		top_h.addWidget(date_v)
		top_h.addWidget(date_d)
		top_h.addWidget(addHost)
		top_h.addWidget(textConcl)
		top_h.addWidget(photoConcl)
		
		'''bottom_h = QHBoxLayout()
		bottom_h.addWidget(reason)
		bottom_h.addWidget(recommendation)
		bottom_h.addWidget(conc)
		
		button_h = QHBoxLayout()
		button_v = QVBoxLayout()
		button_h.addWidget(addHost)
		button_h.addWidget(textConcl)
		button_h.addWidget(photoConcl)
		button_v.addLayout(button_h)
		
		feilds_v = QVBoxLayout()
		feilds_v.addLayout(top_h)
		feilds_v.addLayout(bottom_h)
		
		header_h = QHBoxLayout()
		header_h.addLayout(feilds_v)
		header_h.addLayout(button_v)
		
		bloc_v = QVBoxLayout()
		bloc_v.setSpacing(0)
		bloc_v.addLayout(header_h)
		bloc_v.addLayout(description_h)
		
		bloc = QHBoxLayout()
		bloc.addLayout(bloc_v)
		
		frame = QFrame()
		frame.setLayout(bloc)
		frame.setFixedHeight(150)
		
		x = QHBoxLayout()
		x.addWidget(frame)'''
		
		w1 = QWidget()
		w1.setFixedHeight(50)
		w2 = QWidget()
		w2.setFixedHeight(50)
		w3 = QWidget()
		w3.setFixedHeight(50)
		w1.setLayout(description_h1)
		w2.setLayout(description_h2)
		w3.setLayout(description_h3)
		
		tab = QTabWidget()
		tab.setTabPosition(QTabWidget.South)
		tab.addTab(w1, '  ')
		tab.addTab(w2, '  ')
		tab.addTab(w3, '  ')
		
		form.setSpacing(0)
		form.addRow(top_h)
		form.addRow(tab)
		
		self.setLayout(form)
		
		'''style = "QLabel {background-color: rgba(255, 255, 255, 0.9); font-size: 14px;}" \
				"QPushButton {background-color: rgba(255, 255, 0, 0.9); font-size: 14px;" \
				"border: 1px dashed transparent; border-top-color: black;}"
		'''
		self.setStyleSheet("background-color: rgba(255, 255, 255, 0.6);")
		#self.setStyleSheet("border: 1px solid red;")
		tab.setStyleSheet("background-color: rgba(255, 255, 255, 0.6;")
		
		#description.setStyleSheet("background-color: rgba(255, 255, 255, 0.6);"
								  #"border: 1px solid transparent; border-top-color: rgba(0, 0, 0, 0.5);")
		
		if self.expansion == '1':
			self.showFullScreen()
		else:
			self.setGeometry(0, 30, 800, 600)
		self.setWindowTitle('Menubar')
		self.show()

class Concls(QWidget):
	def __init__(self, expansion, number):
		super().__init__()
		self.expansion = expansion
		self.number = number
		# print('otladka', s_number)
		# self.s_number = s_number
		# print(self.s_number)
		self.initUI()
	
	def initUI(self):
		addInstitutionButton = QPushButton('')
		addInstitutionButton.setIcon(QIcon('image/plus_2.png'))
		addInstitutionButton.setIconSize(QSize(75, 75))
		addInstitutionButton.clicked.connect(self.addConcl)
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
		
		title = QLabel(self.number)
		buttons_left = QHBoxLayout()
		buttons_left.addWidget(backButton)
		buttons_left.addWidget(addInstitutionButton)
		buttons_right = QHBoxLayout()
		buttons_right.addWidget(updateButton)
		buttons_right.addWidget(exitButton)
		
		title.setStyleSheet("background-color: rgba(255, 255, 255, 0.5); color: black;"
							"border: 3px solid transparent;"
							"padding: 10px 300% 10px 300%;"
							"margin-top: 0px;"
							"font-size: 30px; font-family: Verdana;")
		addInstitutionButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); padding: 12px;")
		updateButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); padding: 12px;")
		backButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); padding: 12px;")
		exitButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); padding: 12px;")
		
		tit_h = QHBoxLayout()
		tit_h.addLayout(buttons_left)
		tit_h.addStretch(1)
		tit_h.addWidget(title)
		tit_h.addStretch(1)
		tit_h.addLayout(buttons_right)
		
		addHost = QPushButton()
		addHost.setFixedSize(40, 40)
		addHost.setIcon(QIcon('image/plus.png'))
		addHost.setIconSize(QSize(40, 40))
		textConcl = QPushButton()
		textConcl.setFixedSize(40, 40)
		textConcl.setIcon(QIcon('image/photo.png'))
		textConcl.setIconSize(QSize(40, 40))
		photoConcl = QPushButton()
		photoConcl.setFixedSize(40, 40)
		photoConcl.setIcon(QIcon('image/text.png'))
		photoConcl.setIconSize(QSize(40, 40))
		
		number = QLabel('Номер')
		number.setAlignment(Qt.AlignCenter)
		number.setFixedHeight(40)
		type = QLabel('Тип заключения')
		type.setAlignment(Qt.AlignCenter)
		type.setFixedHeight(40)
		name = QLabel('Имя')
		name.setAlignment(Qt.AlignCenter)
		name.setFixedHeight(40)
		date_z = QLabel('Дата заявки')
		date_z.setAlignment(Qt.AlignCenter)
		date_z.setFixedHeight(40)
		date_v = QLabel('Дата выдачи')
		date_v.setAlignment(Qt.AlignCenter)
		date_v.setFixedHeight(40)
		date_d = QLabel('Дата разрушения')
		date_d.setAlignment(Qt.AlignCenter)
		date_d.setFixedHeight(40)
		top_h = QHBoxLayout()
		top_h.addWidget(number)
		top_h.addWidget(type)
		top_h.addWidget(name)
		top_h.addWidget(date_z)
		top_h.addWidget(date_v)
		top_h.addWidget(date_d)
		top_h.addWidget(addHost)
		top_h.addWidget(textConcl)
		top_h.addWidget(photoConcl)
		
		j = 0
		v_host = QVBoxLayout()
		v_host.setSpacing(0)
		
		scroll = QScrollArea()
		scroll.setWidgetResizable(True)
		scroll.setStyleSheet("border: none; background-color: transparent;")
		
		scroll_mini = QScrollArea()
		scroll_mini.setWidgetResizable(True)
		scroll_mini.setStyleSheet("border: 1px solid transparent; background-color: transparent;")
		
		ii = QWidget()
		ii.setStyleSheet("QWidget {background-color: rgba(255, 255, 255, 0.6);}"
						 "QLabel {background-color: transparent;}"
						 "QPushButton {background-color: transparent; border-radius: 10px;}")
		ii.setFixedHeight(65)
		ii.setLayout(top_h)
		
		scroll_mini.setWidget(ii)
		
		self.w = self.width()
		
		form = QFormLayout()
		db = SqliteDatabase('mydb.db')
		db.connect()
		for i in Conclusions2.select().where(Conclusions2.owner == self.number):
			arr = [i.owner, i.number, i.type, i.name, i.reason, i.recommendation, i.photo, i.conclusions, i.date_z, i.date_v, i.date_d, i.text]
			print(arr)
			if j%2 == 0:
				host = Concl(arr, self.expansion)
			else:
				host = Concl(arr,self.expansion)
			host.move(-300, -300)
			form.addRow(host)
			j += 1
		
		db.close()
		
		gg = QWidget()
		gg.setLayout(form)
		
		hei = self.height()
		print(hei)
		
		scroll.setWidget(gg)
		
		lbl = QLabel()
		
		h = QVBoxLayout()
		h.addLayout(tit_h)
		h.addWidget(scroll_mini)
		h.addWidget(scroll)
		
		'''a1 = Concl('3')
		a2 = Concl('3')
		a3 = Concl('3')
		
		a11 = QHBoxLayout()
		a11.addWidget(a1)
		a22 = QHBoxLayout()
		a22.addWidget(a2)
		a33 = QHBoxLayout()
		a33.addWidget(a3)
		
		grid = QFormLayout()
		grid.setSpacing(0)
		grid.addRow(a11)
		grid.addRow(a22)
		grid.addRow(a33)
		
		
		bloc_v = QVBoxLayout()
		bloc_v.setSpacing(0)
		bloc_v.addWidget(a1)
		bloc_v.addWidget(a2)
		bloc_v.addWidget(a3)
		bloc_v.setSpacing(0)
		
		frame = QFrame()
		frame.setLayout(bloc_v)
		frame.setFixedHeight(450)
		
		x = QHBoxLayout()
		x.addWidget(frame)
		self.setContentsMargins(0,0,0,0)
		x = QWidget()
		x.setLayout(grid)
		
		self.scroll = QScrollArea()
		self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.scroll.setWidgetResizable(True)
		self.scroll.setWidget(x)
		
		h = QHBoxLayout()
		h.addWidget(self.scroll)
		'''
		self.setLayout(h)
		p = QPalette()
		gradient = QLinearGradient(0, 0, 120, 400)
		gradient.setColorAt(0.0, QColor(117,160,252))
		gradient.setColorAt(1.0, QColor(193,203,253))
		p.setBrush(QPalette.Window, QBrush(gradient))
		self.setPalette(p)
		
		if self.expansion == '1':
			self.showFullScreen()
			scroll.setMinimumHeight(hei+100)
		else:
			self.setGeometry(0, 30, 800, 600)
			scroll.setMinimumHeight(hei)
		self.setWindowTitle('Menubar')
		self.show()
	
	def addConcl(self):
		self.add = CreateConcl(self.number)
	def back(self):
		self.close()
	def exit(self):
		quit()
	def update_window(self):
		self.screen = UpdateScreen(self.expansion)
		self.main = Concls(self.expansion, self.number)
		self.close()
		self.screen.close()
		
class CreateConcl(QWidget):
	def __init__(self, number):
		super().__init__()
		self.number_h = number
		self.initUI()

	def initUI(self):

		addInstitutionButton = QPushButton('')
		addInstitutionButton.setIcon(QIcon('image/plus_2.png'))
		addInstitutionButton.setIconSize(QSize(55, 55))
		addInstitutionButton.clicked.connect(self.create_concl)
		
		self.number = QLineEdit()
		self.type = QLineEdit()
		self.name = QLineEdit()
		self.reason = QLineEdit()
		self.recommendation = QLineEdit()
		self.photo = QPushButton()
		self.photo.setFixedWidth(50)
		self.photo.setContentsMargins(0,0,0,0)
		self.photo.setIcon(QIcon('image/icon.png'))
		self.photo.setIconSize(QSize(43, 25))
		self.photo.clicked.connect(self.open_icon)
		self.conclusions = QLineEdit()
		self.date_z = QLineEdit()
		self.date_v = QLineEdit()
		self.date_d = QLineEdit()
		self.text = QLineEdit()
		
		form = QFormLayout()
		
		print("gggggg")
		form.addRow(QLabel('Узел №'), QLabel(self.number_h))
		print("gggggg")
		form.addRow(QLabel('Номер'), self.number)
		form.addRow(QLabel('Тип заключения'), self.type)
		form.addRow(QLabel('Название'), self.name)
		form.addRow(QLabel('Причина'), self.reason)
		form.addRow(QLabel('Рекомендации'), self.recommendation)
		form.addRow(QLabel('Фото'), self.photo)
		print("gggggg")
		form.addRow(QLabel('Выводы'), self.conclusions)
		form.addRow(QLabel('Дата зявки'), self.date_z)
		form.addRow(QLabel('Дата выдачи'), self.date_v)
		form.addRow(QLabel('Дата разрушения'), self.date_d)
		form.addRow(QLabel('Текст заключения'), self.text)
		
		print("gggggg")
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
	def create_concl(self):
		number = self.number.text()
		type = self.type.text()
		name = self.name.text()
		reason = self.reason.text()
		recommendation = self.recommendation.text()
		photo = 'f'
		conclusions = self.conclusions.text()
		date_z = self.date_z.text()
		date_v = self.date_v.text()
		date_d = self.date_d.text()
		text = self.text.text()
		db = SqliteDatabase('mydb.db')
		db.connect()
		concl = Conclusions2.create(owner=self.number_h, number=number, type=type, name=name, reason=reason,
									recommendation=recommendation, photo=photo, conclusions=conclusions,
									date_z=date_z, date_v=date_v, date_d=date_d, text=text)
		
		db.close()
		
		self.close()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Concls('0')
	sys.exit(app.exec_())
