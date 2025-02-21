import sys
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap
from cadastro import Ui_MainWindow as Ui_Cadastro
from login import Ui_MainWindow as Ui_Login
from cardapio import Ui_MainWindow as Ui_Cardapio

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login=Ui_Login()
        self.login.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())