from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QPushButton
from random import randrange


class InitUI(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(800, 800)
        MainWindow.setWindowTitle('Круги')

        self.button = QPushButton(MainWindow)
        self.button.resize(40, 40)