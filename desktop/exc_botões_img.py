from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys

class NameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("America ya")
        self.setGeometry(600,600,100,100)

        central_widget=QWidget(self)
        layout=QVBoxLayout(central_widget)

        img_gragas_scuba=QLabel(self)
        pixmap_scuba=QPixmap("gragas_scuba.jpg")
        pixmap_scuba=pixmap_scuba.scaled(500,500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        img_gragas_scuba.setPixmap(pixmap_scuba)
        img_gragas_scuba.setAlignment(Qt.AlignCenter)

        img_gragas_kda=QLabel(self)
        pixmap_kda=QPixmap("gragas_kda.jpg")
        pixmap_kda=pixmap_kda.scaled(500,500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        img_gragas_kda.setPixmap(pixmap_kda)
        img_gragas_kda.setAlignment(Qt.AlignCenter)

        button_foda=QPushButton("Gragas Foda")
        button_foda.setStyleSheet("font-size: 16px; padding: 20px;")

        button_fodinha=QPushButton("Gragas Fodinha")
        button_fodinha.setStyleSheet("font-size: 16px; padding: 20px;")

        layout.addWidget(img_gragas_kda)
        layout.addWidget(img_gragas_scuba)
        layout.addWidget(button_foda)
        layout.addWidget(button_fodinha)

        self.setCentralWidget(central_widget)
    
    def click1(self):
        
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    window= NameWindow()
    window.show()
    sys.exit(app.exec())