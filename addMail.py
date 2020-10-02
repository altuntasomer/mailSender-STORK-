import sys
from PyQt5 import QtCore, QtGui, QtWidgets

senderMailAddresses = list()
senderPasswords = list()
receiverNames = list()
receiverMailAddresses = list()
senderIndex = 0
receiverIndex = 0
smtpp = ["@yandex","@gmail","@outlook;@hotmail;@msn;.edu"]#
smtps = ["smtp.yandex.com","smtp.gmail.com","smtp.office365.com"]
#----------------------------------------------------------------------------------------------------------------------#
language = 0
sender_text_lan = ["Gönderici","Sender"]
receiver_text_lan = ["Alıcı","Receiver"]
pushbutton_add_text_lan = ["Kaydet (F8)","Save (F8)"]
entersender_text_lan = ["Gönderici Mail Adresi Giriniz","Enter the Sender Mail Address"]
entersenderpass_text_lan = ["Şifrenizi Giriniz","Enter the Password"]
enterreceiver_text_lan = ["Alıcı Mail Adresi Giriniz","Enter the Receiver Mail Address"]
enterreceivername_text_lan = ["Alıcı İsmi Giriniz","Enter the Receiver Name"]
incorrectmail_text_lan = ["Geçersiz Mail Adresi","Incorrect Mail Address"]
savesuccessfully_text_lan = ["Başarıyla Kaydedildi","Saved Successfully"]



#----------------------------------------------------------------------------------------------------------------------#
# Save mail addresses to File
def writeToFile(type,txt1,txt2):
    if type == 's':
        file = open("senderMailAddress.txt","a")
        file.write(txt1+";"+txt2+";\n")
        file.close()
    if type == 'r':
        file = open("receiverMailAddress.txt", "a")
        file.write(txt1 + ";" + txt2+";\n")
        file.close()
#----------------------------------------------------------------------------------------------------------------------#
# Read From File to mail adress list and password list or name list
def readFromFile():
    try:
        senderMailAddresses.clear()
        receiverMailAddresses.clear()
        file = open("senderMailAddress.txt", "r")

        temp = file.readlines()
        file.close()
        for i in temp:
            senderMailAddresses.append(i.split(";")[0])
            senderPasswords.append(i.split(";")[1])

        file = open("receiverMailAddress.txt", "r")
        temp = file.readlines()
        file.close()
        for i in temp:
            receiverMailAddresses.append(i.split(";")[0])
            receiverNames.append(i.split(";")[1])
    except Exception as a:
        pass
#----------------------------------------------------------------------------------------------------------------------#


class Ui_MainWindow_addmailadress(object):
    def setupUi(self, MainWindow_addmailadress):
        MainWindow_addmailadress.setObjectName("MainWindow_addmailadress")
        MainWindow_addmailadress.resize(591, 478)
        self.centralwidget = QtWidgets.QWidget(MainWindow_addmailadress)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.radioButton_sender = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_sender.setFont(font)
        self.radioButton_sender.setChecked(True)
        self.radioButton_sender.setObjectName("radioButton_sender")
        self.verticalLayout.addWidget(self.radioButton_sender)
        self.radioButton_Receiver = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_Receiver.setFont(font)
        self.radioButton_Receiver.setObjectName("radioButton_Receiver")
        self.verticalLayout.addWidget(self.radioButton_Receiver)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.verticalLayout.addWidget(self.lineEdit_1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow_addmailadress.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_addmailadress)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 591, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_addmailadress.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_addmailadress)
        self.statusbar.setObjectName("statusbar")
        MainWindow_addmailadress.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_addmailadress)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_addmailadress)

        self.radioButton_sender.toggled.connect(self.toggled)
        self.radioButton_Receiver.toggled.connect(self.toggled2)
        self.pushButton.clicked.connect(self.save)

        self.pushButton.setShortcut('F8')


    def retranslateUi(self, MainWindow_addmailadress):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_addmailadress.setWindowTitle(_translate("MainWindow_addmailadress", "Stork 1.0.0   SimpleAppsInc"))
        self.radioButton_sender.setText(_translate("MainWindow_addmailadress", sender_text_lan[language]))
        self.radioButton_Receiver.setText(_translate("MainWindow_addmailadress", receiver_text_lan[language]))
        self.label_1.setText(_translate("MainWindow_addmailadress", entersender_text_lan[language]))
        self.label_2.setText(_translate("MainWindow_addmailadress", entersenderpass_text_lan[language]))
        self.pushButton.setText(_translate("MainWindow_addmailadress", pushbutton_add_text_lan[language]))

        # ----------------------------------------------------------------------------------------------------------------------#
        # Saving the mail addresses and passwords or names to file


    def save(self):
        try:
            address = self.lineEdit_1.text()

            if not '@' in address:
                self.pushButton.setText(incorrectmail_text_lan[language])
                return
            if len(address) < 5:
                self.pushButton.setText()(incorrectmail_text_lan[language])
                return

            if self.radioButton_sender.isChecked():

                password = self.lineEdit_2.text()
                writeToFile('s', address, password)

            else:

                name = self.lineEdit_2.text()
                writeToFile('r', address, name)
            self.pushButton.setText(savesuccessfully_text_lan[language])

        except Exception as aaa:
            pass
        # ----------------------------------------------------------------------------------------------------------------------#
        # When Selected the radiobuttons


    def toggled(self):
        self.label_1.setText(entersender_text_lan[language])
        self.label_2.setText(entersenderpass_text_lan[language])
        self.lineEdit_2.EchoMode(QtWidgets.QLineEdit.Password)


    def toggled2(self):
        self.label_1.setText(enterreceiver_text_lan[language])
        self.label_2.setText(enterreceivername_text_lan[language])
        self.lineEdit_2.EchoMode(QtWidgets.QLineEdit.NoEcho)


    # ----------------------------------------------------------------------------------------------------------------------#
    def loginControl(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_addmailadress = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_addmailadress()
    ui.setupUi(MainWindow_addmailadress)
    MainWindow_addmailadress.show()
    sys.exit(app.exec_())