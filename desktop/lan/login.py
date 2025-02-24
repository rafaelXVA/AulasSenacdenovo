# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import um_qrc
import foto_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(617, 610)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.senha = QFrame(self.centralwidget)
        self.senha.setObjectName(u"senha")
        self.senha.setStyleSheet(u"")
        self.senha.setFrameShape(QFrame.Shape.StyledPanel)
        self.senha.setFrameShadow(QFrame.Shadow.Raised)
        self.frame = QFrame(self.senha)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-20, -20, 621, 631))
        self.frame.setStyleSheet(u"image: url(:/foto/lan4.jpg);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.senha_login = QLabel(self.frame)
        self.senha_login.setObjectName(u"senha_login")
        self.senha_login.setGeometry(QRect(240, 210, 35, 16))
        self.senha_login.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.senha_dados = QLineEdit(self.frame)
        self.senha_dados.setObjectName(u"senha_dados")
        self.senha_dados.setGeometry(QRect(240, 230, 151, 22))
        self.senha_dados.setFrame(True)
        self.senha_dados.setEchoMode(QLineEdit.EchoMode.Password)
        self.usuario_login = QLabel(self.frame)
        self.usuario_login.setObjectName(u"usuario_login")
        self.usuario_login.setGeometry(QRect(240, 260, 43, 16))
        self.usuario_login.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.usuario_dados = QLineEdit(self.frame)
        self.usuario_dados.setObjectName(u"usuario_dados")
        self.usuario_dados.setGeometry(QRect(240, 280, 151, 22))
        self.LOgin = QPushButton(self.frame)
        self.LOgin.setObjectName(u"LOgin")
        self.LOgin.setGeometry(QRect(260, 320, 91, 24))
        self.LOgin.setStyleSheet(u"background-color: rgb(255, 247, 15);\n"
"background-color: rgb(187, 214, 68);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.senha)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.usuario_dados, self.senha_dados)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    '''def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(qtTrId(u""))
        self.senha_login.setText(qtTrId(u""))
        self.senha_dados.setText("")
        self.usuario_login.setText(qtTrId(u""))
        self.LOgin.setText(qtTrId(u""))
    # retranslateUi'''

