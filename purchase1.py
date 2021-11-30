from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
import LoginPage
import purchase2
import datetime
import DBconnect
import pymysql

class purchase1(QtWidgets.QMainWindow):

    def __init__(self,id_input):
        super().__init__()
        self.setupUi(self)


        self.pushButton.clicked.connect(self.pushButton_click) #판매자 물품보기
        self.pushButton_2.clicked.connect(self.add_bookmark) #북마크 추가
        self.pushButton_3.clicked.connect(self.Loginbutton_click) #이전으로
        self.pushButton_4.clicked.connect(self.rating) #평점추가
        self.pushButton_5.clicked.connect(self.remove_bookmark)#북마크 삭제
        self.lineEdit.setValidator(QIntValidator(0,100,self))
        self.lineEdit.setValidator(QIntValidator(0, 100, self))
        self.user_id = id_input
        self.user_name = None
        self.user_sex = None
        self.user_type = None
        self.user_brth = None
        self.user_regist = None


        loadseller = DBconnect.SqlCommandResult("Select name from user where user_type=0")
        loadbookmark = DBconnect.SqlCommandResult("select seller_id from bookmark where user_id='{}'".format(self.user_id))
        self.loadInventory()

        if loadseller != -1:
            for i, item in enumerate(loadseller):
                for key in item.keys():
                    self.listWidget.addItem(item[key])
        else:
            self.listWidget.addItem("no items")
        self.listWidget.setCurrentRow(0)

        if loadbookmark != -1:
            for i, item in enumerate(loadbookmark):
                for key in item.keys():
                    self.listWidget_2.addItem(item[key])
        else:
            self.listWidget_2.addItem("no items")
        self.listWidget_2.setCurrentRow(0)





    def loadInventory(self):
        self.tableWidget.reset();
        user=self.user_id
        inven_list = DBconnect.SqlCommandResult("select product_id,date,quantity,price from product_purchase where user_id = '{}'".format(user))
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


    #북마크 추가

    def add_bookmark(self):
        #현재 선택된 리스트의 내용 출력
        #self.listWidget.currentItem().text()
        #이름을 통해 id를 찾는 쿼리
        sql1 = "select user_id from user where name = '{}';".format(self.listWidget.currentItem().text())
        #print(sql1)
        result = DBconnect.SqlCommandResult(sql1)

        name = result[0]['user_id']
        user=self.user_id
        print(user)
        #정상적인 쿼리
        sql = "insert into bookmark (user_id, seller_id) values('{}','{}');".format(user, name)
        print(sql)

        result = DBconnect.SqlCommand(sql)
        purchase1Main(user)
        self.close()
        #추후 북마크 리스트를 보여주는 코드 추가해주세요.

        """
        sql = "insert into bookmark (user_id,seller_id) value('{}','{}')".format("test_id",DBconnect.SqlCommandResult("select user_id from user where name = self.listWidget.currentItem().text()"))
        result = DBconnect.SqlCommand(sql)
        """

    def remove_bookmark(self):

        #sql1 = "select user_id from user where name = '{}';".format(self.listWidget_2.currentItem().text())

        #result = DBconnect.SqlCommandResult(sql1)
        #print(sql1)
        #userid=result[0]
        #print(userid)

        seller = self.listWidget_2.currentItem().text()
        print(seller)
        user = self.user_id
        print(user)
        sql = "delete from bookmark where user_id = '{}' AND seller_id = '{}';".format(user,seller)
        print(sql)
        result = DBconnect.SqlCommand(sql)
        purchase1Main(user)
        self.close()




    #평점 추가
    def rating(self):
        #register_log=self.tableWidget.selectedItems()[0].text()
        #print(register_log)
        print(self.spinBox.value())
        user = self.user_id
        sql = "insert into rating (product_id,user_id,score) value('{}','{}',{});".format(self.tableWidget.selectedItems()[0].text(),
                                                                                         user,
                                                                                         self.spinBox.value())
        print(sql)
        result = DBconnect.SqlCommand(sql)






    #판매자 물품 보기

    def pushButton_click(self):
        user=self.user_id
        seller=self.listWidget_2.currentItem().text()
        print(user,seller)
        purchase2.purchase2Main(user,seller)
        self.close()

    #이전으로

    def Loginbutton_click(self):
        LoginPage.startLoginPage()
        self.close()






    def SetUserData(self,user_data):
        self.user_name = user_data["name"]
        self.user_sex = user_data["sex"]
        self.user_type = user_data["user_type"]
        self.user_brth = user_data["brth"]
        self.user_regist = user_data["register_date"]










    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 90, 411, 381))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 411, 361))
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 0, 411, 361))
        self.listWidget_2.setObjectName("listWidget_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 30, 71, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 20, 131, 31))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 70, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(760, 0, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 30, 61, 21))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(450, 110, 361, 361))
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(720, 80, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(670, 80, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 70, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.label.setText(_translate("MainWindow", "판매자 목록"))
        self.pushButton.setText(_translate("MainWindow", "판매자 물품 보기"))
        self.pushButton_2.setText(_translate("MainWindow", "북마크 추가"))
        self.pushButton_3.setText(_translate("MainWindow", "이전으로"))
        self.label_2.setText(_translate("MainWindow", "구매내역"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "상품id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "구매일자"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "수량"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "가격"))
        self.pushButton_4.setText(_translate("MainWindow", "평점추가"))
        self.pushButton_5.setText(_translate("MainWindow", "북마크 삭제"))



def purchase1Main(id_input):
    global mywindow
    mywindow = purchase1(id_input)
    mywindow.SetUserData(DBconnect.RequestUserData(id_input))
    mywindow.show()

