# -*- coding: utf-8 -*-

"""
Project: ZetCode PyQt5 tutorial

Description:
    In this example, we create a skeleton
    of a calculator using QGridLayout.

Author: Zetta Kim
Website: zetcode.com
Last edited: 2018.12.29
"""

import sys
from PyQt5.QtWidgets import QWidget, QGridLayout,\
    QPushButton, QApplication


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]
        # print(positions)
        for position, name in zip(positions, names):
            # print(position, name)
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())