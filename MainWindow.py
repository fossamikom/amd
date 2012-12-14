# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowBack.ui'
#
# Created: Thu Dec 13 20:47:15 2012
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
      	MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setGeometry(300, 200, 640, 530)
	MainWindow.setMinimumSize(QtCore.QSize(640, 530))
        MainWindow.setMaximumSize(QtCore.QSize(640, 530))
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(_fromUtf8("pic/logoApp.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_download = QtGui.QPushButton(self.centralwidget)
        self.btn_download.setGeometry(QtCore.QRect(440, 410, 98, 27))
        self.btn_download.setObjectName(_fromUtf8("btn_download"))
	
	self.btn_option = QtGui.QPushButton(self.centralwidget)
        self.btn_option.setGeometry(QtCore.QRect(285, 10, 98, 27))
        self.btn_option.setObjectName(_fromUtf8("btn_option"))

	self.btn_about = QtGui.QPushButton(self.centralwidget)
        self.btn_about.setGeometry(QtCore.QRect(285, 40, 98, 27))
        self.btn_about.setObjectName(_fromUtf8("btn_about"))
	
	self.btn_exit = QtGui.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(285, 70, 98, 27))
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))

        self.prog = QtGui.QProgressBar(self.centralwidget)
        self.prog.setGeometry(QtCore.QRect(30, 460, 581, 23))
        self.prog.setProperty("value", 0)
        self.prog.setObjectName(_fromUtf8("prog"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 110, 641, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(310, 130, 20, 311))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 440, 641, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 95))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.user = QtGui.QLineEdit(self.layoutWidget)
        self.user.setObjectName(_fromUtf8("user"))
        self.gridLayout.addWidget(self.user, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pswd = QtGui.QLineEdit(self.layoutWidget)
        self.pswd.setEchoMode(QtGui.QLineEdit.Password)
        self.pswd.setObjectName(_fromUtf8("pswd"))
        self.gridLayout.addWidget(self.pswd, 1, 1, 1, 1)
        self.btn_login = QtGui.QPushButton(self.layoutWidget)
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
        self.gridLayout.addWidget(self.btn_login, 2, 1, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 140, 258, 261))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.list_dosen = QtGui.QListWidget(self.layoutWidget1)
        self.list_dosen.setObjectName(_fromUtf8("list_dosen"))
        self.verticalLayout.addWidget(self.list_dosen)
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(370, 140, 258, 261))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 10, 221, 101))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("pic/splash.png")))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_4 = QtGui.QLabel(self.layoutWidget2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.list_materi = QtGui.QListWidget(self.layoutWidget2)
        self.list_materi.setObjectName(_fromUtf8("list_materi"))
        self.verticalLayout_2.addWidget(self.list_materi)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))

	# Splash Screen
        splash_pic=QtGui.QPixmap('pic/splash.png')
        self.splash=QtGui.QSplashScreen(splash_pic)
        self.splash.show()
	time.sleep(5)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "AMD-Amikom Materi Downloader", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_download.setText(QtGui.QApplication.translate("MainWindow", "Download", None, QtGui.QApplication.UnicodeUTF8))
	self.btn_option.setText(QtGui.QApplication.translate("MainWindow", "Option", None, QtGui.QApplication.UnicodeUTF8))
	self.btn_about.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
	self.btn_exit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_login.setText(QtGui.QApplication.translate("MainWindow", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Dosen", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Materi", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

