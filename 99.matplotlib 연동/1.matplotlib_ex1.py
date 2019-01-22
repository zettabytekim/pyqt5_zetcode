#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    Widget 안에 mtplotlib 차트 보여주기

Author: Zetta Kim
Last edited: 2019.01.22
"""

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QApplication)
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        N = 5
        value = (20, 35, 30, 35, 27)
        ind = np.arange(N)
        width = 0.35

        fig = plt.Figure()
        ax = fig.add_subplot(111)
        ax.bar(ind, value, width)
        ax.set_xticks(ind + width/20)
        ax.set_xticklabels(['G1', 'G2', 'G3', 'G4', 'G5'])
        canvas = FigureCanvas(fig)
        canvas.draw()

        lay = QHBoxLayout()
        self.setLayout(lay)
        lay.addWidget(canvas)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('MatplotLib')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())
