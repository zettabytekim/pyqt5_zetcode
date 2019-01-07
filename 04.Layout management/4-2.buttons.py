# -*- coding: utf-8 -*-

"""
Project: ZetCode PyQt5 tutorial

Description:
    In this example, we position two push
    buttons in the bottom-right corner
    of the window.
Author: Zetta Kim
Website: zetcode.com
Last edited: 2018.12.27
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout,
                            QVBoxLayout, QApplication)


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())