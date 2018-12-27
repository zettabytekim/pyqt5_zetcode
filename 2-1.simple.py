# -*- coding: utf-8 -*-

"""
Project: ZetCode PyQt5 tutorial

Description:
    In this example, we create a simple
    window in PyQt5.

Author: Zetta Kim
Website: zetcode.com
Last edited: 2018.12.25
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple Window')
    w.show()

    sys.exit(app.exec_())
