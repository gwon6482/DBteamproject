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
        self.lineEdit.setValidator(QIntValidator(0, 100, self))
        self.lineEdit.setValidator(QIntValidator(0, 100, self))
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
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        print(now)

        itemtype = {'ramen':1,'drink':2,'snack':3,'bottlewater':4,
                    'television':11,'refrigerator':12,'airconditioner':13,'washingmachine':14,
                    'pencil':21,'pen':23,'sharp':23,'note':24,
                    'shose':31,'pants':32,'underwear':33,'shirts':34}
        sql = "insert into product_purchase (user_id,product_id,date,quantity,price) values('{}',{},'{}',{},{})".format("test_id",
                                                                                                                    itemtype[self.tableWidget.currentRow()[2]],
                                                                                                                    now,
                                                                                                                    self.input_quantity.text(),
                                                                                                                    self.tableWidget.currentRow()[5])

        result = DBconnect.SqlCommand(sql)

        id=self.tableWidget.currentRow()[0]
        quan=self.input_quantity.text()
        self.removeInven(id,quan)
        self.loadInventory()

    #구매시 재고목록 차감
    def removeInven(id,quan):
        DBconnect.SqlCommandResult("update product_register set quantity=quantity-quan where register_log_id=id")












    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 80, 681, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 91, 41))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 470, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 470, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 470, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 440, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 440, 101, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 0, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label_2.setText(_translate("MainWindow", "품목"))
        self.label_3.setText(_translate("MainWindow", "수량"))
        self.pushButton_2.setText(_translate("MainWindow", "이전으로"))


def purchase2Main():
    global mywindow
    mywindow = purchase2()
    mywindow.show()

