from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtCore import Qt
import sys

class NameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("America ya")
        self.setGeometry(100,100,400,200)

        label=QLabel("Rafael\namerica ya", self)
        label.setStyleSheet("font-size: 18px; font-weight: bold; text-align: center")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)
if __name__=="__main__":
    app=QApplication(sys.argv)
    window= NameWindow()
    window.show()
    sys.exit(app.exit())