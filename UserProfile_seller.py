from PyQt5 import QtCore, QtGui, QtWidgets
import DBconnect

import traceback

import InventoryPage
import PuchaseListPage




class UserProfilePage_seller(QtWidgets.QMainWindow):
    def __init__(self,id_input):
        super().__init__()
        self.setupUi(self)
        try:
            self.SalesHistoryListButton.clicked.connect(self.SalesHistoryListButtonClicked)
            self.ProductListButton.clicked.connect(self.ProductListButtonClicked)
        except Exception as e:
            traceback.print_exc()

        self.user_id = id_input
        self.user_name = None
        self.user_sex = None
        self.user_type = None
        self.user_brth = None
        self.user_regist = None

    def SetUserData(self,user_data):
        self.user_name = user_data["name"]
        self.user_sex = user_data["sex"]
        self.user_type = user_data["user_type"]
        self.user_brth = user_data["brth"]
        self.user_regist = user_data["register_date"]

        self.NameBrowser.setPlainText(self.user_name)
        self.IDBrowser.setPlainText(self.user_id)
        if self.user_sex == 1:
            self.SexBrowser.setPlainText("male")
        else:
            self.SexBrowser.setPlainText("female")
        if self.user_type == 1:
            self.UsertypeBrowser.setPlainText("Customer")
        else:
            self.UsertypeBrowser.setPlainText("Seller")
        self.BirthBrowser.setPlainText(str(self.user_brth))
        self.RigisterBrowser.setPlainText(str(self.user_regist))

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 392)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 180, 60, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(100, 260, 60, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.BirthBrowser = QtWidgets.QTextBrowser(Dialog)
        self.BirthBrowser.setGeometry(QtCore.QRect(180, 260, 81, 21))
        self.BirthBrowser.setObjectName("BirthBrowser")
        self.SalesHistoryListButton = QtWidgets.QPushButton(Dialog)
        self.SalesHistoryListButton.setGeometry(QtCore.QRect(360, 220, 161, 61))
        self.SalesHistoryListButton.setObjectName("SalesHistoryListButton")
        self.RigisterBrowser = QtWidgets.QTextBrowser(Dialog)
        self.RigisterBrowser.setGeometry(QtCore.QRect(180, 300, 81, 21))
        self.RigisterBrowser.setObjectName("RigisterBrowser")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 220, 60, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.IDBrowser = QtWidgets.QTextBrowser(Dialog)
        self.IDBrowser.setGeometry(QtCore.QRect(180, 140, 81, 21))
        self.IDBrowser.setObjectName("IDBrowser")
        self.UsertypeBrowser = QtWidgets.QTextBrowser(Dialog)
        self.UsertypeBrowser.setGeometry(QtCore.QRect(180, 220, 81, 21))
        self.UsertypeBrowser.setObjectName("UsertypeBrowser")
        self.ProductListButton = QtWidgets.QPushButton(Dialog)
        self.ProductListButton.setGeometry(QtCore.QRect(360, 120, 161, 61))
        self.ProductListButton.setObjectName("ProductListButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 60, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.NameBrowser = QtWidgets.QTextBrowser(Dialog)
        self.NameBrowser.setGeometry(QtCore.QRect(180, 100, 81, 21))
        self.NameBrowser.setObjectName("NameBrowser")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 20, 181, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 140, 60, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(90, 300, 71, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.SexBrowser = QtWidgets.QTextBrowser(Dialog)
        self.SexBrowser.setGeometry(QtCore.QRect(180, 180, 81, 21))
        self.SexBrowser.setObjectName("SexBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Sex"))
        self.label_6.setText(_translate("Dialog", "BirthDay"))
        self.SalesHistoryListButton.setText(_translate("Dialog", "Sales history"))
        self.label_5.setText(_translate("Dialog", "UserType"))
        self.ProductListButton.setText(_translate("Dialog", "Product List"))
        self.label_2.setText(_translate("Dialog", "Name"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:36pt;\">user profile</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "ID"))
        self.label_7.setText(_translate("Dialog", "RigisterDay"))

    def SalesHistoryListButtonClicked(self):
        self.close()
        PuchaseListPage.startPuchaseListPage(self.user_id)

    def ProductListButtonClicked(self):
        try:
            self.close()
            InventoryPage.startInventoryPage(self.user_id)
        except Exception as e :
            print(e)
            traceback.print_exc()

def StartUserProfile_customer(id_input):
    global mywindow
    mywindow = UserProfilePage_seller(id_input)
    mywindow.SetUserData(DBconnect.RequestUserData(id_input))
    mywindow.show()