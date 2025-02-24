import sys
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap
from form import Ui_furmulario as Ui_Cadastro
from layout import Ui_MainWindow as Ui_Login
from cardapio import Ui_MainWindow as Ui_Cardapio

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.box=QMessageBox()
        self.login=Ui_Login()
        self.cadastro=Ui_Cadastro()
        self.login.setupUi(self)

        self.login.btn_login.clicked.connect(self.btn_login)
        self.login.btn_signup.clicked.connect(self.btn_signup)

    def btn_login(self):
        self.password=self.login.le_password.text()
        self.user=self.login.le_user.text()
        if self.password=='adm' and self.user=='adm':
            self.box.setWindowTitle('login')
            self.box.setText('Login concluído com sucesso')
            self.box.open()
        else:
            self.box.setWindowTitle('login')
            self.box.setText('Falha no login')
            self.box.open()
    def btn_signup(self):
        self.cadastro.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())