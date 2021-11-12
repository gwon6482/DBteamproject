import sys
from PyQt5.QtWidgets import * #pyqt를 위한 라이브러리
from PyQt5 import uic #ui파일을 불러오기위한 라이브러리
import RegisterPage.register #register기능으로 넘어가기 위한 import

#UI파일 연결
form_class = uic.loadUiType("./ui/Login.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼 및 필드의 이름은 QtDesignder 사용시 오프젝트 이름으로 설정합니다.
        #이후 각 오브젝트의 메소드를 이용해 정의한 함수와 connect해주시면 됩니다.

        self.login_button.clicked.connect(self.login_clicked)
        #login_button 클릭시 login_clicked 함수와 연결합니다.
        self.register_button.clicked.connect(self.regitser_clicked)
        self.quit_button.clicked.connect(self.QuitProgram)


    def QuitProgram(self):
        sys.exit()



    #login_clicked 버튼 클릭시 호출되는 함수
    def login_clicked(self):
        #메세지 호출
        print("login button is cilcked")
        #id_input 라인에 적인 값을 출력
        print(self.id_input.text())
        #password_input 라인에 적힌값을 출력
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

