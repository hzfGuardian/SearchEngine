# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import PyQt5
#from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = PyQt5.QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = PyQt5.QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(PyQt5.QtCore.QRect(80, 160, 431, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(PyQt5.QtCore.QRect(170, 240, 251, 71))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = PyQt5.QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(PyQt5.QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = PyQt5.QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        PyQt5.QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = PyQt5.QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Google"))
        self.pushButton.setText(_translate("MainWindow", "搜索"))

