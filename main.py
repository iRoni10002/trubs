#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *
from reg_form import Reg

class Main(QMainWindow):

    def __init__(self, expansion):
        super().__init__()
        self.expansion = expansion
        self.initUI()

    def initUI(self):
        exitAction = QAction('&Exit', self)
        #exitAction.setShortcut('Ctrl+Q')
        #exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        self.statusBar()
        menubar = self.menuBar()
        regMenu = menubar.addMenu('&Регистрация')
        viewMenu = menubar.addMenu('&Просмотр')
        redMenu = menubar.addMenu('&Исправления')
        svdMenu = menubar.addMenu('&Сводки')
        sprMenu = menubar.addMenu('&Справочники')
        srvMenu = menubar.addMenu('&Сервис')
        qMenu = menubar.addMenu('&Выход')
        qMenu.addAction(exitAction)
        regMenu.addAction('&REg', self.open_reg)
        #ggMenu.addAction("jjj")

        menubar.setStyleSheet("background-color: white;")

        self.w = self.calc_expansion_w(self.expansion)
        self.h = self.calc_expansion_h(self.expansion)

        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 400)
        gradient.setColorAt(0.0, QColor(240, 240, 240))
        gradient.setColorAt(1.0, QColor(240, 2, 27))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
