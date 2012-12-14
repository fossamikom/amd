# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OptionWindow.ui'
#
# Created: Thu Dec 13 01:30:55 2012
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setFixedSize(388, 251)
	Dialog.setGeometry(450, 300, 388, 251)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 50, 161, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.oke = QtGui.QPushButton(Dialog)
        self.oke.setGeometry(QtCore.QRect(150, 190, 98, 27))
        self.oke.setObjectName(_fromUtf8("oke"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 110, 331, 29))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.path = QtGui.QLineEdit(self.widget)
        self.path.setObjectName(_fromUtf8("path"))
        self.horizontalLayout.addWidget(self.path)
        self.select = QtGui.QPushButton(self.widget)
        self.select.setObjectName(_fromUtf8("select"))
        self.horizontalLayout.addWidget(self.select)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Select Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Select Download Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.oke.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.select.setText(QtGui.QApplication.translate("Dialog", "select", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

