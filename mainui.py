# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import resource_sheet
import webbrowser
import ctypes
import sys
import os


def admin_checks():
    try:
        adminState = os.getuid() == 0
    except AttributeError:
        adminState = ctypes.windll.shell32.IsUserAnAdmin() != 0

    return adminState


class Ui_DCK_MainWin(object):
    def setupUi(self, DCK_MainWin):
        DCK_MainWin.setObjectName("DCK_MainWin")
        DCK_MainWin.resize(200, 254)
        DCK_MainWin.setMinimumSize(QtCore.QSize(200, 254))
        DCK_MainWin.setMaximumSize(QtCore.QSize(200, 254))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/DNS Cache Killer/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DCK_MainWin.setWindowIcon(icon)
        DCK_MainWin.setStyleSheet("background-color: rgb(56, 70, 89);")
        self.centralwidget = QtWidgets.QWidget(DCK_MainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.titleText = QtWidgets.QLabel(self.centralwidget)
        self.titleText.setGeometry(QtCore.QRect(0, 0, 201, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.titleText.setFont(font)
        self.titleText.setStyleSheet("background-color: rgb(45, 169, 163);")
        self.titleText.setObjectName("titleText")
        self.subText = QtWidgets.QLabel(self.centralwidget)
        self.subText.setGeometry(QtCore.QRect(0, 120, 201, 31))
        self.subText.setObjectName("subText")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(10, 160, 181, 23))
        self.clearButton.setStyleSheet("background-color: none;")
        self.clearButton.setObjectName("clearButton")
        self.visitButton = QtWidgets.QPushButton(self.centralwidget)
        self.visitButton.setGeometry(QtCore.QRect(10, 190, 181, 23))
        self.visitButton.setStyleSheet("background-color: none;")
        self.visitButton.setObjectName("visitButton")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(10, 220, 181, 23))
        self.closeButton.setStyleSheet("background-color: none;")
        self.closeButton.setObjectName("closeButton")
        DCK_MainWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(DCK_MainWin)
        QtCore.QMetaObject.connectSlotsByName(DCK_MainWin)

    def retranslateUi(self, DCK_MainWin):
        _translate = QtCore.QCoreApplication.translate
        DCK_MainWin.setWindowTitle(_translate("DCK_MainWin", "DCK"))
        self.titleText.setText(_translate("DCK_MainWin", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#000000;\">DNS Cache <br/></span><span style=\" font-size:28pt; font-weight:600; color:#000000;\">Killer</span></p></body></html>"))
        self.subText.setText(_translate("DCK_MainWin", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">A program which quickly<br/>clears your DNS Cache</span></p></body></html>"))
        self.clearButton.setText(_translate("DCK_MainWin", "Clear DNS"))
        self.visitButton.setText(_translate("DCK_MainWin", "Visit GitHub"))
        self.closeButton.setText(_translate("DCK_MainWin", "Close Program"))


class Logic(QtWidgets.QMainWindow, Ui_DCK_MainWin):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        admin = admin_checks()

        if admin:
            pass
        else:
            def closethis():
                sys.exit()

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/images/DNS Cache Killer/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg.setWindowIcon(icon)

            msg.setText("DCK Error")
            msg.setInformativeText("Please run the application with administrator privileges, or this will not work.")
            msg.setWindowTitle("DCK Error")
            # msg.setWindowIcon(QtWidgets.QMessageBox.Critical)
            msg.setDetailedText(
                "Please note:\n\nThis program needs administrative rights in order to run the necessary commands.")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            msg.buttonClicked.connect(closethis)

            retval = msg.exec_()
            print("value of pressed message box button:", retval)

            sys.exit()

        self.setupUi(self)
        self.show()

        self.clearButton.clicked.connect(self.clearCache)
        self.visitButton.clicked.connect(self.visitSite)
        self.closeButton.clicked.connect(self.closeProgram)

    def clearCache(self):
        print(" [+] Clearing DNS cache")

        def closethis():
            sys.exit()

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/DNS Cache Killer/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)

        msg.setText("DCK Success")
        msg.setInformativeText("Cleared your DNS Cache.")
        msg.setWindowTitle("DNS Cleared")
        # msg.setWindowIcon(QtWidgets.QMessageBox.Critical)
        msg.setDetailedText(
            "See your DNS entries below: \n\n{} \n\n [+] Cleared".format(os.popen("ipconfig /displaydns").read()))
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.buttonClicked.connect(closethis)

        os.system("ipconfig /flushdns")

        retval = msg.exec_()
        print("value of pressed message box button:", retval)

        sys.exit()


    def visitSite(self):
        print(" [+] Visiting website")
        webbrowser.open("https://github.com/Elliot-Potts/DNS-Cache-Killer")

    def closeProgram(self):
        print(" [+] Closing program")
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    DCK_MainWin = QtWidgets.QMainWindow()
    ui = Logic()
    sys.exit(app.exec_())

