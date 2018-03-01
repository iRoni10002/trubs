#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QMainWindow,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit, QComboBox, QRadioButton, QTextEdit
                             )
from PyQt5.QtGui import QColor

class Reg(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

    #--- Первый блок ---

        f_b_h = QHBoxLayout()

        f_f_b_v = QVBoxLayout()
         #--- Заключение ---
        zakl = QLabel('Заключение №')
        zaklEdit = QLineEdit()
        zakl_h = QHBoxLayout()
        zakl_h.addWidget(zakl)
        zakl_h.addWidget(zaklEdit)
        f_f_b_v.addLayout(zakl_h)

         #--- Состояние работы ---
        cow = QLabel('Состояние работы')
        cowEdit = QComboBox(self)
        cowEdit.addItem("Все плохло")
        cowEdit.addItem("Все очень плохло")
        cow_h = QHBoxLayout()
        cow_h.addWidget(cow)
        cow_h.addWidget(cowEdit)
        f_f_b_v.addLayout(cow_h)

        s_f_b_v = QVBoxLayout()
         #--- Объект ---
        object = QLabel('Объект')
        objectEdit = QComboBox(self)
        objectEdit.addItem("Все плохло")
        objectEdit.addItem("Все очень плохло")
        object_h = QHBoxLayout()
        object_h.addWidget(object)
        object_h.addWidget(objectEdit)
        s_f_b_v.addLayout(object_h)

         #--- Металловед ---
        meved = QLabel('Металловед')
        mevedEdit = QComboBox(self)
        mevedEdit.addItem("Все плохло")
        mevedEdit.addItem("Все очень плохло")
        meved_h = QHBoxLayout()
        meved_h.addWidget(meved)
        meved_h.addWidget(mevedEdit)
        s_f_b_v.addLayout(meved_h)

        t_f_b_v = QVBoxLayout()
         #--- Исследование ---
        issl = QRadioButton('Исследование')
        t_f_b_v.addWidget(issl)

         #--- Разрушение ---
        destr = QRadioButton('Разрушение')
        t_f_b_v.addWidget(destr)

         #--- Расчет ---
        math = QRadioButton('Расчет')
        t_f_b_v.addWidget(math)

        f_b_h.addLayout(f_f_b_v)
        f_b_h.addLayout(s_f_b_v)
        f_b_h.addLayout(t_f_b_v)

    #--- Второй блок ---

        s_b_h = QHBoxLayout()

        f_s_b_h = QHBoxLayout()
         #--- Дата заявки ---
        dateZ = QLabel('Дата заявки')
        dateZEdit = QLineEdit()
        f_s_b_h.addWidget(dateZ)
        f_s_b_h.addWidget(dateZEdit)

        s_s_b_h = QHBoxLayout()
         #--- Дата выдачи ---
        dateG = QLabel('Дата выдачи')
        dateGEdit = QLineEdit()
        s_s_b_h.addWidget(dateG)
        s_s_b_h.addWidget(dateGEdit)

        t_s_b_h = QHBoxLayout()
         #--- Дата разрушения ---
        dateD = QLabel('Дата разрушения')
        dateDEdit = QLineEdit()
        t_s_b_h.addWidget(dateD)
        t_s_b_h.addWidget(dateDEdit)

        s_b_h.addLayout(f_s_b_h)
        s_b_h.addLayout(s_s_b_h)
        s_b_h.addLayout(t_s_b_h)

    #--- Третий блок ---

        t_b_v = QVBoxLayout

        f_t_b_h = QHBoxLayout()
         #--- Агрегат ---
        agr = QLabel('Агрегат')
        agrEdit = QComboBox(self)
        agrEdit.addItem("Все плохло")
        agrEdit.addItem("Все очень плохло")
        arg_h = QHBoxLayout()
        arg_h.addWidget(agr)
        arg_h.addWidget(agrEdit)

         #--- № ---
        nmbr = QLabel('№')
        nmbrEdit = QLineEdit()
        nmbr_h = QHBoxLayout()
        nmbr_h.addWidget(nmbr)
        nmbr_h.addWidget(nmbrEdit)

         #--- Узел ---
        uzl = QLabel('Узел')
        uzlEdit = QLineEdit()
        uzl_h = QHBoxLayout()
        uzl_h.addWidget(uzl)
        uzl_h.addWidget(uzlEdit)

        t_f_b_v.addLayout(arg_h)
        t_f_b_v.addLayout(nmbr_h)
        t_f_b_v.addLayout(uzl_h)

        s_t_b_h = QHBoxLayout()
         #--- Что-то ---
        smth = QLabel('Что-то')
        smthEdit = QLineEdit()
        smth_h = QHBoxLayout()
        smth_h.addWidget(smth)
        smth_h.addWidget(smthEdit)

         #--- Название ---
        name = QLabel('Название')
        nameEdit = QComboBox(self)
        nameEdit.addItem("Все плохло")
        nameEdit.addItem("Все очень плохло")
        name_h = QHBoxLayout()
        name_h.addWidget(name)
        name_h.addWidget(nameEdit)

        t_b_v.addLayout(f_t_b_h)
        t_b_v.addLayout(s_t_b_h)

    #---#  Четвертый блок ---

        fo_b_h = QHBoxLayout()

        f_fo_b_v = QVBoxLayout()
         #--- Причина ----
        rsn = QLabel('Причина')
        rsnEdit = QTextEdit()
        rsn_v = QVBoxLayout()
        rsn_v.addWidget(rsn)
        rsn_v.addWidget(rsnEdit)

         #--- Рекомендации ----
        dvs = QLabel('Рекомендации')
        dvsEdit = QTextEdit()
        dvs_v = QVBoxLayout()
        dvs_v.addWidget(dvs)
        dvs_v.addWidget(dvsEdit)

        f_fo_b_v.addLayout(rsn_v)
        f_fo_b_v.addLayout(dvs_v)

        s_fo_b_v = QVBoxLayout()
         #--- Выводы ----
        cncl = QLabel('Выводы')
        cnclEdit = QTextEdit()
        cncl_v = QVBoxLayout()
        cncl_v.addWidget(cncl)
        cncl_v.addWidget(cnclEdit)

         #--- Примечание ----
        pls = QLabel('Примечание')
        plsEdit = QTextEdit()
        pls_v = QVBoxLayout()
        pls_v.addWidget(pls)
        pls_v.addWidget(plsEdit)

        s_fo_b_v.addLayout(cncl_v)
        s_fo_b_v.addLayout(pls_v)

        fo_b_h.addLayout(f_fo_b_v)
        fo_b_h.addLayout(s_fo_b_v)


        v_block = QHBoxLayout()
        v_block.addLayout(f_b_h)
        v_block.addLayout(s_b_h)
        v_block.addLayout(t_b_v)
        v_block.addLayout(fo_b_h)

        #okButton.setStyleSheet("background-color: #334761; color: white;"
         #                      "font-family: Verdana; font-size: 16px;"
          #                     "margin: 0px 10px 0px 10px")

        self.setLayout(v_block)
        v_block.setStretch(1)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(192, 192, 192))
        self.setPalette(p)

        self.setGeometry(300, 300, 800, 750)
        self.setWindowTitle('Register form')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ppl = Reg()
    sys.exit(app.exec_())
