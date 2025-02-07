from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit
from PySide6.QtGui import QPixmap, QImage, QPainter, QColor
from PySide6.QtCore import Qt
import sys

class NameWindow(QMainWindow):
    def __init__(self):
        super().__init__() 

        self.setWindowTitle("mein got")
        self.setGeometry(600,600,100,100)

        central_widget=QWidget(self)

        self.americaya=QLabel("anything you want: ")
        self.americaya=QLineEdit()

        self.button=QPushButton("backward")
        self.button.clicked.connect(self)

        self.result=QLabel("")
        
        layout=QVBoxLayout()
        layout.addWidget(self.americaya)
        layout.addWidget(self.button)
        layout.addWidget(self.result)

        central_widget=QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=NameWindow()
    window.show()
    sys.exit(app.exec())