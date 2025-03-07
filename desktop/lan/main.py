import sys
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap, QIcon
from form import Ui_furmulario
from layout import Ui_MainWindow as Ui_Login
from cardapio import Ui_MainWindow as Ui_Cardapio
from datetime import datetime
from banco import *


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
        login(self.user, self.password)
        
        if 

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
        nome=self.cadastro.LE_nome.text()
        cpf=self.cadastro.LE_cpf.text()
        sexo=int()
        if self.cadastro.R_masculino.isChecked():
            sexo=1
        elif self.cadastro.R_feminino.isChecked():
            sexo=2
        endereco=self.cadastro.LE_endereco.text()
        telefone=self.cadastro.LE_telefone.text()
        nascimento=self.cadastro.DE_nascimento.text() #data para texto
        data_python = datetime.strptime(nascimento, '%d/%m/%Y') #data para python
        data_sql = data_python.strftime('%Y-%m-%d') #data para sql
        user=self.cadastro.LE_user.text()
        senha=self.cadastro.LE_senha.text()

        adicionar_user(nome, cpf, sexo, endereco, telefone, data_sql, user, senha)
        self.cadastro.LE_cpf.clear()
        self.cadastro.LE_endereco.clear()
        self.cadastro.LE_nome.clear()
        self.cadastro.LE_senha.clear()
        self.cadastro.LE_user.clear()
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