# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutWindow.ui'
#
# Created: Thu Dec 13 08:22:01 2012
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName(_fromUtf8("aboutDialog"))
        aboutDialog.resize(521, 363)
	aboutDialog.setGeometry(350, 250, 521, 363)
        aboutDialog.setMinimumSize(QtCore.QSize(521, 363))
        aboutDialog.setMaximumSize(QtCore.QSize(521, 363))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pic/logoApp.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutDialog.setWindowIcon(icon)
        self.tabs = QtGui.QTabWidget(aboutDialog)
        self.tabs.setGeometry(QtCore.QRect(10, 60, 501, 271))
        self.tabs.setMinimumSize(QtCore.QSize(501, 271))
        self.tabs.setMaximumSize(QtCore.QSize(501, 271))
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.description = QtGui.QLabel(self.tab)
        self.description.setGeometry(QtCore.QRect(0, 10, 490, 201))
        self.description.setMinimumSize(QtCore.QSize(490, 201))
        self.description.setMaximumSize(QtCore.QSize(471, 201))
        self.description.setTextFormat(QtCore.Qt.AutoText)
        self.description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description.setObjectName(_fromUtf8("description"))
        self.tabs.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.authors = QtGui.QTextBrowser(self.tab_3)
        self.authors.setGeometry(QtCore.QRect(7, 6, 481, 211))
        self.authors.setObjectName(_fromUtf8("authors"))
        self.tabs.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.license = QtGui.QLabel(self.tab_2)
        self.license.setGeometry(QtCore.QRect(10, 10, 464, 201))
        self.license.setObjectName(_fromUtf8("license"))
        self.tabs.addTab(self.tab_2, _fromUtf8(""))
        self.cancelButton = QtGui.QPushButton(aboutDialog)
        self.cancelButton.setGeometry(QtCore.QRect(410, 330, 94, 30))
        self.cancelButton.setMinimumSize(QtCore.QSize(94, 30))
        self.cancelButton.setMaximumSize(QtCore.QSize(94, 30))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.logoText = QtGui.QLabel(aboutDialog)
        self.logoText.setGeometry(QtCore.QRect(90, 10, 421, 41))
        self.logoText.setMinimumSize(QtCore.QSize(421, 41))
        self.logoText.setMaximumSize(QtCore.QSize(421, 41))
        self.logoText.setObjectName(_fromUtf8("logoText"))
        self.logoImage = QtGui.QLabel(aboutDialog)
        self.logoImage.setGeometry(QtCore.QRect(10, 0, 81, 61))
        self.logoImage.setMinimumSize(QtCore.QSize(81, 61))
        self.logoImage.setMaximumSize(QtCore.QSize(81, 61))
        self.logoImage.setText(_fromUtf8(""))
        self.logoImage.setPixmap(QtGui.QPixmap(_fromUtf8("pic/logoApp.png")))
        self.logoImage.setObjectName(_fromUtf8("logoImage"))

        self.retranslateUi(aboutDialog)
        self.tabs.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        aboutDialog.setWindowTitle(QtGui.QApplication.translate("aboutDialog", "About AMD", None, QtGui.QApplication.UnicodeUTF8))
        self.description.setText(QtGui.QApplication.translate("aboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt;\">Software ini digunakan untuk mendowload materi yang ada di Elearning</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt;\">Amikom, kamu bisa download materi dari aplikasi ini langsung,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt;\">dengan form login yang ada di dalamnya anda sudah terintegrasi sebagai</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt;\">mahasiswa amikom,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt;\">    1. isi Login Form<br />    2. Setting Destination Folder<br />    3. klik login, dan ikuti sesuai feeling kamu :D</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt;\">@rizqonsadida, 2012</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), QtGui.QApplication.translate("aboutDialog", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.authors.setHtml(QtGui.QApplication.translate("aboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt;\">Crew:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt;\">Rizqon Sadida (@rizqonsadida) as Programmer</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt;\">Rangga SeptyoWijaya (@ranggaseptyo) as Design Artist</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt;\">thank\'s to:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt;\">Robbyn Rahmandaru (@robzlabz) yang uda nyumbang ide. :D</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt;\">Rian Eka Putra (@rianekaputra) kamarnya gue pake bua lembur, :D</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt;\">Ghozi Fadli (@ghost21) yang uda nraktir pizza, (jadi tambah semangat) :D</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt;\">Herman (@hermansiregar) yang dari kemaren gue rusuhin terus :D<br />All member of FOSSIL AMIKOM, :D</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt;\">dan semuanya yang uda support, sampai aplikasi ini selesai :D </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_3), QtGui.QApplication.translate("aboutDialog", "Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.license.setText(QtGui.QApplication.translate("aboutDialog", "<html><head/><body><p>Software ini buatan Mahasiswa Amikom <br/>Berbasis Open Source dan dapat di gunakan Gratis<br/><br/><br/><br/>Haahahahahahahaha</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), QtGui.QApplication.translate("aboutDialog", "License", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("aboutDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.logoText.setText(QtGui.QApplication.translate("aboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:36pt; font-weight:600; vertical-align:super;\">AMD-</span><span style=\" font-family:\'Arial\'; font-size:20pt; vertical-align:super;\">AMIKOM MATERI DOWNLOADER</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    aboutDialog = QtGui.QDialog()
    ui = Ui_aboutDialog()
    ui.setupUi(aboutDialog)
    aboutDialog.show()
    sys.exit(app.exec_())

