import sys
from PyQt5.QtWidgets import *
import LoginPage.Login #login 기능 호출을 위한 import


#main app 실행
app = QApplication(sys.argv)
#어떤 윈도우를 표시할 지는 미정
myWindow = None


#login 기능의 starlogin()을 호출하여 myWindow를 login페이지로 바꿔주고 보여줌
LoginPage.Login.starlogin()
#이후 앱실행
#sys.exit와 함께 실행함으로써 앱 윈도우 종료시 프로그램 자동종료
sys.exit(app.exec_())
