#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

    This example shows a QSlider widget.

Author: Zetta Kim
Website: zetcode.com
Last edited: 2019.01.08
"""

import sys
from PyQt5.QtWidgets import (QWidget, QSlider,
                             QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.lbl = QLabel(self)
        self.lbl.setPixmap(QPixmap('../images/mute.png'))
        self.lbl.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSilder')
        self.show()


    def changeValue(self, value):

        if value ==0:
            self.lbl.setPixmap(QPixmap('../images/mute.png'))
        elif value > 0 and value <= 30:
            self.lbl.setPixmap(QPixmap('../images/min.png'))
        elif value > 30 and value < 80:
            self.lbl.setPixmap(QPixmap('../images/med.png'))
        else:
            self.lbl.setPixmap(QPixmap('../images/max.png'))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())