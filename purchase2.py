from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
import LoginPage
import purchase1
import DBconnect
import datetime


class purchase2(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.purchase) #구매하지
        self.pushButton_2.clicked.connect(self.pushButton_2_click)#이전으로
        self.loadInventory()



    #판매자 목록 창으로 복귀
    def pushButton_2_click(self):
        purchase1.purchase1Main()
        self.close()



    #판매자 재고목록 확인
    def loadInventory(self):
        self.tableWidget.reset();
        inven_list = DBconnect.SqlCommandResult("select * from product_register where user_id = 'test_id'")
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

    #구매 기록
    def purchase(self):




        register_log_id=self.tableWidget.selectedItems()[0].text()
        print(register_log_id)
        seller_id=self.tableWidget.selectedItems()[1].text()
        print(seller_id)
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        print(now)
        quantity = self.spinBox.value()
        print(quantity)
        price = self.tableWidget.selectedItems()[5].text()
        print(price)


        item = self.tableWidget.selectedItems()[2].text()

        sql = "insert into product_purchase (user_id,product_id,date,quantity,price) values('{}',{},'{}',{},{});".format("test_id",item,now,quantity,price)
        print(sql)
        result = DBconnect.SqlCommand(sql)
        #removeInven(register_log_id,quantity)

        self.loadInventory()




    #구매시 재고목록 차감
    def removeInven(id,quan):
        DBconnect.SqlCommandResult("update product_register set quantity=quantity-quan where register_log_id=id")












    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 80, 791, 321))
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
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
        self.label.setText(_translate("MainWindow", "상품 목록"))
        self.pushButton.setText(_translate("MainWindow", "구매하기"))
        self.label_3.setText(_translate("MainWindow", "수량"))
        self.pushButton_2.setText(_translate("MainWindow", "이전으로"))


def purchase2Main():
    global mywindow
    mywindow = purchase2()
    mywindow.show()

