# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

import foto_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 767)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 1331, 721))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.LOgin = QPushButton(self.frame)
        self.LOgin.setObjectName(u"LOgin")
        self.LOgin.setGeometry(QRect(420, 520, 131, 41))
        self.LOgin.setStyleSheet(u"background-color: rgb(255, 247, 15);\n"
"background-color: rgb(187, 214, 68);")
        self.senha = QFrame(self.frame)
        self.senha.setObjectName(u"senha")
        self.senha.setGeometry(QRect(360, 400, 261, 51))
        self.senha.setFrameShape(QFrame.Shape.StyledPanel)
        self.senha.setFrameShadow(QFrame.Shadow.Raised)
        self.senha_login = QLabel(self.senha)
        self.senha_login.setObjectName(u"senha_login")
        self.senha_login.setGeometry(QRect(10, 20, 49, 16))
        self.senha_login.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.senha_dados = QLineEdit(self.senha)
        self.senha_dados.setObjectName(u"senha_dados")
        self.senha_dados.setGeometry(QRect(70, 20, 171, 22))
        self.senha_dados.setFrame(True)
        self.senha_dados.setEchoMode(QLineEdit.EchoMode.Password)
        self.usuario = QFrame(self.frame)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setGeometry(QRect(360, 340, 261, 51))
        self.usuario.setFrameShape(QFrame.Shape.StyledPanel)
        self.usuario.setFrameShadow(QFrame.Shadow.Raised)
        self.usuario_login = QLabel(self.usuario)
        self.usuario_login.setObjectName(u"usuario_login")
        self.usuario_login.setGeometry(QRect(10, 20, 49, 16))
        self.usuario_login.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.usuario_dados = QLineEdit(self.usuario)
        self.usuario_dados.setObjectName(u"usuario_dados")
        self.usuario_dados.setGeometry(QRect(70, 20, 171, 22))
        self.Image_Login = QLabel(self.frame)
        self.Image_Login.setObjectName(u"Image_Login")
        self.Image_Login.setGeometry(QRect(-40, 0, 961, 711))
        self.Image_Login.setPixmap(QPixmap(u"lan4.jpg"))
        self.Image_Login.setScaledContents(True)
        self.Image_Login.raise_()
        self.LOgin.raise_()
        self.senha.raise_()
        self.usuario.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.usuario_dados, self.senha_dados)
        QWidget.setTabOrder(self.senha_dados, self.LOgin)

        #self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(qtTrId(u""))
        self.LOgin.setText(qtTrId(u""))
        self.senha_login.setText(qtTrId(u""))
        self.senha_dados.setText("")
        self.usuario_login.setText(qtTrId(u""))
        self.Image_Login.setText("")
    # retranslateUi

