# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DCK_MainWin(object):
    def setupUi(self, DCK_MainWin):
        DCK_MainWin.setObjectName("DCK_MainWin")
        DCK_MainWin.resize(200, 254)
        DCK_MainWin.setMinimumSize(QtCore.QSize(200, 254))
        DCK_MainWin.setMaximumSize(QtCore.QSize(200, 254))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DCK_MainWin = QtWidgets.QMainWindow()
    ui = Ui_DCK_MainWin()
    ui.setupUi(DCK_MainWin)
    DCK_MainWin.show()
    sys.exit(app.exec_())

