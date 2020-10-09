# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 22:16:05 2020

@author: Jola
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import QRect, QPoint

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.flag = False

    def initUI(self):
        self.setFixedSize(1600, 900)
        self.setWindowTitle('Ct')
        self.btn = QPushButton("generate", self)
        #btn
        self.btn.move(1400, 15)
        self.btn.clicked.connect(self.onClicked)
        #createView
        
        self.show()

    def onClicked(self):
        print("Generated!")
        self.flag = True
        self.update()


    def paintEvent(self, e):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawRectangles(qp)
            qp.end()

    def drawRectangles(self, qp):
        #draw rectangle in paint event
        col = QColor(0, 0, 0)
        col.setNamedColor('#ffd4d4')
        qp.setPen(col)
        qp.setBrush(QColor(200, 0, 0))
        qp.drawEllipse(100,100, 200,300)
        
    def _shepp_logan ():
    #  Standard head phantom, taken from Shepp & Logan
        return [[   2,   .69,   .92,    0,      0,   0],
                [-.98, .6624, .8740,    0, -.0184,   0],
                [-.02, .1100, .3100,  .22,      0, -18],
                [-.02, .1600, .4100, -.22,      0,  18],
                [ .01, .2100, .2500,    0,    .35,   0],
                [ .01, .0460, .0460,    0,     .1,   0],
                [ .02, .0460, .0460,    0,    -.1,   0],
                [ .01, .0460, .0230, -.08,  -.605,   0],
                [ .01, .0230, .0230,    0,  -.606,   0],
                [ .01, .0230, .0460,  .06,  -.605,   0]]


App = QApplication(sys.argv) 
window = Example() 
sys.exit(App.exec()) 