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
            # Recuperation des donnees de la couche ethernet
            eth_layer = {}
            eth_layer['LayerType'] = "Ethernet"
            # Un header ethernet fait 14 bytes (2 * 6 bytes d'addresses MAC  + l'ethertype ou la taille du payload (2 bytes))
            eth_layer['Header length'] = 14
            eth_layer['Type'] = socket.ntohs(eth.type)
            eth_layer['Destination MAC'] = network_utils.eth_addr(eth.dst)
            eth_layer['Source MAC'] = network_utils.eth_addr(eth.src)
            packet.add_layer(eth_layer)

            ip = eth.data

            ip_layer = {}
            # Recuperation des donnees de la couche ip
            ip_layer['LayerType'] = 'IP'
            ip_layer['Version'] = ip.v
            ip_layer['Header length'] = ip.hl
            ip_layer['TTL'] = ip.ttl
            ip_layer['Protocol'] = ip.p
            # on converti les adresses IP binaire en leur notation string
            ip_layer['Source Address'] = socket.inet_ntop(socket.AF_INET, ip.src)
            ip_layer['Destination Address'] = socket.inet_ntop(socket.AF_INET, ip.dst)
            # On rajoute la couche IP recuperee au paquet
            packet.add_layer(ip_layer)

            # TCP protocol
            if ip.p == dpkt.ip.IP_PROTO_TCP:
                tcp = ip.data
                # Recuperation des donnees de la couche TCP
                tcp_layer = {}
                tcp_layer['LayerType'] = 'TCP'
                tcp_layer['Source port'] = tcp.sport
                tcp_layer['Destination port'] = tcp.dport
                tcp_layer['Sequence'] = tcp.seq
                tcp_layer['Acknowledgement'] = tcp.ack
                tcp_layer['Header length'] = tcp.off
                tcp_layer['Data'] = tcp.data
                # On rajoute la couche TCP recuperee au paquet
                packet.add_layer(tcp_layer)
            # ICMP protocol
            elif ip.p == dpkt.ip.IP_PROTO_ICMP:
                icmp = ip.data
                # Recuperation des donnees de la couche ICMP
                icmp_layer = {}
                icmp_layer['LayerType'] = 'ICMP'
                icmp_layer['Type'] = icmp.type
                icmp_layer['Code'] = icmp.code
                icmp_layer['Checksum'] = icmp.sum
                icmp_layer['Data'] = icmp.data
                # On rajoute la couche ICMP recuperee au paquet
                packet.add_layer(icmp_layer)
            # UDP protocol
            elif ip.p == dpkt.ip.IP_PROTO_UDP:
                udp = ip.data
                # Recuperation des donnees de la couche UDP
                udp_layer = {}
                udp_layer['LayerType'] = 'UDP'
                udp_layer['Source port'] = udp.sport
                udp_layer['Destination port'] = udp.dport
                udp_layer['Length'] = udp.ulen
                udp_layer['Checksum'] = udp.sum
                udp_layer['Data'] = udp.data
                # On rajoute la couche UDP recuperee au paquet
                packet.add_layer(udp_layer)
            self._packets.append(packet)
        self.close_file()
