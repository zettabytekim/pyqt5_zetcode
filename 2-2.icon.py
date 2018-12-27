# -*- coding: utf-8 -*-

"""
Project: ZetCode PyQt5 tutorial

Description:
    This example shows an icon in the titlebar of the window

Author: Zetta Kim
Website: zetcode.com
Last edited: 2018.12.25
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon # 추가

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('../images/web.png'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())