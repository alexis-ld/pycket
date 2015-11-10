# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Tue Nov 10 14:01:24 2015
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
        MainWindow.resize(666, 649)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.packetsList = QtGui.QTreeWidget(self.centralwidget)
        self.packetsList.setStyleSheet(_fromUtf8("font: 11pt \"Cantarell\";\n"
"selection-background-color: rgb(199, 199, 199);\n"
""))
        self.packetsList.setRootIsDecorated(False)
        self.packetsList.setItemsExpandable(True)
        self.packetsList.setAnimated(True)
        self.packetsList.setColumnCount(5)
        self.packetsList.setObjectName(_fromUtf8("packetsList"))
        self.packetsList.header().setVisible(True)
        self.verticalLayout.addWidget(self.packetsList)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.packetDetail = QtGui.QTabWidget(self.centralwidget)
        self.packetDetail.setMaximumSize(QtCore.QSize(16777215, 250))
        self.packetDetail.setObjectName(_fromUtf8("packetDetail"))
        self.tab_packet = QtGui.QWidget()
        self.tab_packet.setStyleSheet(_fromUtf8("background-color: rgb(52, 52, 52);\n"
"color: rgb(255, 255, 255);"))
        self.tab_packet.setObjectName(_fromUtf8("tab_packet"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_packet)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tab_packet_label = QtGui.QLabel(self.tab_packet)
        self.tab_packet_label.setObjectName(_fromUtf8("tab_packet_label"))
        self.gridLayout_4.addWidget(self.tab_packet_label, 0, 0, 1, 1)
        self.packetDetail.addTab(self.tab_packet, _fromUtf8(""))
        self.tab_eth = QtGui.QWidget()
        self.tab_eth.setObjectName(_fromUtf8("tab_eth"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_eth)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_2 = QtGui.QLabel(self.tab_eth)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.packetDetail.addTab(self.tab_eth, _fromUtf8(""))
        self.gridLayout.addWidget(self.packetDetail, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(16, 16))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 666, 29))
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
        self.packetDetail.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pycket", None))
        self.packetsList.setSortingEnabled(True)
        self.packetsList.headerItem().setText(0, _translate("MainWindow", "Time", None))
        self.packetsList.headerItem().setText(1, _translate("MainWindow", "#", None))
        self.packetsList.headerItem().setText(2, _translate("MainWindow", "Source", None))
        self.packetsList.headerItem().setText(3, _translate("MainWindow", "Destination", None))
        self.packetsList.headerItem().setText(4, _translate("MainWindow", "Protocol", None))
        self.tab_packet_label.setText(_translate("MainWindow", "No packet selected", None))
        self.packetDetail.setTabText(self.packetDetail.indexOf(self.tab_packet), _translate("MainWindow", "Packet", None))
        self.label_2.setText(_translate("MainWindow", "Deuxieme page", None))
        self.packetDetail.setTabText(self.packetDetail.indexOf(self.tab_eth), _translate("MainWindow", "Page", None))
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

