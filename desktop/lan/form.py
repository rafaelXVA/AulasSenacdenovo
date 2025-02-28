# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_furmulario(object):
    def setupUi(self, furmulario):
        if not furmulario.objectName():
            furmulario.setObjectName(u"furmulario")
        furmulario.resize(400, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(furmulario.sizePolicy().hasHeightForWidth())
        furmulario.setSizePolicy(sizePolicy)
        furmulario.setMinimumSize(QSize(400, 600))
        furmulario.setMaximumSize(QSize(400, 600))
        furmulario.setAutoFillBackground(False)
        furmulario.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(furmulario)
        self.centralwidget.setObjectName(u"centralwidget")
        self.txt_formulario = QLabel(self.centralwidget)
        self.txt_formulario.setObjectName(u"txt_formulario")
        self.txt_formulario.setGeometry(QRect(140, 0, 124, 36))
        font = QFont()
        font.setPointSize(20)
        self.txt_formulario.setFont(font)
        self.txt_formulario.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.F_quest = QFrame(self.centralwidget)
        self.F_quest.setObjectName(u"F_quest")
        self.F_quest.setGeometry(QRect(10, 40, 381, 541))
        self.F_quest.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.F_quest.setFrameShape(QFrame.Shape.StyledPanel)
        self.F_quest.setFrameShadow(QFrame.Shadow.Raised)
        self.txt_nome = QLabel(self.F_quest)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(20, 10, 49, 16))
        self.LE_nome = QLineEdit(self.F_quest)
        self.LE_nome.setObjectName(u"LE_nome")
        self.LE_nome.setGeometry(QRect(20, 30, 201, 22))
        self.txt_cpf = QLabel(self.F_quest)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setGeometry(QRect(20, 70, 49, 16))
        self.LE_cpf = QLineEdit(self.F_quest)
        self.LE_cpf.setObjectName(u"LE_cpf")
        self.LE_cpf.setGeometry(QRect(20, 90, 113, 22))
        self.txt_sexo = QLabel(self.F_quest)
        self.txt_sexo.setObjectName(u"txt_sexo")
        self.txt_sexo.setGeometry(QRect(20, 130, 49, 16))
        self.R_masculino = QRadioButton(self.F_quest)
        self.R_masculino.setObjectName(u"R_masculino")
        self.R_masculino.setGeometry(QRect(20, 150, 89, 20))
        self.R_feminino = QRadioButton(self.F_quest)
        self.R_feminino.setObjectName(u"R_feminino")
        self.R_feminino.setGeometry(QRect(20, 170, 89, 20))
        self.LE_endereco = QLineEdit(self.F_quest)
        self.LE_endereco.setObjectName(u"LE_endereco")
        self.LE_endereco.setGeometry(QRect(20, 220, 113, 22))
        self.txt_endereco = QLabel(self.F_quest)
        self.txt_endereco.setObjectName(u"txt_endereco")
        self.txt_endereco.setGeometry(QRect(20, 200, 49, 16))
        self.txt_telefone = QLabel(self.F_quest)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setGeometry(QRect(20, 260, 49, 16))
        self.LE_telefone = QLineEdit(self.F_quest)
        self.LE_telefone.setObjectName(u"LE_telefone")
        self.LE_telefone.setGeometry(QRect(20, 280, 113, 22))
        self.txt_nascimento = QLabel(self.F_quest)
        self.txt_nascimento.setObjectName(u"txt_nascimento")
        self.txt_nascimento.setGeometry(QRect(20, 320, 111, 16))
        self.DE_nascimento = QDateEdit(self.F_quest)
        self.DE_nascimento.setObjectName(u"DE_nascimento")
        self.DE_nascimento.setGeometry(QRect(20, 340, 110, 22))
        self.btn_completar = QPushButton(self.F_quest)
        self.btn_completar.setObjectName(u"btn_completar")
        self.btn_completar.setGeometry(QRect(140, 470, 111, 24))
        self.btn_completar.setStyleSheet(u"color: rgb(107, 127, 255);\n"
"border-color: rgb(107, 127, 255);")
        self.btn_completar.setAutoDefault(False)
        self.btn_completar.setFlat(False)
        self.label = QLabel(self.F_quest)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 130, 49, 16))
        self.label_2 = QLabel(self.F_quest)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 70, 49, 16))
        self.LE_senha = QLineEdit(self.F_quest)
        self.LE_senha.setObjectName(u"LE_senha")
        self.LE_senha.setGeometry(QRect(240, 150, 113, 22))
        self.LE_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.LE_user = QLineEdit(self.F_quest)
        self.LE_user.setObjectName(u"LE_user")
        self.LE_user.setGeometry(QRect(240, 90, 113, 22))
        furmulario.setCentralWidget(self.centralwidget)

        self.retranslateUi(furmulario)

        self.btn_completar.setDefault(False)


        QMetaObject.connectSlotsByName(furmulario)
    # setupUi

    def retranslateUi(self, furmulario):
        furmulario.setWindowTitle(QCoreApplication.translate("furmulario", u"formulario", None))
        self.txt_formulario.setText(QCoreApplication.translate("furmulario", u"formul\u00e1rio", None))
        self.txt_nome.setText(QCoreApplication.translate("furmulario", u"Nome", None))
        self.txt_cpf.setText(QCoreApplication.translate("furmulario", u"CPF", None))
        self.LE_cpf.setInputMask(QCoreApplication.translate("furmulario", u"000.000.000-00", None))
        self.txt_sexo.setText(QCoreApplication.translate("furmulario", u"Sexo", None))
        self.R_masculino.setText(QCoreApplication.translate("furmulario", u"Masculino", None))
        self.R_feminino.setText(QCoreApplication.translate("furmulario", u"Feminino", None))
        self.txt_endereco.setText(QCoreApplication.translate("furmulario", u"Endere\u00e7o", None))
        self.txt_telefone.setText(QCoreApplication.translate("furmulario", u"Telefone", None))
        self.txt_nascimento.setText(QCoreApplication.translate("furmulario", u"Data de nascimento", None))
        self.btn_completar.setText(QCoreApplication.translate("furmulario", u"Completar", None))
        self.label.setText(QCoreApplication.translate("furmulario", u"Senha", None))
        self.label_2.setText(QCoreApplication.translate("furmulario", u"User", None))
    # retranslateUi

