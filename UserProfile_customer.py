from PyQt5 import QtCore, QtGui, QtWidgets
import DBconnect

class UserProfilePage_customer(QtWidgets.QMainWindow):
    def __init__(self,id_input):
        super().__init__()
        # 객체 생성시 id값을 받아 해당 id의 프로필을 출력


        self.setupUi(self)


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







    def setupUi(self, SexBrowser_2):
        SexBrowser_2.setObjectName("SexBrowser_2")
        SexBrowser_2.resize(652, 387)
        self.label = QtWidgets.QLabel(SexBrowser_2)
        self.label.setGeometry(QtCore.QRect(230, 0, 181, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(SexBrowser_2)
        self.label_2.setGeometry(QtCore.QRect(90, 80, 60, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(SexBrowser_2)
        self.label_3.setGeometry(QtCore.QRect(90, 120, 60, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(SexBrowser_2)
        self.label_4.setGeometry(QtCore.QRect(90, 160, 60, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(SexBrowser_2)
        self.label_5.setGeometry(QtCore.QRect(90, 200, 60, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(SexBrowser_2)
        self.label_6.setGeometry(QtCore.QRect(90, 240, 60, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(SexBrowser_2)
        self.label_7.setGeometry(QtCore.QRect(80, 280, 71, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.NameBrowser = QtWidgets.QTextBrowser(SexBrowser_2)
        self.NameBrowser.setGeometry(QtCore.QRect(170, 80, 81, 21))
        self.NameBrowser.setObjectName("NameBrowser")
        self.IDBrowser = QtWidgets.QTextBrowser(SexBrowser_2)
        self.IDBrowser.setGeometry(QtCore.QRect(170, 120, 81, 21))
        self.IDBrowser.setObjectName("IDBrowser")
        self.SexBrowser = QtWidgets.QTextBrowser(SexBrowser_2)
        self.SexBrowser.setGeometry(QtCore.QRect(170, 160, 81, 21))
        self.SexBrowser.setObjectName("SexBrowser")
        self.UsertypeBrowser = QtWidgets.QTextBrowser(SexBrowser_2)
        self.UsertypeBrowser.setGeometry(QtCore.QRect(170, 200, 81, 21))
        self.UsertypeBrowser.setObjectName("UsertypeBrowser")
        self.BirthBrowser = QtWidgets.QTextBrowser(SexBrowser_2)
        self.BirthBrowser.setGeometry(QtCore.QRect(170, 240, 81, 21))
        self.BirthBrowser.setObjectName("BirthBrowser")
        self.RigisterBrowser = QtWidgets.QTextBrowser(SexBrowser_2)
        self.RigisterBrowser.setGeometry(QtCore.QRect(170, 280, 81, 21))
        self.RigisterBrowser.setObjectName("RigisterBrowser")
        self.ProductListButton = QtWidgets.QPushButton(SexBrowser_2)
        self.ProductListButton.setGeometry(QtCore.QRect(350, 100, 161, 61))
        self.ProductListButton.setObjectName("ProductListButton")
        self.FavoritMarketButton = QtWidgets.QPushButton(SexBrowser_2)
        self.FavoritMarketButton.setGeometry(QtCore.QRect(350, 170, 161, 61))
        self.FavoritMarketButton.setObjectName("FavoritMarketButton")
        self.BuyListButton = QtWidgets.QPushButton(SexBrowser_2)
        self.BuyListButton.setGeometry(QtCore.QRect(350, 240, 161, 61))
        self.BuyListButton.setObjectName("BuyListButton")

        self.retranslateUi(SexBrowser_2)
        QtCore.QMetaObject.connectSlotsByName(SexBrowser_2)

    def retranslateUi(self, SexBrowser_2):
        _translate = QtCore.QCoreApplication.translate
        SexBrowser_2.setWindowTitle(_translate("SexBrowser_2", "Dialog"))
        self.label.setText(_translate("SexBrowser_2", "<html><head/><body><p><span style=\" font-size:36pt;\">user profile</span></p></body></html>"))
        self.label_2.setText(_translate("SexBrowser_2", "Name"))
        self.label_3.setText(_translate("SexBrowser_2", "ID"))
        self.label_4.setText(_translate("SexBrowser_2", "Sex"))
        self.label_5.setText(_translate("SexBrowser_2", "UserType"))
        self.label_6.setText(_translate("SexBrowser_2", "BirthDay"))
        self.label_7.setText(_translate("SexBrowser_2", "RigisterDay"))
        self.ProductListButton.setText(_translate("SexBrowser_2", "Product List"))
        self.FavoritMarketButton.setText(_translate("SexBrowser_2", "Favorit Market"))
        self.BuyListButton.setText(_translate("SexBrowser_2", "Buy list"))

def StartUserProfile_customer(id_input):
    global mywindow
    mywindow = UserProfilePage_customer(id_input)
    mywindow.SetUserData(DBconnect.RequestUserData(id_input))
    mywindow.show()
