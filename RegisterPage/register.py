from PyQt5.QtWidgets import *
from PyQt5 import uic
import LoginPage.Login


#UI파일 연결
form_class = uic.loadUiType("./ui/Register.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :

        self.sex = None
        self.usertype = None

        super().__init__()
        self.setupUi(self)

        #등록버튼을 누를 경우 register_button_clicked 함수를 호출
        self.register_button.clicked.connect(self.register_button_clicked)
        self.cancel_button.clicked.connect(self.returnToLogin)
        self.male_radiobutton.clicked.connect(self.changeSex_male)
        self.female_radiobutton.clicked.connect(self.changeSex_female)
        self.customer_radioButton.clicked.connect(self.changeUsertype_customer)
        self.seller_radioButton.clicked.connect(self.changeUsertype_seller)



    def returnToLogin(self):
        LoginPage.Login.starlogin()
        self.close()

    def changeUsertype_customer(self):
        self.usertype = 0

    def changeUsertype_seller(self):
        self.usertype = 1

    def changeSex_male(self):
        self.sex = 0

    def changeSex_female(self):
        self.sex = 1


    def register_button_clicked(self):
        print("register button clicked")
        print(self.usertype)
        print(self.id_input.text())
        print(self.pwd_input.text())
        print(self.pwd_agn_input.text())
        print(self.name_input.text())
        print(self.phone_input.text())
        print(self.sex)
        print(self.birth_calendar.selectedDate().toString())



def starRegister():
    #메인에 있는 myWindow를 불러옴
    #Login페이지를 윈도우로 설정한다음 보여줌
    global myWindow
    myWindow = WindowClass()
    myWindow.show()

