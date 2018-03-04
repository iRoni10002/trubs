#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QMainWindow,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit, QComboBox, QRadioButton, QTextEdit,
                             QCheckBox, QListView)


#class xep(QWidget):

#    def __init__(self):
 #       super().__init__()
  #      self.initUI()

   # def initUI(self):
    #    self.setGeometry(300, 300, 250, 150)
     #   self.setWindowTitle('Event handler')
      #  self.show()

#    def keyPressEvent(self, e):
 #       if e.key() == Qt.Key_Escape:
  #          self.close()


class Request(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        #okButton = QPushButton("Submit")
        #okButton.clicked.connect(self.Submit)

        #mail = QLabel('E-mail:')
        #password = QLabel('Password:')
        #emailEdit = QLineEdit()
        #passwordEdit = QLineEdit()

    #--- Первый блок ---
        period_from = QLabel('За период с ')
        period_from_edit = QLineEdit()
        period_to = QLabel('по ')
        period_to_edit = QLineEdit()
        period_from_h = QHBoxLayout()
        period_from_h.addStretch(2)
        period_from_h.addWidget(period_from)
        period_from_h.addWidget(period_from_edit)
        period_to_h = QHBoxLayout()
        period_to_h.addStretch(1)
        period_to_h.addWidget(period_to)
        period_to_h.addWidget(period_to_edit)
        period_v = QVBoxLayout()
        period_v.addLayout(period_from_h)
        period_v.addLayout(period_to_h)
        #---------
        research = QRadioButton('исследование')

        style = "QRadioButton { margin-right: 20%; }"
        self.setStyleSheet(style)

        destruction = QRadioButton('разрушения')
        all_ = QRadioButton('все')
        r_btn_v = QVBoxLayout()
        r_btn_v.addWidget(research)
        r_btn_v.addWidget(destruction)
        r_btn_v.addWidget(all_)

        first_block_H = QHBoxLayout()
        first_block_H.addLayout(period_v)
        first_block_H.addLayout(r_btn_v)
    #--- Второй блок ---
        metallized = QCheckBox('металловед')
        metallized_edit = QComboBox()
        metallized_h = QHBoxLayout()
        metallized_h.addWidget(metallized)
        metallized_h.addWidget(metallized_edit)
        object = QCheckBox('объкт')
        object_edit = QComboBox()
        object_h = QHBoxLayout()
        object_h.addWidget(object)
        object_h.addWidget(object_edit)
        unit = QCheckBox('агрегат')
        unit_edit = QComboBox()
        unit_h = QHBoxLayout()
        unit_h.addWidget(unit)
        unit_h.addWidget(unit_edit)
        chose_unit = QCheckBox('выбрать агрегат с №')
        chose_unit_edit = QLineEdit()
        chose_unit_h = QHBoxLayout()
        chose_unit_h.addWidget(chose_unit)
        chose_unit_h.addWidget(chose_unit_edit)
        host_unit = QCheckBox('узел агрегата')
        host_unit_edit = QComboBox()
        host_unit_h = QHBoxLayout()
        host_unit_h.addWidget(host_unit)
        host_unit_h.addWidget(host_unit_edit)

        second_block_V = QVBoxLayout()
        second_block_V.addLayout(metallized_h)
        second_block_V.addLayout(object_h)
        second_block_V.addLayout(unit_h)
        second_block_V.addLayout(chose_unit_h)
        second_block_V.addLayout(host_unit_h)
    #--- Третий блок ---
        cansel_button = QPushButton('Отмена')
        cansel_button.clicked.connect(self.Submit)
        ok_button = QPushButton('ОК')
        ok_button.clicked.connect(self.Submit)
        btn_h = QHBoxLayout()
        btn_h.addStretch(1)
        btn_h.addWidget(cansel_button)
        btn_h.addWidget(ok_button)



        main_v = QVBoxLayout()
        main_v.addLayout(first_block_H)
        main_v.addLayout(second_block_V)
        main_v.addLayout(btn_h)


        self.setLayout(main_v)



        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Buttons')
        self.show()

    def Submit(self):
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ppl = Request()
    sys.exit(app.exec_())
