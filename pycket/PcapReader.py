import dpkt
import socket
import network_utils
from packet import Packet


class PcapReader(object):
    """ Classe pour lire un fichier pcap
    Le constructeur prends en parametre le chemin du fichier pcap
    Une liste de Packet est cree a partir du dump """

    def __init__(self, path):
        super(PcapReader, self).__init__()
        self._packets = []
        self._file = None
        self.open_file(path)

    def get_packets(self):
        return self._packets

    def open_file(self, path):
        if self._file is not None:
            self._file.close()
        try:
            self._file = open(path, 'r')
        except IOError, msg:
            print "Error : PcapReader can't open file "+"'"+path+"' : "+str(msg)

    def close_file(self):
        if self._file is not None:
            self._file.close()
            self._file = None

    def parse(self):
        if self._file is None:
            print "Error : PcapReader : Open a file before using parse"
            return
        if self._packets:
            self._packets[:] = []

        # Parsing du fichier via dpkt
        pcap = dpkt.pcap.Reader(self._file)
        for ts, buf in pcap:
            # Parsing des donnees du paquet
            eth = dpkt.ethernet.Ethernet(buf)

            # On ne traite que les paquets IP
            if eth.type != dpkt.ethernet.ETH_TYPE_IP:
                continue

            packet = Packet(buf)
            self._packets.append(packet)
        self.close_file()
