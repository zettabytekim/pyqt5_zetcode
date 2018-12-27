#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program creates a submenu.

Author: Zetta Kim
Website: zetcode.com
Last edited: 2018.12.26
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar = self.statusBar()
        self.statusBar.showMessage('Ready')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)  # macOS에서는 중요

        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction('View Statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View Statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', sel   f)
        impAct = QAction('Import mail', self)
        impAct.setStatusTip('Import mail')
        impMenu.addAction(impAct)

        expMenu = QMenu('Export', self)
        expAct = QAction('Export mail', self)
        expAct.setStatusTip('Export mail')
        expMenu.addAction(expAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addMenu(expMenu)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusBar.show()
        else:
            self.statusBar.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())