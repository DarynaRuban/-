# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu(object):
    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(600, 450)
        menu.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(menu)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 70))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_1 = QtWidgets.QPushButton(menu)
        self.pushButton_1.setGeometry(QtCore.QRect(200, 140, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(menu)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 190, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(menu)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 240, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(menu)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 290, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(menu)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 340, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)

    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "Dialog"))
        self.label.setText(_translate("menu", "?????????????????????? \"??????????????????\""))
        self.pushButton_1.setText(_translate("menu", "???????????????????? ??????????????????"))
        self.pushButton_2.setText(_translate("menu", "???????????????? ??????????????????"))
        self.pushButton_3.setText(_translate("menu", "?????????????? ????????????????????"))
        self.pushButton_4.setText(_translate("menu", "???????????????? ????????????"))
        self.pushButton_5.setText(_translate("menu", "??????????"))
