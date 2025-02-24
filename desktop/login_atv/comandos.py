from desktop.lan.layout import Ui_MainWindow
from desktop.lan.form import Ui_furmulario
import sys

class comando():
    ui=Ui_furmulario()
    def login(self):
        password=self.ui.le_password.text()
        user=self.ui.le_user.text()
        if password=="adm" and user=="adm":
            print("oi")
        else:
            print("ha")