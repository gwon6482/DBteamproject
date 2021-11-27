from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
import datetime
import DBconnect
import InventoryPage
from functools import partial
import traceback

class PuchaseListWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableWidget.horizontalHeader().setResizeContentsPrecision(QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setStretchLastSection((True))

        #btn events
        self.btn_addinven_2.clicked.connect(self.btnToInven)

        #추후 함수화시킬 예정
        index_product = DBconnect.SqlCommandResult("Select name from product")
        self.loadPuchaseList()
        #print(type(index_product.values()))


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 81, 31))
        self.label.setObjectName("label")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(40, 50, 81, 31))
        self.label_username.setObjectName("label_username")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 100, 691, 301))
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.btn_addinven_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addinven_2.setGeometry(QtCore.QRect(30, 420, 101, 41))
        self.btn_addinven_2.setObjectName("btn_addinven_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "판매관리"))
        self.label_username.setText(_translate("MainWindow", "사용자:"))
        self.btn_addinven_2.setText(_translate("MainWindow", "재고목록"))


    #재고목록 refresh
    def loadPuchaseList(self):
        self.tableWidget.reset();
        inven_list = DBconnect.SqlCommandResult("select * from product_purchase where user_id = 'test_id'")
        header_list = list(inven_list[0].keys())
        self.tableWidget.setHorizontalHeaderLabels(header_list)
        self.tableWidget.setColumnCount(len(inven_list[0]))
        self.tableWidget.setRowCount(len(inven_list))

        if inven_list != -1:
            for row, item in enumerate(inven_list):
                # print(x,item)
                for col, key in enumerate(item.keys()):
                    #print(col, item[key])
                    self.tableWidget.setItem(row, col, QTableWidgetItem("{}".format(item[key])))
                #print(tmp,len(inven_list[0]))

            self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            self.tableWidget.horizontalHeader().setSectionResizeMode(len(inven_list[0])-1, QtWidgets.QHeaderView.Stretch)
        else:
            print("")
            # do nothing

    def btnToInven(self):
        InventoryPage.startInventoryPage()
        self.close()




def startPuchaseListPage():
    global mywindow
    mywindow = PuchaseListWin()
    mywindow.show()