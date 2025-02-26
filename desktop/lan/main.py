import sys
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap, QIcon
from form import Ui_furmulario
from layout import Ui_MainWindow as Ui_Login
from cardapio import Ui_MainWindow as Ui_Cardapio

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.box=QMessageBox()
        self.login=Ui_Login()
        self.cadastro=Ui_furmulario()
        self.cardapio=Ui_Cardapio()
        self.cadastro.setupUi(self)
        self.login.setupUi(self)


        self.setFixedSize(600,600)
        self.setWindowIcon(QIcon("lanche.png"))
        self.setWindowTitle("Lanchonete Maneira")
        self.login.btn_login.clicked.connect(self.btn_login)
        self.login.btn_signup.clicked.connect(self.btn_signup)

    def btn_login(self):
        self.password=self.login.le_password.text()
        self.user=self.login.le_user.text()
        if self.password=='adm' and self.user=='adm':
            window.close()
            window_cardapio.show()
            self.box.setWindowTitle('login')
            self.box.setText('Login concluído com sucesso')
            self.box.open()
        else:
            self.box.setWindowTitle('login')
            self.box.setText('Falha no login')
            self.box.open()
    def btn_signup(self):
        window.close()
        window_cadastro.show()

class Cadastro(QMainWindow):

    def __init__(self):
        super().__init__()
        self.cadastro=Ui_furmulario()
        self.cadastro.setupUi(self)
        self.cadastro.btn_completar.clicked.connect(self.completar)
    def completar(self):
        window_cadastro.close()
        window.show()
class Cardapio(QMainWindow):

    def __init__(self):
        super().__init__()
        self.cardapio=Ui_Cardapio()
        self.cardapio.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window=MainWindow()
    window_cadastro=Cadastro()
    window_cardapio=Cardapio()
    window.show()
    sys.exit(app.exec())