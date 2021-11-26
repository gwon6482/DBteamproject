from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
import LoginPage
import purchase2
import datetime
import DBconnect
import pymysql

class purchase1(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.pushButton.clicked.connect(self.pushButton_click) #판매자 물품보기
        self.pushButton_2.clicked.connect(self.add_bookmark) #북마크 추가
        self.pushButton_3.clicked.connect(self.Loginbutton_click) #이전으로
        self.pushButton_4.clicked.connect(self.rating) #평점추가
        self.lineEdit.setValidator(QIntValidator(0,100,self))
        self.lineEdit.setValidator(QIntValidator(0, 100, self))



        loadseller = DBconnect.SqlCommandResult("Select name from user where user_type=1")
        loadbookmark = DBconnect.SqlCommandResult("Select seller_id from bookmark where user_id = 'test_id'")
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


    #북마크 추가

    def add_bookmark(self):
        sql = "insert into bookmark (user_id,seller_id) value('{}','{}')".format("test_id","customer")
        result = DBconnect.SqlCommand(sql)
        """
        sql = "insert into bookmark (user_id,seller_id) value('{}','{}')".format("test_id",DBconnect.SqlCommandResult("select user_id from user where name = self.listWidget.currentItem().text()"))
        result = DBconnect.SqlCommand(sql)
        """

    #평점 추가
    def rating(self):
        sql = "insert into rating (product_id,user_id,score) value('{}','{}',{})".format(self.tableWidget.currentItem(),
                                                                                         "test_id",
                                                                                         self.spinBox.value())
        result = DBconnect.SqlCommand(sql)






    #판매자 물품 보기

    def pushButton_click(self):
        purchase2.purchase2Main()
        self.close()

    #이전으로

    def Loginbutton_click(self):
        LoginPage.startLoginPage()
        self.close()










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
        self.pushButton_2.setGeometry(QtCore.QRect(320, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(760, 0, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 30, 61, 21))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(450, 110, 361, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(720, 80, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(670, 80, 42, 22))
        self.spinBox.setObjectName("spinBox")
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
        self.pushButton_4.setText(_translate("MainWindow", "평점추가"))



def purchase1Main():
    global mywindow
    mywindow = purchase1()
    mywindow.show()

