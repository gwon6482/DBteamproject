from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
import datetime
import DBconnect


class InventoryWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #버튼 이벤트 추가
        self.btn_addinven.clicked.connect(self.addInven)

        #self.input_quantity.settext("quantity")
        self.input_quantity.setValidator(QIntValidator(0,100,self))
        #self.input_quantity.settext("price")
        self.input_price.setValidator(QIntValidator(0,9999999,self))

        #추후 함수화시킬 예정
        index_product = DBconnect.SqlCommand("Select name from product")
        self.loadInventory()
        #print(type(index_product.values()))

        if index_product != -1:
           for i,item in enumerate(index_product):
               for key in item.keys() :
                   print(i,key)
                   print(type(item[key]))
                   print(item[key])
                   self.listWidget.addItem(item[key])
               #print(type(str(item.values())))
               #print(item.values())
        else :
            self.listWidget.addItem("no items")
        self.listWidget.setCurrentRow(0)


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
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.btn_addinven = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addinven.setGeometry(QtCore.QRect(620, 410, 101, 41))
        self.btn_addinven.setObjectName("btn_addinven")
        self.input_quantity = QtWidgets.QLineEdit(self.centralwidget)
        self.input_quantity.setGeometry(QtCore.QRect(430, 440, 113, 20))
        self.input_quantity.setObjectName("input_quantity")
        self.input_price = QtWidgets.QLineEdit(self.centralwidget)
        self.input_price.setGeometry(QtCore.QRect(430, 500, 113, 20))
        self.input_price.setObjectName("input_price")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(305, 410, 111, 131))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 410, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 470, 81, 31))
        self.label_3.setObjectName("label_3")
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

    #재고목록 refresh
    def loadInventory(self):
        self.tableWidget.reset();
        inven_list = DBconnect.SqlCommand("select * from product_register where user_id = 'test_id'")
        self.tableWidget.setHorizontalHeaderLabels(inven_list[0].keys())
        self.tableWidget.setColumnCount(len(inven_list[0]))
        self.tableWidget.setRowCount(len(inven_list))

        # print(len(inven_list))
        # print(len(inven_list[0]))
        if inven_list != -1:
            for x, item in enumerate(inven_list):
                # print(x,item)
                for y, key in enumerate(item.keys()):
                    # print(y, item[key])
                    self.tableWidget.setItem(x, y, QTableWidgetItem("{}".format(item[key])))
        else:
            print("")
            # do nothing

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "재고 관리"))
        self.label_username.setText(_translate("MainWindow", "사용자:"))

    #재고목록 추가
    def addInven(self):
        #self.input_quantity.text()
        print(self.listWidget.currentItem().text())
        print(self.input_quantity.text())
        print(self.input_price.text())
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        print(now)

        itemtype = {'ramen':1,'drink':2,'snack':3,'bottlewater':4,
                    'television':11,'refrigerator':12,'airconditioner':13,'washingmachine':14,
                    'pencil':21,'pen':23,'sharp':23,'note':24,
                    'shose':31,'pants':32,'underwear':33,'shirts':34}
        sql = "insert into product_register (user_id,product_id,date,quantity,price) values('{}',{},'{}',{},{})".format("test_id",
                                                                                                                    itemtype[self.listWidget.currentItem().text()],
                                                                                                                    now,
                                                                                                                    self.input_quantity.text(),
                                                                                                                    self.input_price.text())
        print(sql)
        result = DBconnect.SqlCommand(sql)
        self.loadInventory()


def startInventoryPage():
    global mywindow
    mywindow = InventoryWin()
    mywindow.show()
