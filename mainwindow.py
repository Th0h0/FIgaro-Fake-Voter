# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets

#Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#####
import time
import random
import os
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 677)
        MainWindow.setMinimumSize(QtCore.QSize(1052, 677))
        MainWindow.setMaximumSize(QtCore.QSize(1052, 677))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("background-color: rgb(90, 90, 90);")
        MainWindow.setDocumentMode(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 1139, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.URL = QtWidgets.QLineEdit(self.centralWidget)
        self.URL.setGeometry(QtCore.QRect(10, 110, 831, 81))
        self.URL.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.URL.setObjectName("URL")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(-10, 310, 1181, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Slider = QtWidgets.QSlider(self.centralWidget)
        self.Slider.setGeometry(QtCore.QRect(250, 350, 160, 22))
        self.Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Slider.setObjectName("Slider")
        self.voteToSend = QtWidgets.QLCDNumber(self.centralWidget)
        self.voteToSend.setGeometry(QtCore.QRect(430, 350, 64, 23))
        self.voteToSend.setObjectName("voteToSend")
        self.proxies = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.proxies.setGeometry(QtCore.QRect(700, 380, 271, 101))
        self.proxies.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.proxies.setObjectName("proxies")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(750, 340, 221, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(130, 250, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(60, 230, 61, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/images/icons8-true-false-64.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(700, 320, 41, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/images/icons8-page-40.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(110, 20, 301, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/images/rsz_1280px-le_figaro_logosvg.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(30, 340, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 500, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(184, 102, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(270, 490, 91, 81))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/images/icons8-rocket-96.png"))
        self.label_7.setObjectName("label_7")
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(350, 600, 301, 31))
        self.progressBar.setStyleSheet("color: rgb(184, 102, 255);")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(240, 600, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(670, 600, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.voteNumber = QtWidgets.QLabel(self.centralWidget)
        self.voteNumber.setGeometry(QtCore.QRect(720, 600, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.voteNumber.setFont(font)
        self.voteNumber.setStyleSheet("color: rgb(255, 255, 255);")
        self.voteNumber.setObjectName("voteNumber")
        self.buttonYes = QtWidgets.QPushButton(self.centralWidget)
        self.buttonYes.setGeometry(QtCore.QRect(310, 250, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonYes.setFont(font)
        self.buttonYes.setObjectName("buttonYes")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 250, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1052, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #   My Changes #
        self.buttonYes.setCheckable(True)
        self.pushButton_3.setCheckable(True)
        self.Slider.setMaximum(5000)
        self.Slider.valueChanged.connect(self.voteToSend.display)
        self.progressBar.setValue(0) #Reset progressBar value since nothing started yet
        self.pushButton.clicked.connect(self.FakeVoting) #When user clicks -> FakeVoting function is launched
        # End Of My Changes#

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Figaro Fake Voter"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#ffffff;\"> SURVEY FAKER</span></p></body></html>"))
        self.URL.setText(_translate("MainWindow", "Figaro\'s Survey URL"))
        self.label.setText(_translate("MainWindow", "Paste your proxies here :"))
        self.label_2.setText(_translate("MainWindow", "Vote Choice :"))
        self.label_6.setText(_translate("MainWindow", "Fake votes to submit"))
        self.pushButton.setText(_translate("MainWindow", "Launch Votes ! "))
        self.label_8.setText(_translate("MainWindow", "Voting Progress :"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>Votes :<span style=\" font-weight:600;\"/></p></body></html>"))
        self.voteNumber.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">0</span></p></body></html>"))
        self.buttonYes.setText(_translate("MainWindow", "Yes"))
        self.pushButton_3.setText(_translate("MainWindow", "No"))

    def FakeVoting(self):

        try:
            os.remove("temporary_file.txt")
        except:
            print("Program Launching")
        total_proxy = self.proxies.toPlainText()
        file_name = 'temporary_file.txt'
        f = open(file_name, 'a+')
        f.write(str(total_proxy))
        f.close()
        f = open("temporary_file.txt","r")
        url = self.URL.text()
        voteNumber = self.voteToSend.intValue()
        voteLaunched = 0
        chrome_options = webdriver.ChromeOptions()
        chromedriver = "chromedriver.exe"
        #chrome_options.add_argument('headless')
        while voteLaunched < voteNumber:
            f.close()
            f = open("temporary_file.txt","r")
            proxy = random.choice(list(f))
            chrome_options.add_argument('--proxy-server=http://%s'%proxy)
            driver = webdriver.Chrome(executable_path=os.path.abspath(chromedriver), options=chrome_options)
            driver.get(str(url))
            while driver.current_url != str(url):
                time.sleep(0.5)
            if self.buttonYes.pressed:
                try:
                    driver.find_element_by_xpath('//*[@id="fig-page"]/div/div[1]/div[1]/article/div[2]/form/label[1]').click()
                    time.sleep(2)
                except:
                    print("L'URL entré est invalide, le programme va fermer ... ")
            if self.pushButton_3.pressed:
                try:
                    driver.find_element_by_xpath('//*[@id="fig-page"]/div/div[1]/div[1]/article/div[2]/form/label[2]').click()
                    time.sleep(2)
                except:
                    print("L'URL entré est invalide, le programme va fermer ... ")
            voteLaunched += 1
            self.progressBar.setValue(voteLaunched/voteNumber*100)
            self.voteNumber.setNum(voteLaunched)
            driver.close()
        
            
        

import resource

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

