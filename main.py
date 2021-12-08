import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog
from menu import Ui_menu
from window1 import Ui_Window1
from window2 import Ui_Window2
from window3 import Ui_Window3

excel1 = "\Users\STEELTECH\Desktop\проєкт\Excel1.xls"
excel2 = "\Users\STEELTECH\Desktop\проєкт\Excel2.xls"
excel3 = "\Users\STEELTECH\Desktop\проєкт\Excel3.xls"
excel4 = "\Users\STEELTECH\Desktop\проєкт\Excel4.xls"

excel12 = pd.read_excel(excel1)
excel13 = pd.DataFrame(excel12, index=[1,2,3,4,5,6,7,8,9,10,11])
excel14 = str(excel13)

excel22 = pd.read_excel(excel2)
excel23 = pd.DataFrame(excel22, index=[1,2,3])
excel24 = str(excel23)



app = QtWidgets.QApplication(sys.argv)
menu = QtWidgets.QDialog()
ui = Ui_menu()
ui.setupUi(menu)
menu.show()

def openExcel1():
    global Window1
    Window1 = QtWidgets.QDialog()
    ui = Ui_Window1()
    ui.setupUi(Window1)
    menu.close()
    Window1.show()

    ui.table_1.setText(excel14)

    def returnToMain1():
        Window1.close()
        menu.show()
   
    ui.buttonMenu_1.clicked.connect(returnToMain1)

def openExcel2():
    global Window2
    Window2 = QtWidgets.QDialog()
    ui = Ui_Window2()
    ui.setupUi(Window2)
    menu.close()
    Window2.show()

    ui.table_2.setText(excel24)

    def returnToMain2():
        Window2.close()
        menu.show()

    ui.buttonMenu_2.clicked.connect(returnToMain2)

def drawGraph1():
    dataExcelFile3 = pd.read_excel(excel3)

    y1 = dataExcelFile3.iloc[0]
    y2 = dataExcelFile3.iloc[1]
    y3 = dataExcelFile3.iloc[2]
    y4 = dataExcelFile3.iloc[3]
    y5 = dataExcelFile3.iloc[4]
    y6 = dataExcelFile3.iloc[5]

    plt.plot(y1, label = u'Плановий товарообмін 1 магазин')
    plt.plot(y2, label = u'Плановий товарообмін 6 магазин')
    plt.plot(y3, label = u'Плановий товарообмін 7 магазин')
    plt.plot(y4, label = u'Фактичний товарообмін 1 магазин')
    plt.plot(y5, label = u'Фактичний товарообмін 6 магазин')
    plt.plot(y6, label = u'Фактичний товарообмін 7 магазин')

    plt.title("Товарообмін")
    plt.ylabel("Товарообмін")
    plt.xlabel("Квартали")
    plt.legend()
    plt.show()

def drawGraph2():
    dataExcelFile3 = pd.read_excel(excel4)

    y1 = dataExcelFile3.iloc[0]
    y2 = dataExcelFile3.iloc[1]
    y3 = dataExcelFile3.iloc[2]
    y4 = dataExcelFile3.iloc[3]
    y5 = dataExcelFile3.iloc[4]
    y6 = dataExcelFile3.iloc[5]

    plt.plot(y1, label = u'Планова чисельність чол. 1 магазин')
    plt.plot(y2, label = u'Планова чисельність чол. 6 магазин')
    plt.plot(y3, label = u'Планова чисельність чол. 7 магазин')
    plt.plot(y4, label = u'Фактична чисельність чол. 1 магазин')
    plt.plot(y5, label = u'Фактична чисельність чол. 6 магазин')
    plt.plot(y6, label = u'Фактична чисельність чол. 7 магазин')

    plt.title("Чисельність чоловік")
    plt.ylabel("Чисельність чоловік")
    plt.xlabel("Квартали")
    plt.legend()
    plt.show()

def openGraphWindow():
    global Window3

    Window3 = QtWidgets.QDialog()
    ui = Ui_Window3()
    ui.setupUi(Window3)
    menu.close()
    Window3.show()

    ui.buttonGraph1.clicked.connect(drawGraph1)
    ui.buttonGraph2.clicked.connect(drawGraph2)

    def returnToMain3():
        Window3.close()
        menu.show()

    ui.buttonMenu3.clicked.connect(returnToMain3)

def saveExcel():
    fname = QFileDialog.getSaveFileName()[0]

    try:
        f = open(fname, "w")
        f.write(excel14)
        f.close()
    except:
        pass

def close():
    QApplication.closeAllWindows()

ui.pushButton_1.clicked.connect(openExcel1)
ui.pushButton_2.clicked.connect(openExcel2)
ui.pushButton_3.clicked.connect(openGraphWindow)
ui.pushButton_4.clicked.connect(saveExcel)
ui.pushButton_5.clicked.connect(close)

sys.exit(app.exec_())
