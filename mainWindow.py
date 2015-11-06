# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Fri Nov  6 15:22:19 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(696, 618)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.startCaptureBtn = QtGui.QPushButton(self.centralwidget)
        self.startCaptureBtn.setObjectName(_fromUtf8("startCaptureBtn"))
        self.horizontalLayout.addWidget(self.startCaptureBtn, QtCore.Qt.AlignLeft)
        self.stopCaptureBtn = QtGui.QPushButton(self.centralwidget)
        self.stopCaptureBtn.setEnabled(False)
        self.stopCaptureBtn.setObjectName(_fromUtf8("stopCaptureBtn"))
        self.horizontalLayout.addWidget(self.stopCaptureBtn, QtCore.Qt.AlignLeft)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.packetsList = QtGui.QTreeWidget(self.centralwidget)
        self.packetsList.setColumnCount(0)
        self.packetsList.setObjectName(_fromUtf8("packetsList"))
        self.packetsList.header().setVisible(True)
        self.verticalLayout.addWidget(self.packetsList)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 696, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pycket", None))
        self.startCaptureBtn.setText(_translate("MainWindow", "Start capture", None))
        self.stopCaptureBtn.setText(_translate("MainWindow", "Stop capture", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

