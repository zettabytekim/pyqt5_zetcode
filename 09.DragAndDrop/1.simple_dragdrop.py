#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    ZetCode PyQt5 tutorial
    This is a simple drag and
    drop example. 
Author: Zetta Kim
Last edited: 2019.01.27
"""

from PyQt5.QtWidgets import (QPushButton, QWidget, QLineEdit, QApplication)
import sys


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)
        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300, 300, 300, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    app.exec_()
