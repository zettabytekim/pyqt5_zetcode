#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
ZetCode PyQt5 tutorial
    This example shows
    how to use QSplitter widget.

Author: Zetta Kim
Website: zetcode.com
Last edited: 2019.01.16
"""

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
                             QSplitter, QStyleFactory, QApplication)
from PyQt5.QtCore import Qt
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        hbox = QHBoxLayout(self)
        topLeft = QFrame(self)
        topLeft.setFrameShape(QFrame.StyledPanel)
        topRight = QFrame(self)
        topRight.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        spltter1 = QSplitter(Qt.Horizontal)
        spltter1.addWidget(topLeft)
        spltter1.addWidget(topRight)

        spltter2 = QSplitter(Qt.Vertical)
        spltter2.addWidget(spltter1)
        spltter2.addWidget(bottom)

        hbox.addWidget(spltter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("QSplitter")
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())

