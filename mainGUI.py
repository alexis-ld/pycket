from PyQt4 import QtGui, QtCore  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication
import lib.hexdump as hexdump
import packetFilter
from PcapReader import PcapReader
import mainWindow  # This file holds our MainWindow and all design related things

import captureThread

from PyQt4.QtCore import SIGNAL



class pycketGUI(QtGui.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        #Action binding
        self.startCaptureBtn.triggered.connect(self.start_capture)
        self.open_pcap_file.triggered.connect(self.open_pcap)
        self.exitBtn.triggered.connect(self.close)

        self.filtersApplyBtn.clicked.connect(self.refresh_list)

        # Variables pour contenir les paquets traites (evite de les stocker sous formes d'objet Qt)
        self.currentPackets = []

        # Counter de nombre de paquets
        self.packetsCounter = 0

        # On bind le clic sur un item de la liste
        self.packetsList.itemSelectionChanged.connect(self.packet_selected)


    def open_pcap(self):
         fileName = QtGui.QFileDialog.getOpenFileName(self, "Open File", "/home", "Pcap files (*.pcap)");
         if fileName:
             try:
                 pcap_reader = PcapReader(fileName)
                 pcap_reader.parse()
                 for packet in pcap_reader.get_packets():
                     self.add_packet(packet)
             except ValueError:
                QtGui.QMessageBox.information(self, "Error", "'"+fileName+"' is not a pcap file.")
             except:
                 print "Unexpected error:", sys.exc_info()[0]

    def start_capture(self):
        print('Starting capture from GUI')
        self.captureThread = captureThread.Capture()

        # On connect le signale add packet a la fonction locale
        self.connect(self.captureThread, SIGNAL("add_packet(PyQt_PyObject)"), self.add_packet)
        # On connect le signal de la fin du thread avec la fonction locale done
        self.connect(self.captureThread, SIGNAL("finished()"), self.done)
        # Signale qui indique que l'user n'a pas les droits suffisants pour capturer des paquets sur le reseau
        self.connect(self.captureThread, SIGNAL("error_user_privilege(QString)"), self.error_user_privilege)
        # On bind le bouton stop
        self.stopCaptureBtn.triggered.connect(self.captureThread.terminate)

        self.stopCaptureBtn.setEnabled(True)
        self.startCaptureBtn.setEnabled(False)

        # On lance la capture
        self.captureThread.start()


    def error_user_privilege(self, msg):
        QtGui.QMessageBox.information(self, "Error", "Your user doesn't have the priviledges required to capture packets.\
        Please check your permissions. "+msg)


    def done(self):
        self.stopCaptureBtn.setEnabled(False)
        self.startCaptureBtn.setEnabled(True)

    def refresh_list(self):
        self.packetsList.clear()
        for packet in self.currentPackets:
            if packetFilter.filterPacket(self.filtersInput.text(), packet):
                item = QtGui.QTreeWidgetItem(self.packetsList)
                item.setText(0, str(packet.created))
                item.setText(1, str(packet.id))
                item.setText(2, str(packet.layers[1]['Source Address']))
                item.setText(3, str(packet.layers[1]['Destination Address']))
                item.setText(4, str(packet.layers[2]['LayerType']))


    def add_packet(self, packetToAdd):
        packetToAdd.id = self.packetsCounter
        self.currentPackets.append(packetToAdd)
        self.packetsCounter += 1

        if packetFilter.filterPacket(self.filtersInput.text(), packetToAdd):
            item = QtGui.QTreeWidgetItem(self.packetsList)
            item.setText(0, str(packetToAdd.created))
            item.setText(1, str(packetToAdd.id))
            item.setText(2, str(packetToAdd.layers[1]['Source Address']))
            item.setText(3, str(packetToAdd.layers[1]['Destination Address']))
            item.setText(4, str(packetToAdd.layers[2]['LayerType']))


    def packet_selected(self):

        # on clear
        self.tab_ethernet_list.clear()
        self.tab_ip_list.clear()
        self.tab_protocol_list.clear()

        # on recupere la selection
        selected = self.packetsList.selectedItems()
        selected = selected[0]

        # on recherche le paquet complet dans currentPackets (le QTreeWidget n'a pas toutes les infos)
        fullPacket = next((packet for packet in self.currentPackets if packet.id == int(selected.text(1))), None)

        # premier onglet (hexdump)
        hexdumpString = hexdump.hexdump(fullPacket.packet, 'return')
        self.tab_packet_hexdump.setText(hexdumpString)

        #deuxieme onglet (ethernet)
        for key,value in fullPacket.layers[0].items() :
            item = QtGui.QTreeWidgetItem(self.tab_ethernet_list)
            item.setText(0, str(key))
            item.setText(1, str(value))

        #troisieme onglet (ip)
        for key,value in fullPacket.layers[1].items() :
            item = QtGui.QTreeWidgetItem(self.tab_ip_list)
            item.setText(0, str(key))
            item.setText(1, str(value))

        #quatrieme onglet (protocole)
        self.packetDetail.setTabText(3, fullPacket.layers[2]['LayerType'])
        for key,value in fullPacket.layers[2].items() :
            item = QtGui.QTreeWidgetItem(self.tab_protocol_list)
            item.setText(0, str(key))
            item.setText(1, str(value))





def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    mainWin = pycketGUI()
    mainWin.show()
    app.exec_()


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
