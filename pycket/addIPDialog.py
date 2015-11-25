# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addIPDialog.ui'
#
# Created: Tue Nov 24 16:01:41 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(300, 147)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.verticalLayout_1 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_1.setObjectName(_fromUtf8("verticalLayout_1"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_ip = QtGui.QWidget()
        self.tab_ip.setObjectName(_fromUtf8("tab_ip"))
        self.gridLayout_1 = QtGui.QGridLayout(self.tab_ip)
        self.gridLayout_1.setObjectName(_fromUtf8("gridLayout_1"))
        self.formLayout_1 = QtGui.QFormLayout()
        self.formLayout_1.setObjectName(_fromUtf8("formLayout_1"))
        self.label_ip = QtGui.QLabel(self.tab_ip)
        self.label_ip.setObjectName(_fromUtf8("label_ip"))
        self.formLayout_1.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_ip)
        self.line_edit_add_ip = QtGui.QLineEdit(self.tab_ip)
        self.line_edit_add_ip.setText(_fromUtf8(""))
        self.line_edit_add_ip.setMaxLength(15)
        self.line_edit_add_ip.setObjectName(_fromUtf8("line_edit_add_ip"))
        self.formLayout_1.setWidget(0, QtGui.QFormLayout.FieldRole, self.line_edit_add_ip)
        self.gridLayout_1.addLayout(self.formLayout_1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_ip, _fromUtf8(""))
        self.tab_multiple = QtGui.QWidget()
        self.tab_multiple.setObjectName(_fromUtf8("tab_multiple"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_multiple)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_multiple_ip = QtGui.QLabel(self.tab_multiple)
        self.label_multiple_ip.setObjectName(_fromUtf8("label_multiple_ip"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_multiple_ip)
        self.text_edit_add_ip = QtGui.QTextEdit(self.tab_multiple)
        self.text_edit_add_ip.setText(_fromUtf8(""))
        self.text_edit_add_ip.setObjectName(_fromUtf8("text_edit_add_ip"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_edit_add_ip)
        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_multiple, _fromUtf8(""))
        self.verticalLayout_1.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_1.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Add IP to watch", None))
        self.label_ip.setText(_translate("Dialog", "IP Address", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ip), _translate("Dialog", "IP", None))
        self.label_multiple_ip.setText(_translate("Dialog", "IP Addresses", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_multiple), _translate("Dialog", "Multiple IPs", None))

