# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DesignAnalisadorIIhHOH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(360, 526)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 281, 71))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.buttonAbrir = QPushButton(self.centralwidget)
        self.buttonAbrir.setObjectName(u"buttonAbrir")
        self.buttonAbrir.setGeometry(QRect(20, 80, 101, 23))
        self.buttonSalvar = QPushButton(self.centralwidget)
        self.buttonSalvar.setObjectName(u"buttonSalvar")
        self.buttonSalvar.setGeometry(QRect(200, 80, 101, 23))
        self.textEntrada = QTextEdit(self.centralwidget)
        self.textEntrada.setObjectName(u"textEntrada")
        self.textEntrada.setGeometry(QRect(20, 130, 281, 121))
        self.buttonProcessar = QPushButton(self.centralwidget)
        self.buttonProcessar.setObjectName(u"buttonProcessar")
        self.buttonProcessar.setGeometry(QRect(120, 270, 101, 23))
        self.textSaida = QTextBrowser(self.centralwidget)
        self.textSaida.setObjectName(u"textSaida")
        self.textSaida.setGeometry(QRect(20, 300, 281, 192))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Analisador L\u00e9xico", None))
        self.buttonAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir Arquivo", None))
        self.buttonSalvar.setText(QCoreApplication.translate("MainWindow", u"Salvar Arquivo", None))
        self.buttonProcessar.setText(QCoreApplication.translate("MainWindow", u"Processar", None))
    # retranslateUi

