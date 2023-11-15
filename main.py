import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication
from random import randrange
from ui import InitUI


class Round(InitUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_round(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()
    def draw_round(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        r = randrange(10, 800)
        qp.drawEllipse(0, 50, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Round()
    ex.show()
    sys.exit(app.exec())