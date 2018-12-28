# -*- coding: utf-8 -*-

"""
Project: ZetCode PyQt5 tutorial

Description:
    QMainWindow Template

Author: Zetta Kim
Website: zetcode.com
Last edited: 2018.12.27
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())