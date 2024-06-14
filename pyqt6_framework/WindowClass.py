from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Window")
        self.setWindowIcon(QIcon("QBpi.png"))
        # self.setFixedHeight(200)
        # self.setFixedWidth(200)
        self.setGeometry(500, 300, 400, 300)
        self.setStyleSheet('background-color:grey')

        stylesheet = (
            'background-color:black'
        )

        self.setStyleSheet(stylesheet)



app = QApplication([]) # Creating appliction object
window = Window() # Creating object of our window
window.show() # showing our window
sys.exit(app.exec())