 
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QMainWindow)


class Ex(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lcd = QLCDNumber(self)
        self.sld = QSlider(Qt.Horizontal, self)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.lcd)
        self.vbox.addWidget(self.sld)
        self.setLayout(self.vbox)
        self.sld.valueChanged.connect(self.lcd.display)


        self.show()
class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.ff = Ex()
        self.h = QVBoxLayout()
        self.h.addWidget(self.ff)
        self.setLayout(self.h)
        self.setCentralWidget(self.ff)
        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Signal & slot')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
