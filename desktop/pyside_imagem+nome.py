from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys

class NameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("america ya")
        self.setGeometry(100,100,400,400)

        central_widget=QWidget(self)
        layout=QVBoxLayout(central_widget)

        label=QLabel("Rafael", self)
        label.setStyleSheet("font-size: 20px; font-weight: bold; text-align: center")
        label.setAlignment(Qt.AlignCenter)

        button=QPushButton("america ya")
        button.setStyleSheet("font-size: 16px; padding: 50px;")
        button.clicked.connect(self.click)
        
        img_label=QLabel(self)
        pixmap=QPixmap("syndra.jpg")
        pixmap=pixmap.scaled(200,200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        img_label.setPixmap(pixmap)
        img_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
        layout.addWidget(img_label)
        layout.addWidget(button)

        self.setCentralWidget(central_widget)

    def click(self):
        print('hallo')

if __name__=="__main__":
    app=QApplication(sys.argv)
    window= NameWindow()
    window.show()
    sys.exit(app.exec())