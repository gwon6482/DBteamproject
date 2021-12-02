from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
import LoginPage
import purchase1
import DBconnect
import datetime


class purchase2(QtWidgets.QMainWindow):

    def __init__(self,id_input,seller_input):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.check) #구매하지
        self.pushButton_2.clicked.connect(self.pushButton_2_click)#이전으로

        self.user_id = id_input
        self.seller_id = seller_input
        self.user_name = None
        self.user_sex = None
        self.user_type = None
        self.user_brth = None
        self.user_regist = None
        print("고객",self.user_id,"판매자",self.seller_id)
        inven_list = DBconnect.SqlCommandResult(
            "select register_log_id from product_register where user_id = '{}'".format(self.seller_id))
        print(inven_list)
        if not inven_list:
            print("공란")
        elif inven_list != -1:
            self.loadInventory()
            print("")


    #판매자 목록 창으로 복귀
    def pushButton_2_click(self):
        user=self.user_id
        purchase1.purchase1Main(user)
        self.close()



    #판매자 재고목록 확인
    def loadInventory(self):
        user=self.seller_id
        print(user)
        self.tableWidget.reset();
        inven_list = DBconnect.SqlCommandResult("select * from product_register where user_id = '{}'".format(user))
        self.tableWidget.setHorizontalHeaderLabels(inven_list[0].keys())
        self.tableWidget.setColumnCount(len(inven_list[0]))
        self.tableWidget.setRowCount(len(inven_list))
        tmp = 0;
        if inven_list != -1:
            for row, item in enumerate(inven_list):
                for col, key in enumerate(item.keys()):
                    self.tableWidget.setItem(row, col, QTableWidgetItem("{}".format(item[key])))

                tmp += 1
        else:
            print("")



    def check(self):
        register_log_id_a = self.tableWidget.selectedItems()[0].text()
        print(register_log_id_a)
        quantity_a = self.spinBox.value()
        print(quantity_a)
        sql = "select quantity from product_register where register_log_id = {};".format(register_log_id_a)
        print(sql)
        result = DBconnect.SqlCommandResult(sql)
        quantity_b = result[0]['quantity']
        user=self.user_id
        print(quantity_a, quantity_b)
        if quantity_a <= quantity_b:

            register_log_id_a = self.tableWidget.selectedItems()[0].text()
            print(register_log_id_a)
            seller_id = self.tableWidget.selectedItems()[1].text()
            print(seller_id)
            now = datetime.datetime.now().strftime("%Y-%m-%d")
            print(now)
            quantity_a = self.spinBox.value()
            print(quantity_a)
            price = self.tableWidget.selectedItems()[5].text()
            print(price)

            item = self.tableWidget.selectedItems()[2].text()

            sql = "insert into product_purchase (user_id,product_id,refund,date,quantity,price,register_id) values('{}',{},{},'{}',{},{},{});".format(
                user, item, 0, now, quantity_a, price,register_log_id_a)
            print(sql)
            result = DBconnect.SqlCommand(sql)
            print(sql)
            sql2 = "update product_register set quantity=quantity-{} where register_log_id='{}';".format(quantity_a,
                                                                                                         register_log_id_a)
            print(sql2)
            result = DBconnect.SqlCommand(sql2)

            self.loadInventory()


        else:
            print("구매불가")







    def SetUserData(self,user_data):
        self.user_name = user_data["name"]
        self.user_sex = user_data["sex"]
        self.user_type = user_data["user_type"]
        self.user_brth = user_data["brth"]
        self.user_regist = user_data["register_date"]







    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 80, 791, 321))
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 91, 41))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 470, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 470, 31, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 0, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(230, 470, 42, 22))
        self.spinBox.setObjectName("spinBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
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
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "등록번호"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "판매자id"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "상품id"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "날짜"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "수량"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "가격"))
        self.label.setText(_translate("MainWindow", "상품 목록"))
        self.pushButton.setText(_translate("MainWindow", "구매하기"))
        self.label_3.setText(_translate("MainWindow", "수량"))
        self.pushButton_2.setText(_translate("MainWindow", "이전으로"))


def purchase2Main(id_input,seller_input):
    global mywindow
    mywindow = purchase2(id_input,seller_input)
    mywindow.SetUserData(DBconnect.RequestUserData(id_input))

    mywindow.show()

