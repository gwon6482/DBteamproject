import sys
from PyQt5.QtWidgets import *
import OrderPage.order
import LoginPage.Login
import RegisterPage.register


#main app 실행
app = QApplication(sys.argv)
#어떤 윈도우를 표시할 지는 미정
myWindow = None

LoginPage.Login.starlogin()
sys.exit(app.exec_())
