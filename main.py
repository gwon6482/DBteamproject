import sys
from PyQt5.QtWidgets import *
import temp_mainPage
import LoginPage
import InventoryPage

"""

main의 내용은 고정입니다.

모든 테스트가 끝난 후에 
temp_mainPage.StartTempMain() 를 
LoginPage.StartLogin() 으로 바꿔주면 앱이 완성됩니다. 

"""

app = QApplication(sys.argv)    #앱 생성
mywindow = None                 #윈도우 생성
LoginPage.startLoginPage()   #로그인 페이지 불러오기
sys.exit(app.exec_())           #앱 실행 및 종료



