from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
import datetime
import DBconnect
import PuchaseListPage
from functools import partial
import traceback

import UserProfile_seller


class InventoryWin(QtWidgets.QMainWindow):
    def __init__(self, id_input):
        super().__init__()
        self.setupUi(self)
        self.tableWidget.horizontalHeader().setResizeContentsPrecision(QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setStretchLastSection((True))

        # id 추가
        self.user_id = id_input
        self.user_name = None
        self.user_sex = None
        self.user_type = None
        self.user_brth = None
        self.user_regist = None

        self.label_username.setText("사용자 : {}".format(self.user_id))

        # 버튼 이벤트 추가
        self.btn_addinven.clicked.connect(self.addInven)
        self.btn_purchaseList.clicked.connect(self.btnToPurchaseList)
        self.btn_profile.clicked.connect(self.btnToProfile)

        # self.input_quantity.settext("quantity")
        self.input_quantity.setValidator(QIntValidator(0, 100, self))
        # self.input_quantity.settext("price")
        self.input_price.setValidator(QIntValidator(0, 9999999, self))

        # 추후 함수화시킬 예정
        index_product = DBconnect.SqlCommandResult("Select name from product")
        self.loadInventory()
        # print(type(index_product.values()))

        if index_product != -1:
            for i, item in enumerate(index_product):
                for key in item.keys():
                    # print(i,key)
                    # print(type(item[key]))
                    # print(item[key])
                    self.listWidget.addItem(item[key])
                # print(type(str(item.values())))
                # print(item.values())
        else:
            self.listWidget.addItem("no items")
        self.listWidget.setCurrentRow(0)

    def SetUserData(self, user_data):
        self.user_name = user_data["name"]
        self.user_sex = user_data["sex"]
        self.user_type = user_data["user_type"]
        self.user_brth = user_data["brth"]
        self.user_regist = user_data["register_date"]

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
        self.btn_addinven = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addinven.setGeometry(QtCore.QRect(150, 500, 101, 41))
        self.btn_addinven.setObjectName("btn_addinven")
        self.input_quantity = QtWidgets.QLineEdit(self.centralwidget)
        self.input_quantity.setGeometry(QtCore.QRect(150, 450, 113, 20))
        self.input_quantity.setObjectName("input_quantity")
        self.input_price = QtWidgets.QLineEdit(self.centralwidget)
        self.input_price.setGeometry(QtCore.QRect(290, 450, 113, 20))
        self.input_price.setObjectName("input_price")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 430, 111, 111))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 410, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 410, 81, 31))
        self.label_3.setObjectName("label_3")
        self.btn_purchaseList = QtWidgets.QPushButton(self.centralwidget)
        self.btn_purchaseList.setGeometry(QtCore.QRect(260, 500, 101, 41))
        self.btn_purchaseList.setObjectName("btn_purchaseList")
        self.btn_profile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_profile.setGeometry(QtCore.QRect(370, 500, 101, 41))
        self.btn_profile.setObjectName("btn_profile")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 400, 81, 31))
        self.label_4.setObjectName("label_4")
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
        self.label.setText(_translate("MainWindow", "재고 관리"))
        self.label_username.setText(_translate("MainWindow", "사용자:"))
        self.btn_addinven.setText(_translate("MainWindow", "재고추가"))
        #self.input_quantity.setText(_translate("MainWindow", "quantity"))
        #self.input_price.setText(_translate("MainWindow", "price"))
        self.input_quantity.setPlaceholderText("수량 입력")
        self.input_price.setPlaceholderText("가격 입력")
        self.label_2.setText(_translate("MainWindow", "수량"))
        self.label_3.setText(_translate("MainWindow", "가격"))
        self.btn_purchaseList.setText(_translate("MainWindow", "판매기록"))
        self.btn_profile.setText(_translate("MainWindow", "프로필로"))
        self.label_4.setText(_translate("MainWindow", "상품목록"))

    # 재고목록 refresh
    def loadInventory(self):
        self.tableWidget.reset();
        sql = "select register_log_id product_id, date, quantity, price from product_register where user_id = '{}'".format(self.user_id)
        inven_list = DBconnect.SqlCommandResult(sql)

        try:
            header_list = list(inven_list[0].keys())
            print(header_list)
            header_list.append(" ")
            # header_list.append(" ")
            self.tableWidget.setColumnCount(len(header_list))
            self.tableWidget.setRowCount(len(inven_list))
            self.tableWidget.setHorizontalHeaderLabels(header_list)

            # print(len(inven_list))
            # print(len(inven_list[0]))
            tmp = 0
            for row, item in enumerate(inven_list):
                # print(x,item)
                for col, key in enumerate(item.keys()):
                    self.tableWidget.setItem(row, col, QTableWidgetItem("{}".format(item[key])))

                    #print(tmp,len(inven_list[0]))

                button = QPushButton("삭제", self)
                self.tableWidget.setCellWidget(row, len(header_list)-1, button)
                button.clicked.connect(partial(self.removeInven, self.tableWidget.item(row, 0).text()))
                self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(len(inven_list[0]),QtWidgets.QHeaderView.Stretch)
                self.tableWidget.currentItemChanged.connect(self.cellchange)
        except Exception as e:
            print(e)
            traceback.print_exc()

        #finally :
            #

    # 재고목록 추가
    def addInven(self):
        # self.input_quantity.text()
        # print(self.listWidget.currentItem().text())
        # print(self.input_quantity.text())
        # print(self.input_price.text())
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        print(now)

        itemtype = {'ramen': 1, 'drink': 2, 'snack': 3, 'bottlewater': 4,
                    'television': 11, 'refrigerator': 12, 'airconditioner': 13, 'washingmachine': 14,
                    'pencil': 21, 'pen': 23, 'sharp': 23, 'note': 24,
                    'shose': 31, 'pants': 32, 'underwear': 33, 'shirts': 34}
        product_id = itemtype[self.listWidget.currentItem().text()]
        quant = self.input_quantity.text()
        price = self.input_price.text()
        sql = "insert into product_register (user_id,product_id,date,quantity,price) values('{}',{},'{}',{},{})".format(
            self.user_id, product_id, now, quant, price)
        # print(sql)
        result = DBconnect.SqlCommand(sql)
        self.loadInventory()

    # 해당 row 삭제(확인 메시지 뜬후)
    def removeInven(self, num):
        reply = QMessageBox.question(self, 'Message', '삭제하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                print("clicked!{}".format(num))
                # DELETE FROM product_register where register_log_id = '1' and user_id = 'test_id';
                DBconnect.SqlCommand(
                    "DELETE FROM product_register where register_log_id = {} AND  user_id = '{}';".format(num,self.user_id))
                self.loadInventory()
            except Exception as e:
                traceback.print_exc()

    def btnToProfile(self):
        self.close()
        UserProfile_seller.StartUserProfile_customer(self.user_id)

    def btnToPurchaseList(self):
        self.close()
        PuchaseListPage.startPuchaseListPage(self.user_id)

    def cellchange(self):
        item = self.tableWidget.selectedItems()
        print("current row : {}".format(self.tableWidget.currentRow()))
        for i in item:
            print(i.text())

def startInventoryPage(id_input):
    global mywindow
    mywindow = InventoryWin(id_input)
    mywindow.SetUserData(DBconnect.RequestUserData(id_input))
    mywindow.show()
