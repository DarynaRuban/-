# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window1(object):
    def setupUi(self, Window1):
        Window1.setObjectName("Window1")
        Window1.resize(700, 450)
        self.label = QtWidgets.QLabel(Window1)
        self.label.setGeometry(QtCore.QRect(0, 0, 700, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.table_1 = QtWidgets.QLabel(Window1)
        self.table_1.setGeometry(QtCore.QRect(0, 50, 700, 400))
        self.table_1.setText("")
        self.table_1.setAlignment(QtCore.Qt.AlignCenter)
        self.table_1.setObjectName("table_1")
        self.buttonMenu_1 = QtWidgets.QPushButton(Window1)
        self.buttonMenu_1.setGeometry(QtCore.QRect(0, 0, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.buttonMenu_1.setFont(font)
        self.buttonMenu_1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(250, 250, 250);")
        self.buttonMenu_1.setObjectName("buttonMenu_1")

        self.retranslateUi(Window1)
        QtCore.QMetaObject.connectSlotsByName(Window1)

    def retranslateUi(self, Window1):
        _translate = QtCore.QCoreApplication.translate
        Window1.setWindowTitle(_translate("Window1", "Dialog"))
        self.label.setText(_translate("Window1", "Діяльніть магазинів"))
        self.buttonMenu_1.setText(_translate("Window1", "Меню"))