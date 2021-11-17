import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import LoginPage
import DBconnect

class Register_Page(QtWidgets.QMainWindow):
    def __init__(self):
        self.Duplicatedcheck = 0    #중복확인 실행 여부
        self.PWD_Check = 0          #비밀번호 일치 여부
        self.sex = 2                #성별 2:선택안함  1:남 0:여
        self.usertype = 2           #유저타입  2:선택안함 1:구매자 0:판매자

        super().__init__()
        self.setupUi(self)

        #취소버튼을 누르면 로그인 화면으로 돌아감
        self.Cancle_Button.clicked.connect(self.CancleButtonClicked)

        #중복확인 버튼 클릭시 중복확인
        self.DuplicateButton.clicked.connect(self.DuplicateButtonClicked)

        #아이디 값이 변경될때마다 중복확인을 다시 요구
        self.ID_input.textChanged.connect(self.DuplicateReset)

        #pwd 입력값이 변경될 때 마다 두 값이 같은지 확인
        self.PWD_input.textChanged.connect(self.PWD_same_check)
        self.PWD_check_input.textChanged.connect(self.PWD_same_check)

        #성별 변경
        self.Male_radioButton.clicked.connect(self.Set_sex_male)
        self.Female_radioButton.clicked.connect(self.Set_sex_female)

        #유저타입 변경
        self.Customer_radioButton.clicked.connect(self.Set_user_Customer)
        self.Seller_radioButton.clicked.connect(self.Set_user_Seller)

        #Regitser버튼 클릭
        self.Register_button.clicked.connect(self.RegiserButtonClicked)


    #성별 변경 함수
    def Set_sex_male(self):
        self.sex = 1
        print(self.sex)
    def Set_sex_female(self):
        self.sex = 0
        print(self.sex)

    #유저타입 변경 함수
    def Set_user_Customer(self):
        self.usertype = 1
        print(self.usertype)
    def Set_user_Seller(self):
        self.usertype = 0
        print(self.usertype)

    def PWD_same_check(self):
        if self.PWD_input.text() == self.PWD_check_input.text():
            self.PWD_Check = 1
        else:
            self.PWD_Check = 0
        print(self.PWD_Check)

    #아이디 칸의 값이 변경될 경우 다시 중복확인 요구
    def DuplicateReset(self):
        self.Duplicatedcheck = 0
        print(self.Duplicatedcheck)

    #cancle 버튼을 누를 경우 창을 닫고 다시 로그인화면으로 이동
    def CancleButtonClicked(self):
        LoginPage.startLoginPage()
        self.close()

    #중복체크버튼을 누를 경우 중복체크를 하고
    #중복이 없을 경우에만 Duplicatedcheck를 1로 설정
    #이후 Register버튼을 눌렀을때 Duplicatedcheck가 1인지 확인
    def DuplicateButtonClicked(self):
        id = self.ID_input.text()
        self.Duplicatedcheck =  DBconnect.IdDuplicateCheck(id)
        print(self.Duplicatedcheck)


    #Regiser버튼 클릭시 호출
    #추후에 DB와 연결 예정
    def RegiserButtonClicked(self):
        #임시 입력 확인
        print("user type: ",self.usertype)
        print("sex: ", self.sex)
        print("user id:", self.ID_input.text())
        print("id duplicate check: ", self.Duplicatedcheck)
        print("pwd: ", self.PWD_input.text())
        print("PWD same check: ", self.PWD_Check)
        print("name: ", self.name_input.text())
        print("birth: ", self.brth_input.text())
        print("phone: ", self.phone_input.text())
        now = time.localtime()
        print("Registertime: "+"%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday))



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(675, 521)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 90, 281, 80))
        self.groupBox.setObjectName("groupBox")
        self.Customer_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.Customer_radioButton.setGeometry(QtCore.QRect(10, 40, 100, 20))
        self.Customer_radioButton.setObjectName("Customer_radioButton")
        self.Seller_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.Seller_radioButton.setGeometry(QtCore.QRect(140, 40, 100, 20))
        self.Seller_radioButton.setObjectName("Seller_radioButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 20, 281, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 200, 60, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 270, 60, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(340, 200, 60, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(350, 90, 281, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.Male_radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.Male_radioButton.setGeometry(QtCore.QRect(10, 40, 100, 20))
        self.Male_radioButton.setObjectName("Male_radioButton")
        self.Female_radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.Female_radioButton.setGeometry(QtCore.QRect(140, 39, 100, 21))
        self.Female_radioButton.setObjectName("Female_radioButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 330, 81, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(340, 270, 60, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(340, 330, 60, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.ID_input = QtWidgets.QLineEdit(Dialog)
        self.ID_input.setGeometry(QtCore.QRect(130, 200, 113, 21))
        self.ID_input.setObjectName("ID_input")
        self.PWD_check_input = QtWidgets.QLineEdit(Dialog)
        self.PWD_check_input.setGeometry(QtCore.QRect(130, 330, 113, 21))
        self.PWD_check_input.setObjectName("PWD_check_input")
        self.PWD_input = QtWidgets.QLineEdit(Dialog)
        self.PWD_input.setGeometry(QtCore.QRect(130, 270, 113, 21))
        self.PWD_input.setObjectName("PWD_input")
        self.name_input = QtWidgets.QLineEdit(Dialog)
        self.name_input.setGeometry(QtCore.QRect(460, 200, 113, 21))
        self.name_input.setObjectName("name_input")
        self.brth_input = QtWidgets.QLineEdit(Dialog)
        self.brth_input.setGeometry(QtCore.QRect(460, 270, 113, 21))
        self.brth_input.setPlaceholderText("yyyy-mm-dd")
        self.brth_input.setObjectName("brth_input")
        self.phone_input = QtWidgets.QLineEdit(Dialog)
        self.phone_input.setGeometry(QtCore.QRect(460, 330, 113, 21))
        self.phone_input.setPlaceholderText("010-0000-0000")
        self.phone_input.setObjectName("phone_input")
        self.DuplicateButton = QtWidgets.QPushButton(Dialog)
        self.DuplicateButton.setGeometry(QtCore.QRect(128, 220, 121, 32))
        self.DuplicateButton.setObjectName("DuplicateButton")
        self.Register_button = QtWidgets.QPushButton(Dialog)
        self.Register_button.setGeometry(QtCore.QRect(200, 420, 113, 32))
        self.Register_button.setObjectName("Register_button")
        self.Cancle_Button = QtWidgets.QPushButton(Dialog)
        self.Cancle_Button.setGeometry(QtCore.QRect(370, 420, 113, 32))
        self.Cancle_Button.setObjectName("Cancle_Button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "user type"))
        self.Customer_radioButton.setText(_translate("Dialog", "Customer"))
        self.Seller_radioButton.setText(_translate("Dialog", "Seller"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:48pt;\">Register Page</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "ID"))
        self.label_3.setText(_translate("Dialog", "PWD"))
        self.label_4.setText(_translate("Dialog", "name"))
        self.groupBox_2.setTitle(_translate("Dialog", "Sex"))
        self.Male_radioButton.setText(_translate("Dialog", "Male"))
        self.Female_radioButton.setText(_translate("Dialog", "Female"))
        self.label_5.setText(_translate("Dialog", "PWD_check"))
        self.label_6.setText(_translate("Dialog", "brth"))
        self.label_7.setText(_translate("Dialog", "phone"))
        self.DuplicateButton.setText(_translate("Dialog", "duplicate check"))
        self.Register_button.setText(_translate("Dialog", "Register"))
        self.Cancle_Button.setText(_translate("Dialog", "Cancle"))


def StartRegister():
    global mywindow
    mywindow = Register_Page()
    mywindow.show()