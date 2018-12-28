# -*- coding: utf-8 -*-

"""
Project: ZetCode PyQt5 tutorial

Description:
    This program creates a skeleton of
    a classic GUI application with a menubar,
    toolbar, statusbar, and a central widget.

Author: Zetta Kim
Website: zetcode.com
Last edited: 2018.12.27
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # textEdit
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        # action of menu
        exitAction = QAction(QIcon('images/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        # statusbar
        self.statusBar()

        # menubar
        menubar = self.menuBar( )
        menubar.setNativeMenuBar(False)  # macOS에서는 중요
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        # toolbar
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)


        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())