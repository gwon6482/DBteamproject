from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
import datetime
import DBconnect
import InventoryPage
from functools import partial
import traceback
import UserProfile_seller

class PuchaseListWin(QtWidgets.QMainWindow):
    def __init__(self, id_input):
        super().__init__()
        self.setupUi(self)
        self.tableWidget.horizontalHeader().setResizeContentsPrecision(QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setStretchLastSection((True))

        #id 추가
        self.user_id = id_input
        self.user_name = None
        self.user_sex = None
        self.user_type = None
        self.user_brth = None
        self.user_regist = None

        #btn events
        self.btn_addinven_2.clicked.connect(self.btnToInven)
        self.btn_addinven_3.clicked.connect(self.btnToProfile)

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
        self.btn_addinven_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addinven_3.setGeometry(QtCore.QRect(140, 420, 101, 41))
        self.btn_addinven_3.setObjectName("btn_addinven_3")
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
        self.btn_addinven_3.setText(_translate("MainWindow", "프로필로"))

    def SetUserData(self, user_data):
        self.user_name = user_data["name"]
        self.user_sex = user_data["sex"]
        self.user_type = user_data["user_type"]
        self.user_brth = user_data["brth"]
        self.user_regist = user_data["register_date"]

    #재고목록 refresh
    def loadPuchaseList(self):
        self.tableWidget.reset();
        sql = "select * from product_purchase;"
        print(sql)
        inven_list = DBconnect.SqlCommandResult(sql)

        itemtype = {1: 'ramen', 2: 'drink',3: 'snack', 4: 'bottlewater',
                    11: 'television', 12: 'refrigerator', 13:'airconditioner', 14:'washingmachine',
                    21: 'pencil' , 22: 'pen',23: 'sharp', 24: 'note',
                    31: 'shose', 32:'pants',33:'underwear', 34:'shirts' }


        try:
            header_list = list(inven_list[0].keys())
            self.tableWidget.setColumnCount(len(inven_list[0]))
            self.tableWidget.setRowCount(len(inven_list))
            self.tableWidget.setHorizontalHeaderLabels(header_list)

            for row, item in enumerate(inven_list):
                # print(x,item)
                for col, key in enumerate(item.keys()):
                    if col == 2 :
                        print(type(item[key]))
                        print(item[key])
                        self.tableWidget.setItem(row, col, QTableWidgetItem("{}".format(itemtype[1])))
                    elif col == 3:
                        txt = "test"
                        if(item[key] == 1):
                            txt = "환불처리됨."
                        else:
                            txt = "정상처리됨."
                        self.tableWidget.setItem(row, col, QTableWidgetItem(txt))
                    else:
                        self.tableWidget.setItem(row, col, QTableWidgetItem("{}".format(item[key])))
                #print(tmp,len(inven_list[0]))

            self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            self.tableWidget.horizontalHeader().setSectionResizeMode(len(inven_list[0])-1, QtWidgets.QHeaderView.Stretch)
        except Exception as e:
            traceback.print_exc()

    def btnToInven(self):
        self.close()
        InventoryPage.startInventoryPage(self.user_id)

    def btnToProfile(self):
        self.close()
        UserProfile_seller.StartUserProfile_customer(self.user_id)


def startPuchaseListPage(input_id):
    global mywindow
    mywindow = PuchaseListWin(input_id)
    mywindow.SetUserData(DBconnect.RequestUserData(input_id))
    mywindow.show()