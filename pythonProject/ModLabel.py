# from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class ModLabel(QWidget):

    def __int__(self, parent):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        self.check_box = QCheckBox()
        layout.addWidget(self.check_box, Qt.AlignCenter)

        self.name = QLabel(self)
        self.name.setText("test")
        layout.addWidget(self.name, Qt.AlignCenter)

        self.setLayout(layout)

    def set_dimensions(self, width, height):
        self.setGeometry(0, 0, width, height)
