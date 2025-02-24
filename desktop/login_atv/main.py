import sys
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap
from layout import Ui_MainWindow
from form import Ui_furmulario
from comandos import comando

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.box=QMessageBox()
        self.ui.setupUi(self)
        self.comando = comando()
        self.ui.btn_login.clicked.connect(self.login)
        self.ui.btn_signup.clicked.connect(self.signup)
    def signup(self):
        form=Ui_furmulario()
        form.setupUi(self)
    def completar(self):
        print('oi')
    def login(self):
        password=self.ui.le_password.text()
        user=self.ui.le_user.text()
        if password=="adm" and user=="adm":
            print("oi")
            self.box.open()
        else:
            print("ha")
    
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() 
    sys.exit(app.exec())