import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QWidget
)

from color_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Layout Demo")

        layout = QGridLayout()
        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("green"), 1, 1)
        layout.addWidget(Color("blue"), 2, 2)
        layout.addWidget(Color("yellow"), 3, 3)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()