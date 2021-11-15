from PyQt5 import QtCore, QtGui, QtWidgets

class sampleWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(535, 409)
        self.button_A = QtWidgets.QPushButton(Dialog)
        self.button_A.setGeometry(QtCore.QRect(200, 180, 113, 32))
        self.button_A.setObjectName("button_A")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.button_A.setText(_translate("Dialog", "button A"))

        

def StartSamplePage():
    global mywindow
    mywindow = sampleWin()
    mywindow.show()