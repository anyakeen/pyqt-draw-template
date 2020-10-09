# pyqt-draw-template

Draw the ellipse by pressing the button, drawing the figure in the selected region. This solution does not require drawing in the <code> graphicsView </code> element

Import important QWidgets and QGui for PyQt5

<code>
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import QRect, QPoint
</code>

onClick event

<code>
  def onClicked(self):
        print("Generated!")
        self.flag = True
        self.update()
  </code>
  
  Paint Event 
  
  <code>
  def paintEvent(self, e):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawRectangles(qp)
            qp.end()
  </code>
  
  Draw Rectangle/Ellipse function
  
  <code>
   def drawRectangles(self, qp):
        #draw rectangle in paint event
        col = QColor(0, 0, 0)
        col.setNamedColor('#ffd4d4')
        qp.setPen(col)
        qp.setBrush(QColor(200, 0, 0))
        qp.drawEllipse(100,100, 200,300)
  </code>
  
  Create QApplication
  
  <code>
  App = QApplication(sys.argv) 
window = Example() 
sys.exit(App.exec()) 
</code>

Example is our class, like: <code> class Example(QWidget): </code>

Out main and UI function:

<code>
 def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.flag = False
</code>
<code>
    def initUI(self):
        self.setFixedSize(1600, 900)
        self.setWindowTitle('Ct')
        self.btn = QPushButton("generate", self)
        #btn
        self.btn.move(1400, 15)
        self.btn.clicked.connect(self.onClicked)
        #createView
        self.show()
</code>
