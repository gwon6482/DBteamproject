import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import RegisterPage.register

#UI파일 연결
#UI파일의 위치는 절대경로로 삽입바랍니다.
form_class = uic.loadUiType("./ui/Login.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.login_button.clicked.connect(self.login_clicked)
        self.register_button.clicked.connect(self.regitser_clicked)
        self.quit_button.clicked.connect(self.QuitProgram)


    def QuitProgram(self):
        sys.exit()



    def login_clicked(self):
        print("login button is cilcked")
        print(self.id_input.text())
        print(self.password_input.text())



    def regitser_clicked(self):
        RegisterPage.register.starRegister()
        self.close()


def starlogin():
    #메인에 있는 myWindow를 불러옴
    #Login페이지를 윈도우로 설정한다음 보여줌
    global myWindow
    myWindow = WindowClass()
    myWindow.show()

