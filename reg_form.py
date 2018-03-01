#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QMainWindow,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit, QComboBox, QRadioButton, QTextEdit
                             )
from PyQt5.QtGui import QColor

class Reg(QWidget):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.initUI()


    def initUI(self):

        #block_vertical
            #first_block_horisontal(h)
                #first_block_vertical_1(v)
                    #conclusion(h)
                    #condition(h)
                #first_block_vertical_2(v)
                    #oblect(h)
                    #metalloized(h)
                #first_block_vertical_3(v)
            #second_block_horisontal(h)
                #second_block_vertical_1(v)
                    #date_application(h)
                #second_block_vertical_2(v)
                    #date_issue(h)
                #second_block_vertical_3(v)
                    #date_destruction(h)
            #third_block_horisontal(h)
                #third_block_vertical(v)
                    #third_block_horisontal_1(h)
                        #unit(h)
                        #number(h)
                        #host(h)
                    #third_block_horisontal_2(h)
                        #adres(h)
                        #name(h)
            #fourth_block_horisontal(h)
                #fourth_block_vertical_1(v)
                    #fourth_block_horisontal_1(h)
                        #reason(v)
                        #advice(v)
                #fourth_block_vertical_2(v)
                    #fourth_block_horisontal_2(h)
                        #output(v)
                        #notice(v)

        conclusion = QLabel('Заключение')
        conclusionE = QLineEdit()
        conclusion_h = QHBoxLayout()
        conclusion_h.addWidget(conclusion)
        conclusion_h.addWidget(conclusionE)
        condition = QLabel('Состояние работы')
        conditionE = QComboBox()
        condition_h = QHBoxLayout()
        condition_h.addWidget(condition)
        condition_h.addWidget(conditionE)
        first_block_vertical_1 = QVBoxLayout()
        first_block_vertical_1.addLayout(conclusion_h)
        first_block_vertical_1.addLayout(condition_h)

        object = QLabel('Объект')
        objectE = QComboBox()
        object_h = QHBoxLayout()
        object_h.addWidget(object)
        object_h.addWidget(objectE)
        metalloized = QLabel('Металловед')
        metalloizedE = QComboBox()
        metalloized_h = QHBoxLayout()
        metalloized_h.addWidget(metalloized)
        metalloized_h.addWidget(metalloizedE)
        first_block_vertical_2 = QVBoxLayout()
        first_block_vertical_2.addLayout(object_h)
        first_block_vertical_2.addLayout(metalloized_h)

        researches = QRadioButton('Исследование')
        destruction = QRadioButton('Разрушение')
        calculate = QRadioButton('Расчет')
        first_block_vertical_3 = QVBoxLayout()
        first_block_vertical_3.addWidget(researches)
        first_block_vertical_3.addWidget(destruction)
        first_block_vertical_3.addWidget(calculate)

        first_block_horisontal = QHBoxLayout()
        first_block_horisontal.addLayout(first_block_vertical_1)
        first_block_horisontal.addLayout(first_block_vertical_2)
        first_block_horisontal.addLayout(first_block_vertical_3)
    #-----------------------------------------------------------
        date_application = QLabel('Дата заявки')
        date_issue = QLabel('Дата выдачи')
        date_destruction = QLabel('Дата разрушения')
        date_applicationE = QLineEdit()
        date_issueE = QLineEdit()
        date_destructionE = QLineEdit()
        date_application_h = QHBoxLayout()
        date_application_h.addWidget(date_application)
        date_application_h.addWidget(date_applicationE)
        date_issue_h = QHBoxLayout()
        date_issue_h.addWidget(date_issue)
        date_issue_h.addWidget(date_issueE)
        date_destruction_h = QHBoxLayout()
        date_destruction_h.addWidget(date_destruction)
        date_destruction_h.addWidget(date_destructionE)

        second_block_horisontal = QHBoxLayout()
        second_block_horisontal.addLayout(date_application_h)
        second_block_horisontal.addLayout(date_issue_h)
        second_block_horisontal.addLayout(date_destruction_h)
    #-----------------------------------------------------------
        unit = QLabel('Агрегат')
        unitE = QComboBox()
        unit_h = QHBoxLayout()
        unit_h.addWidget(unit)
        unit_h.addWidget(unitE)
        number = QLabel('№')
        numberE = QLineEdit()
        number_h = QHBoxLayout()
        number_h.addWidget(number)
        number_h.addWidget(numberE)
        host = QLabel('Узел')
        hostE = QComboBox()
        host_h = QHBoxLayout()
        host_h.addWidget(host)
        host_h.addWidget(hostE)
        third_block_horisontal_1 = QHBoxLayout()
        third_block_horisontal_1.addLayout(unit_h)
        third_block_horisontal_1.addLayout(number_h)
        third_block_horisontal_1.addLayout(host_h)

        adress = QLabel('Адресс')
        adressE = QLineEdit()
        adress_h = QHBoxLayout()
        adress_h.addWidget(adress)
        adress_h.addWidget(adressE)
        name = QLabel('Название')
        nameE = QLineEdit()
        name_h = QHBoxLayout()
        name_h.addWidget(name)
        name_h.addWidget(nameE)
        third_block_horisontal_2 = QHBoxLayout()
        third_block_horisontal_2.addLayout(adress_h)
        third_block_horisontal_2.addLayout(name_h)

        third_block_vertical = QVBoxLayout()
        third_block_vertical.addLayout(third_block_horisontal_1)
        third_block_vertical.addLayout(third_block_horisontal_2)
    #-----------------------------------------------------------
        reason = QLabel('Причина')
        reasonE = QTextEdit()
        reason_h = QVBoxLayout()
        reason_h.addWidget(reason)
        reason_h.addWidget(reasonE)
        advice = QLabel('Рекомендации')
        adviceE = QTextEdit()
        advice_h = QVBoxLayout()
        advice_h.addWidget(advice)
        advice_h.addWidget(adviceE)
        fourth_block_horisontal_1 = QHBoxLayout()
        fourth_block_horisontal_1.addLayout(reason_h)
        fourth_block_horisontal_1.addLayout(advice_h)

        output = QLabel('Выводы')
        outputE = QTextEdit()
        output_h = QVBoxLayout()
        output_h.addWidget(output)
        output_h.addWidget(outputE)
        notice = QLabel('Примечание')
        noticeE = QTextEdit()
        notice_h = QVBoxLayout()
        notice_h.addWidget(notice)
        notice_h.addWidget(noticeE)
        fourth_block_horisontal_2 = QHBoxLayout()
        fourth_block_horisontal_2.addLayout(output_h)
        fourth_block_horisontal_2.addLayout(notice_h)

        fourth_block_vertical = QVBoxLayout()
        fourth_block_vertical.addLayout(fourth_block_horisontal_1)
        fourth_block_vertical.addLayout(fourth_block_horisontal_2)
    #-----------------------------------------------------------

        block_verical = QVBoxLayout()
        block_verical.addLayout(first_block_horisontal)
        block_verical.addLayout(second_block_horisontal)
        block_verical.addLayout(third_block_vertical)
        block_verical.addLayout(fourth_block_vertical)

    #-------------------------Style----------------------------

        style = "QLabel { border: 1px solid transparent; border-bottom-color: red; color: white; " \
                "font-family: Verdana; font-size: 5%; " \
                "margin: 0px 10px 0px 10px; " \
                "border-radius: 20px 20px 20px 20px;" \
                "border-radius: 20px;}"

        self.setStyleSheet(style)



        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(192, 192, 192))
        self.setPalette(p)

        self.setLayout(block_verical)
        self.resize(self.width, self.height-60)
        self.move(-10, 60)
        self.setWindowTitle('Buttons')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ppl = Reg()
    sys.exit(app.exec_())
