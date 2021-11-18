import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.qp = QPainter()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.push)
        self.flag = False

    def push(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        color = QColor(random.choice(range(256)),
                       random.choice(range(256)),
                       random.choice(range(256)))
        size = random.choice(range(10, 300))

        self.qp.setBrush(color)
        self.qp.drawEllipse(400 - size // 2, 250 - size // 2, size, size)


if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
