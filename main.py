import sys

from PyQt6 import uic

from PyQt6.QtWidgets import QApplication, QMainWindow

from PyQt6.QtGui import QPainter, QColor

from random import randint


class Exercise(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('C:/Users/chern/Desktop/Ui.ui')
        self.do_paint = False
        self.push.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exercise()
    ex.show()
    sys.exit(app.exec())