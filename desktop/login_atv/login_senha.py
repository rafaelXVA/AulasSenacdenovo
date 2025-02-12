from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys

class NameWindow(QMainWindow):
    def __init__(self) :
        super().__init__()

        self.setWindowTitle("login")
        self.setGeometry(500,500,200,50)

        central_widget=QWidget(self)
        layout=QVBoxLayout(central_widget)

        labelUser=QLabel("User", self)
        labelUser.setStyleSheet("font-size: 12px; font-weight: regular; text-align: Left")
        labelUser.setAlignment(Qt.AlignLeft)

        self.user_input=QLineEdit(self)
        self.user_input.setFixedSize(250,20)
        self.user_input.setAlignment(Qt.AlignLeft)

        labelSenha=QLabel("Password", self)
        labelSenha.setStyleSheet("font-size: 12px; font-weight: regular; text-align: Left")
        labelSenha.setAlignment(Qt.AlignLeft)

        self.senha_input=QLineEdit(self)
        self.senha_input.setEchoMode(QLineEdit.Password)
        self.senha_input.setFixedSize(250,20)
        self.senha_input.setAlignment(Qt.AlignLeft)

        button=QPushButton("Login")
        button.setStyleSheet("font-size: 10px; padding: 10px;")
        button.setFixedSize(100,35)
        button.clicked.connect(self.user)

        layout.addWidget(labelUser)
        layout.addWidget(self.user_input)
        layout.addWidget(labelSenha)
        layout.addWidget(self.senha_input)
        layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(central_widget)
    def user(self):
        userConf=self.senha_input.text()
        senhaConf=self.user_input.text()
        
        while True:
            if userConf=="admin" and senhaConf=="admin":
                box=QMessageBox()
                box.setText("Login Completed")
                box.setWindowTitle("Login")
                box.exec()
                self.NameWindow2()
                break
            else:
                box=QMessageBox()
                box.setText("Login Failed")
                box.setWindowTitle("Login")
                box.exec()
                return print("bad")
    
    class NameWindow2(QMainWindow):
        def __init__(self) :
            super().__init__()

            self.setWindowTitle("Register")
            self.setGeometry(500,500,200,50)

            central_widget=QWidget(self)
            layout=QVBoxLayout(central_widget)

            labelCPF=QLabel("CPF", self)
            labelCPF.setStyleSheet("font-size: 12px; font-weight: regular; text-align: Left")
            labelCPF.setAlignment(Qt.AlignLeft)

            self.CPF_input=QLineEdit(self)
            self.CPF_input.setFixedSize(250,20)
            self.CPF_input.setAlignment(Qt.AlignLeft)

            labelName=QLabel("Name", self)
            labelName.setStyleSheet("font-size: 12px; font-weight: regular; text-align: Left")
            labelName.setAlignment(Qt.AlignLeft)

            self.Name_input=QLineEdit(self)
            self.Name_input.setFixedSize(250,20)
            self.Name_input.setAlignment(Qt.AlignLeft)

            button=QPushButton("Register")
            button.setStyleSheet("font-size: 10px; padding: 10px;")
            button.setFixedSize(100,35)
            button.clicked.connect(self.user)

            layout.addWidget(labelCPF)
            layout.addWidget(self.CPF_input)
            layout.addWidget(labelName)
            layout.addWidget(self.Name_input)
            layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.setAlignment(Qt.AlignCenter)

            self.setCentralWidget(central_widget)
        def OpenRegister(self):
            self.registerWindow=NameWindow()
            self.registerWindow.show()
            self.close()
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=NameWindow()
    window.show()
    sys.exit(app.exec())