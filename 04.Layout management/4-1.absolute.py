# -*- coding: utf-8 -*-

"""
Project: ZetCode PyQt5 tutorial

Description:
    This example shows three labels on a window
    using absolute positioning.


Author: Zetta Kim
Website: zetcode.com
Last edited: 2018.12.28
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorial', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('Absolute')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())