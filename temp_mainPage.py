from PyQt5 import QtCore, QtGui, QtWidgets
import LoginPage

class temp_main(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.TestButton.clicked.connect(self.testbuttonClicked) # 테스트 버튼에 연결해 보겠습니다.
        self.Loginbutton.clicked.connect(self.Loginbutton_click)
        """
                이 부분에 테스트를 원하는 기능과 연결하신 후
                테스트 하시면 됩니다.
        
        """
    def testbuttonClicked(self):
        pass


    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(490, 166)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 20, 281, 51))
        self.label.setObjectName("label")
        self.TestButton = QtWidgets.QPushButton(Dialog)
        self.TestButton.setGeometry(QtCore.QRect(240, 100, 113, 32))
        self.TestButton.setObjectName("TestButton")
        self.Loginbutton = QtWidgets.QPushButton(Dialog)
        self.Loginbutton.setGeometry(QtCore.QRect(120, 100, 113, 32))
        self.Loginbutton.setObjectName("Loginbutton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)





    def Loginbutton_click(self):
        LoginPage.startLoginPage()
        self.close()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:36pt;\">임시 메인 페이지</span></p></body></html>"))
        self.TestButton.setText(_translate("Dialog", "test page"))
        self.Loginbutton.setText(_translate("Dialog", "login page"))


def StartTempMain():
    global mywindow
    mywindow = temp_main()
    mywindow.show()

