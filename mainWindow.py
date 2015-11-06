# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Fri Nov  6 18:11:05 2015
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
        self.packetsList = QtGui.QTreeWidget(self.centralwidget)
        self.packetsList.setRootIsDecorated(False)
        self.packetsList.setItemsExpandable(True)
        self.packetsList.setAnimated(True)
        self.packetsList.setColumnCount(0)
        self.packetsList.setObjectName(_fromUtf8("packetsList"))
        self.packetsList.header().setVisible(True)
        self.verticalLayout.addWidget(self.packetsList)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(16, 16))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 696, 29))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuCapture = QtGui.QMenu(self.menuBar)
        self.menuCapture.setObjectName(_fromUtf8("menuCapture"))
        MainWindow.setMenuBar(self.menuBar)
        self.startCaptureBtn = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startCaptureBtn.setIcon(icon)
        self.startCaptureBtn.setObjectName(_fromUtf8("startCaptureBtn"))
        self.stopCaptureBtn = QtGui.QAction(MainWindow)
        self.stopCaptureBtn.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("img/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopCaptureBtn.setIcon(icon1)
        self.stopCaptureBtn.setObjectName(_fromUtf8("stopCaptureBtn"))
        self.actionOpen_pcap_file = QtGui.QAction(MainWindow)
        self.actionOpen_pcap_file.setObjectName(_fromUtf8("actionOpen_pcap_file"))
        self.actionSave_as_pcap_file = QtGui.QAction(MainWindow)
        self.actionSave_as_pcap_file.setObjectName(_fromUtf8("actionSave_as_pcap_file"))
        self.exitBtn = QtGui.QAction(MainWindow)
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.startCaptureBtn)
        self.toolBar.addAction(self.stopCaptureBtn)
        self.menuFile.addAction(self.actionOpen_pcap_file)
        self.menuFile.addAction(self.actionSave_as_pcap_file)
        self.menuFile.addAction(self.exitBtn)
        self.menuCapture.addAction(self.startCaptureBtn)
        self.menuCapture.addAction(self.stopCaptureBtn)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuCapture.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pycket", None))
        self.packetsList.setSortingEnabled(True)
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuCapture.setTitle(_translate("MainWindow", "Capture", None))
        self.startCaptureBtn.setText(_translate("MainWindow", "Start capture", None))
        self.startCaptureBtn.setToolTip(_translate("MainWindow", "Start a new capture", None))
        self.stopCaptureBtn.setText(_translate("MainWindow", "Stop capture", None))
        self.stopCaptureBtn.setToolTip(_translate("MainWindow", "Stop current capture", None))
        self.actionOpen_pcap_file.setText(_translate("MainWindow", "Open pcap file", None))
        self.actionSave_as_pcap_file.setText(_translate("MainWindow", "Save as pcap file", None))
        self.exitBtn.setText(_translate("MainWindow", "Exit", None))
        self.exitBtn.setToolTip(_translate("MainWindow", "Exit app", None))

