from PyQt5 import QtCore, QtGui, QtWidgets
import DBconnect
import RegisterPage

class LoginWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.LoginButton.clicked.connect(self.LoginCheckByDB)
        self.RegisterButton.clicked.connect(self.RegisterButtonClicked)

    def RegisterButtonClicked(self):
        RegisterPage.StartRegister()
        self.close()

    def LoginCheckByDB(self):
        try:
            id = self.ID_input.text()
            pwd = self.PW_input.text()
            Login_result =  DBconnect.LoginCheck(id,pwd)
            #로그인 성공
            #이후 프로필 페이지로 이동
            if Login_result == 1:
                print("login succcess")
                DBconnect.show_popup_ok("login success","login success")
                #여기에 해당 프로필로 이동 구현
            else:
                print("login fail")
                #여기에 실페 메세지 출력 함수 구현
                DBconnect.show_popup_ok("login fail","there is no match id")

        except:
            #로그인 실패
            #경고 메세지 출력

            #실패 케이스 1 : 아이디나 패스워드칸이 빈칸
            if self.ID_input.text() == "" or self.PW_input.text() == "":
                DBconnect.show_popup_ok("fail","id or pwd is null")


            #실패 케이스 2 : 입력정보와 매칭되는 데이터 없음


    #팝업메세지 필요하시면 이 함수 사용하시면 됩니다.



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(588, 426)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 90, 121, 51))
        self.label.setObjectName("label")
        self.ID_input = QtWidgets.QLineEdit(Dialog)
        self.ID_input.setGeometry(QtCore.QRect(240, 160, 113, 21))
        self.ID_input.setObjectName("ID_input")
        self.PW_input = QtWidgets.QLineEdit(Dialog)
        self.PW_input.setGeometry(QtCore.QRect(240, 190, 113, 21))
        self.PW_input.setObjectName("PW_input")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 160, 60, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(170, 190, 60, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.LoginButton = QtWidgets.QPushButton(Dialog)
        self.LoginButton.setGeometry(QtCore.QRect(170, 230, 113, 32))
        self.LoginButton.setObjectName("LoginButton")
        self.RegisterButton = QtWidgets.QPushButton(Dialog)
        self.RegisterButton.setGeometry(QtCore.QRect(290, 230, 113, 32))
        self.RegisterButton.setObjectName("RegisterButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt;\">Login Page</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "ID"))
        self.label_3.setText(_translate("Dialog", "PW"))
        self.LoginButton.setText(_translate("Dialog", "Login"))
        self.RegisterButton.setText(_translate("Dialog", "Register"))


def startLoginPage():
    global mywindow
    mywindow = LoginWin()
    mywindow.show()