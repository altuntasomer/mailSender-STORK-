from PyQt5 import QtCore, QtGui, QtWidgets
import addMail
from smtplib import SMTP
import time
#import tkinter.filedialog
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
msg = MIMEMultipart()
filename = None
global_attach = False
nameOfTheApp = "Stork 1.0.0  SimpleAppsInc"
#----------------------------------------------------------------------------------------------------------------------#
languages = [0,1]
language = languages[0]
label2_text_lan = ["Gönderici Mail Adres","Sender Mail Address"]
label_text_lan  = ["Alıcı Mail Adres","Receiver Mail Address"]
lineedit_text_lan = ["Konu:","Subject:"]
textedit_message_text_lan = ["Mesaj:","Message:"]
pushbutton_attach_text_lan = ["Dosya Ekle (F6)","Attach File (F6)"]
pushbutton_send_text_lan = ["Gönder -> (F8)","Send -> (F8)"]
pushbutton_add_text_lan = ["Gönderici / Alıcı Mail Adresi Ekle (F7)","Add Sender / Receiver Mail Address (F7)"]
pushbutton_refresh_text_lan = ["Yenile (F5)","Refresh (F5)"]
sending_text_lan = ["Gönderiliyor","Sending"]
sended_text_lan = ["Gönderildi","Sended"]
attached_text_lan = ["Eklendi","Attached"]
erroroccured_text_lan = ["Bir Hata Oluştu","An Error Occured"]
change_language_text_lan = ["Change Language (F9)","Dil Değiştir (F9)"]
addMail.language = language
#----------------------------------------------------------------------------------------------------------------------#


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(917, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox_chooseSenderMailAddress = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_chooseSenderMailAddress.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_chooseSenderMailAddress.setSizeIncrement(QtCore.QSize(20, 20))
        self.comboBox_chooseSenderMailAddress.setBaseSize(QtCore.QSize(20, 20))
        self.comboBox_chooseSenderMailAddress.setIconSize(QtCore.QSize(24, 24))
        self.comboBox_chooseSenderMailAddress.setObjectName("comboBox_chooseSenderMailAddress")
        self.verticalLayout_2.addWidget(self.comboBox_chooseSenderMailAddress)
        self.comboBox_chooseReceiverMailAddress = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_chooseReceiverMailAddress.setEditable(True)
        self.comboBox_chooseReceiverMailAddress.setObjectName("comboBox_chooseReceiverMailAddress")
        self.verticalLayout_2.addWidget(self.comboBox_chooseReceiverMailAddress)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_language = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_language.setFont(font)
        self.pushButton_language.setObjectName("pushButton_language")
        self.horizontalLayout.addWidget(self.pushButton_language)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_subject = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_subject.setText("")
        self.lineEdit_subject.setObjectName("lineEdit_subject")
        self.horizontalLayout_4.addWidget(self.lineEdit_subject)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit_message = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_message.setObjectName("textEdit_message")
        self.horizontalLayout_2.addWidget(self.textEdit_message)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.pushButton_attach = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_attach.setFont(font)
        self.pushButton_attach.setAutoDefault(True)
        self.pushButton_attach.setObjectName("pushButton_attach")
        self.horizontalLayout_3.addWidget(self.pushButton_attach)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.pushButton_SendButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_SendButton.setFont(font)
        self.pushButton_SendButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_SendButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_SendButton.setAutoFillBackground(False)
        self.pushButton_SendButton.setAutoDefault(True)
        self.pushButton_SendButton.setObjectName("pushButton_SendButton")
        self.horizontalLayout_3.addWidget(self.pushButton_SendButton)
        self.pushButton_AddSenderMail = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_AddSenderMail.setFont(font)
        self.pushButton_AddSenderMail.setAutoDefault(True)
        self.pushButton_AddSenderMail.setObjectName("pushButton_AddSenderMail")
        self.horizontalLayout_3.addWidget(self.pushButton_AddSenderMail)
        self.pushButton_AddReceiverMail = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_AddReceiverMail.setFont(font)
        self.pushButton_AddReceiverMail.setAutoDefault(False)
        self.pushButton_AddReceiverMail.setObjectName("pushButton_AddReceiverMail")
        self.horizontalLayout_3.addWidget(self.pushButton_AddReceiverMail)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setObjectName("label_error")
        self.verticalLayout.addWidget(self.label_error)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 917, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ----------------------------------------------------------------------------------------------------------------------#
        addMail.readFromFile()
        for i in addMail.senderMailAddresses:
            self.comboBox_chooseSenderMailAddress.addItem(i)
        for i in addMail.receiverMailAddresses:
            self.comboBox_chooseReceiverMailAddress.addItem(i)

        self.comboBox_chooseSenderMailAddress.activated[str].connect(self.onSelectedComboBoxSenderMail)
        self.comboBox_chooseReceiverMailAddress.activated[str].connect(self.onSelectedComboBoxReceiverMail)
        self.pushButton_SendButton.clicked.connect(self.send)
        self.pushButton_AddSenderMail.clicked.connect(self.addEmail)
        self.pushButton_AddReceiverMail.clicked.connect(self.refresh)
        self.pushButton_attach.clicked.connect(self.attach)
        self.pushButton_language.clicked.connect(self.change_language)

        self.pushButton_attach.setShortcut("F6")
        self.pushButton_SendButton.setShortcut("F8")
        self.pushButton_AddReceiverMail.setShortcut("F5")
        self.pushButton_AddSenderMail.setShortcut("F7")
        self.pushButton_language.setShortcut("F9")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", nameOfTheApp))
        self.label_2.setText(_translate("MainWindow", label2_text_lan[language]))
        self.label.setText(_translate("MainWindow", label_text_lan[language]))
        self.lineEdit_subject.setPlaceholderText(_translate("MainWindow", lineedit_text_lan[language]))
        self.textEdit_message.setPlaceholderText(_translate("MainWindow", textedit_message_text_lan[language]))
        self.pushButton_attach.setText(_translate("MainWindow", pushbutton_attach_text_lan[language]))
        self.pushButton_SendButton.setText(_translate("MainWindow", pushbutton_send_text_lan[language]))
        self.pushButton_AddSenderMail.setText(_translate("MainWindow", pushbutton_add_text_lan[language]))
        self.pushButton_AddReceiverMail.setText(_translate("MainWindow", pushbutton_refresh_text_lan[language]))
        self.pushButton_language.setText(_translate("MainWindow", change_language_text_lan[language]))
        self.pushButton_attach.setShortcut("F6")
        self.pushButton_SendButton.setShortcut("F8")
        self.pushButton_AddReceiverMail.setShortcut("F5")
        self.pushButton_AddSenderMail.setShortcut("F7")
        self.pushButton_language.setShortcut("F9")
        self.label_error.setText("")

    def onSelectedComboBoxSenderMail(self, mail):
        self.pushButton_SendButton.setText(pushbutton_send_text_lan[language])
        for i in range(0, len(addMail.senderMailAddresses)):
            if addMail.senderMailAddresses[i] == mail:
                addMail.senderIndex = i

    def onSelectedComboBoxReceiverMail(self, mail):
        self.pushButton_SendButton.setText(pushbutton_send_text_lan[language])
        for i in range(0, len(addMail.receiverMailAddresses)):
            if addMail.receiverMailAddresses[i] == mail:
                addMail.receiverIndex = i

    # -----------------------------------------------------------------------------------------------------------------#
    def send(self):
        self.pushButton_SendButton.setText(sending_text_lan[language])
        global global_attach
        ssmtp = None
        try:
            for i in range(len(addMail.smtpp)):
                a = addMail.smtpp[i].split(";")
                for j in a:
                    if j in addMail.senderMailAddresses[addMail.senderIndex]:
                        ssmtp = addMail.smtps[i]
                        break

            msg['From'] = addMail.senderMailAddresses[addMail.senderIndex]
            msg['To'] = self.comboBox_chooseReceiverMailAddress.currentText()
            msg['Subject'] = self.lineEdit_subject.text()
            msg.attach(MIMEText(self.textEdit_message.toPlainText(), 'plain'))
            if global_attach == True:
                global filename

                attachment = open(filename[0], 'rb')

                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= " + filename[0].split("/")[-1])
                msg.attach(part)

            text = msg.as_string()
            mail = SMTP(ssmtp, 587)
            mail.ehlo()

            mail.starttls()
            mail.login(addMail.senderMailAddresses[addMail.senderIndex],
                       addMail.senderPasswords[addMail.senderIndex])
            mail.sendmail(addMail.senderMailAddresses[addMail.senderIndex],
                          self.comboBox_chooseReceiverMailAddress.currentText(), text.encode("utf8"))
            self.pushButton_SendButton.setText(sended_text_lan[language])
            global_attach = False
            mail.quit()
            self.pushButton_attach.setText(pushbutton_attach_text_lan[language])



        except Exception as a:
            self.label_error.setText(str(a))
            self.pushButton_SendButton.setText(erroroccured_text_lan[language])

    def addEmail(self):
        addMail.language = language
        self.window = QtWidgets.QMainWindow()
        self.ui = addMail.Ui_MainWindow_addmailadress()
        self.ui.setupUi(self.window)
        self.window.show()

    def refresh(self):
        addMail.readFromFile()
        self.comboBox_chooseSenderMailAddress.clear()
        self.comboBox_chooseReceiverMailAddress.clear()
        for i in addMail.senderMailAddresses:
            self.comboBox_chooseSenderMailAddress.addItem(i)
        for i in addMail.receiverMailAddresses:
            self.comboBox_chooseReceiverMailAddress.addItem(i)

        self.retranslateUi(MainWindow)

    # -----------------------------------------------------------------------------------------------------------------#
    def attach(self):
        try:
            home_dir = str(Path.home())
            # window = tkinter.Tk()
            global filename, global_attach
            # filename = tkinter.filedialog.askopenfile()
            filename = QtWidgets.QFileDialog.getOpenFileName(caption='Open file', directory=home_dir)
            global_attach = True
            self.pushButton_attach.setText(attached_text_lan[language])
            # window.destroy()
        except Exception as aax:
            self.label_error.setText(str(aax))

    def change_language(self):
        global language

        language += 1
        if language >= len(languages):
            language = 0
        self.retranslateUi(MainWindow)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())