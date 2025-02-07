from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QPixmap, QImage, QPainter, QColor
from PySide6.QtCore import Qt
import sys

class NameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("America ya")
        self.setGeometry(600,600,100,100)

        central_widget=QWidget(self)
        layout=QVBoxLayout(central_widget)

        self.img_gragas_scuba=QLabel(self)
        self.pixmap_scuba=QPixmap("gragas_scuba.jpg")
        self.pixmap_scuba=self.pixmap_scuba.scaled(0,0, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.img_gragas_scuba.setPixmap(self.pixmap_scuba)
        self.img_gragas_scuba.setAlignment(Qt.AlignCenter)

        self.img_gragas_kda=QLabel(self)
        self.pixmap_kda=QPixmap("gragas_kda.jpg")
        self.pixmap_kda=self.pixmap_kda.scaled(0,0, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.img_gragas_kda.setPixmap(self.pixmap_kda)
        self.img_gragas_kda.setAlignment(Qt.AlignCenter)

        button_foda=QPushButton("Gragas Foda")
        button_foda.setStyleSheet("font-size: 16px; padding: 20px;")
        button_foda.clicked.connect(self.click1)

        button_fodinha=QPushButton("Gragas Fodinha")
        button_fodinha.setStyleSheet("font-size: 16px; padding: 20px;")
        button_foda.clicked.connect(self.click2)


        layout.addWidget(self.img_gragas_kda)
        layout.addWidget(self.img_gragas_scuba)
        layout.addWidget(button_foda)
        layout.addWidget(button_fodinha)

        self.setCentralWidget(central_widget)
    
    def click1(self):
        x=self.img_gragas_kda.width(500)
        y=self.img_gragas_kda.height(500)
        new=self.pixmap_kda=self.pixmap_kda.scaled(x,y, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.img_gragas_kda.setPixmap(new)
    def click2(self):
        pixmap_scuba=pixmap_scuba.scaled(500,500, Qt.KeepAspectRatio, Qt.SmoothTransformation)


if __name__=="__main__":
    app=QApplication(sys.argv)
    window=NameWindow()
    window.show()
    sys.exit(app.exec())