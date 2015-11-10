# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Tue Nov 10 16:55:56 2015
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
        MainWindow.resize(850, 700)
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
        self.packetsList.header().setDefaultSectionSize(150)
        self.packetsList.header().setMinimumSectionSize(150)
        self.verticalLayout.addWidget(self.packetsList)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.packetDetail = QtGui.QTabWidget(self.centralwidget)
        self.packetDetail.setMaximumSize(QtCore.QSize(16777215, 400))
        self.packetDetail.setTabPosition(QtGui.QTabWidget.North)
        self.packetDetail.setTabShape(QtGui.QTabWidget.Rounded)
        self.packetDetail.setObjectName(_fromUtf8("packetDetail"))
        self.tab_packet = QtGui.QWidget()
        self.tab_packet.setStyleSheet(_fromUtf8("background-color: rgb(52, 52, 52);\n"
"color: rgb(255, 255, 255);"))
        self.tab_packet.setObjectName(_fromUtf8("tab_packet"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_packet)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tab_packet_hexdump = QtGui.QTextBrowser(self.tab_packet)
        self.tab_packet_hexdump.setObjectName(_fromUtf8("tab_packet_hexdump"))
        self.gridLayout_4.addWidget(self.tab_packet_hexdump, 0, 0, 1, 1)
        self.packetDetail.addTab(self.tab_packet, _fromUtf8(""))
        self.tab_ethernet = QtGui.QWidget()
        self.tab_ethernet.setObjectName(_fromUtf8("tab_ethernet"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_ethernet)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.tab_ethernet_list = QtGui.QTreeWidget(self.tab_ethernet)
        self.tab_ethernet_list.setStyleSheet(_fromUtf8("font: 11pt \"Cantarell\";\n"
"background-color: rgb(52, 52, 52);\n"
"color: rgb(255, 255, 255);"))
        self.tab_ethernet_list.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tab_ethernet_list.setRootIsDecorated(False)
        self.tab_ethernet_list.setObjectName(_fromUtf8("tab_ethernet_list"))
        self.tab_ethernet_list.header().setVisible(False)
        self.tab_ethernet_list.header().setDefaultSectionSize(200)
        self.tab_ethernet_list.header().setMinimumSectionSize(200)
        self.gridLayout_6.addWidget(self.tab_ethernet_list, 0, 0, 1, 1)
        self.packetDetail.addTab(self.tab_ethernet, _fromUtf8(""))
        self.tab_ip = QtGui.QWidget()
        self.tab_ip.setObjectName(_fromUtf8("tab_ip"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_ip)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.tab_ip_list = QtGui.QTreeWidget(self.tab_ip)
        self.tab_ip_list.setStyleSheet(_fromUtf8("font: 11pt \"Cantarell\";\n"
"background-color: rgb(52, 52, 52);\n"
"color: rgb(255, 255, 255);"))
        self.tab_ip_list.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tab_ip_list.setRootIsDecorated(False)
        self.tab_ip_list.setAnimated(True)
        self.tab_ip_list.setObjectName(_fromUtf8("tab_ip_list"))
        self.tab_ip_list.header().setVisible(False)
        self.tab_ip_list.header().setDefaultSectionSize(200)
        self.tab_ip_list.header().setMinimumSectionSize(200)
        self.gridLayout_7.addWidget(self.tab_ip_list, 0, 0, 1, 1)
        self.packetDetail.addTab(self.tab_ip, _fromUtf8(""))
        self.tab_protocol = QtGui.QWidget()
        self.tab_protocol.setObjectName(_fromUtf8("tab_protocol"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_protocol)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.tab_protocol_list = QtGui.QTreeWidget(self.tab_protocol)
        self.tab_protocol_list.setStyleSheet(_fromUtf8("font: 11pt \"Cantarell\";\n"
"background-color: rgb(52, 52, 52);\n"
"color: rgb(255, 255, 255);"))
        self.tab_protocol_list.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tab_protocol_list.setRootIsDecorated(False)
        self.tab_protocol_list.setAnimated(True)
        self.tab_protocol_list.setObjectName(_fromUtf8("tab_protocol_list"))
        self.tab_protocol_list.header().setVisible(False)
        self.tab_protocol_list.header().setDefaultSectionSize(200)
        self.tab_protocol_list.header().setMinimumSectionSize(200)
        self.gridLayout_5.addWidget(self.tab_protocol_list, 0, 0, 1, 1)
        self.packetDetail.addTab(self.tab_protocol, _fromUtf8(""))
        self.gridLayout.addWidget(self.packetDetail, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(16, 16))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 850, 29))
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
        self.open_pcap_file = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("img/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_pcap_file.setIcon(icon2)
        self.open_pcap_file.setObjectName(_fromUtf8("open_pcap_file"))
        self.save_as_pcap_file = QtGui.QAction(MainWindow)
        self.save_as_pcap_file.setObjectName(_fromUtf8("save_as_pcap_file"))
        self.exitBtn = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("img/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitBtn.setIcon(icon3)
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.startCaptureBtn)
        self.toolBar.addAction(self.stopCaptureBtn)
        self.toolBar.addAction(self.open_pcap_file)
        self.toolBar.addAction(self.exitBtn)
        self.menuFile.addAction(self.open_pcap_file)
        self.menuFile.addAction(self.save_as_pcap_file)
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
        self.tab_packet_hexdump.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">No packet selected</p></body></html>", None))
        self.packetDetail.setTabText(self.packetDetail.indexOf(self.tab_packet), _translate("MainWindow", "Packet", None))
        self.tab_ethernet_list.headerItem().setText(0, _translate("MainWindow", "Field name", None))
        self.tab_ethernet_list.headerItem().setText(1, _translate("MainWindow", "Value", None))
        self.packetDetail.setTabText(self.packetDetail.indexOf(self.tab_ethernet), _translate("MainWindow", "Ethernet", None))
        self.tab_ip_list.headerItem().setText(0, _translate("MainWindow", "Field name", None))
        self.tab_ip_list.headerItem().setText(1, _translate("MainWindow", "Value", None))
        self.packetDetail.setTabText(self.packetDetail.indexOf(self.tab_ip), _translate("MainWindow", "IP", None))
        self.tab_protocol_list.headerItem().setText(0, _translate("MainWindow", "Field name", None))
        self.tab_protocol_list.headerItem().setText(1, _translate("MainWindow", "Value", None))
        self.packetDetail.setTabText(self.packetDetail.indexOf(self.tab_protocol), _translate("MainWindow", "Protocol", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuCapture.setTitle(_translate("MainWindow", "Capture", None))
        self.startCaptureBtn.setText(_translate("MainWindow", "Start capture", None))
        self.startCaptureBtn.setToolTip(_translate("MainWindow", "Start a new capture", None))
        self.stopCaptureBtn.setText(_translate("MainWindow", "Stop capture", None))
        self.stopCaptureBtn.setToolTip(_translate("MainWindow", "Stop current capture", None))
        self.open_pcap_file.setText(_translate("MainWindow", "Open pcap file", None))
        self.save_as_pcap_file.setText(_translate("MainWindow", "Save as pcap file", None))
        self.exitBtn.setText(_translate("MainWindow", "Exit", None))
        self.exitBtn.setToolTip(_translate("MainWindow", "Exit app", None))

