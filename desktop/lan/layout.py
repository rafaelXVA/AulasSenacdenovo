# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import foto_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(625, 602)
        MainWindow.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(210, 180, 201, 221))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(60, 120, 75, 24))
        self.btn_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_login.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.txt_user = QLabel(self.frame)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setGeometry(QRect(40, 20, 49, 16))
        self.le_user = QLineEdit(self.frame)
        self.le_user.setObjectName(u"le_user")
        self.le_user.setGeometry(QRect(40, 40, 113, 22))
        self.txt_password = QLabel(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(40, 70, 49, 16))
        self.le_password = QLineEdit(self.frame)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setGeometry(QRect(40, 90, 113, 22))
        self.le_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.btn_signup = QPushButton(self.frame)
        self.btn_signup.setObjectName(u"btn_signup")
        self.btn_signup.setGeometry(QRect(60, 150, 75, 24))
        self.btn_signup.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 801, 601))
        self.label.setStyleSheet(u"background-image: url(:/foto/lan4.jpg);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.frame.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"login", None))
        self.txt_user.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.txt_password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btn_signup.setText(QCoreApplication.translate("MainWindow", u"sign up", None))
        self.label.setText("")
    # retranslateUi

