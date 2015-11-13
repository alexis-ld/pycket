import sys, socket, time, network_utils
# pour convertir les structs C recue sur le reseau en python (fonctions pack et unpack)
from struct import *


class Packet(object):
    """docstring for Packet
    classe representant un paquet
    sous forme d'une liste de layers (dictionnaires)
    representant les couches du paquet
    le constructeur prend en parametre le packet renvoye par le socket
    afin d'avoir acces au donnees brutes si besoin"""

    def __init__(self, packet=None):
        super(Packet, self).__init__()
        # on recupere le paquet brut dans la variable packet pour l'utiliser en hexdump par exemple
        self._packet = packet
        self._layers = []
        self.created = time.clock()
        if self._packet is not None:
            self.parseRaw()

    def packet():
        doc = "Le paquet, compose de plusieurs couches (layers)"
        def fget(self):
            return self._packet
        def fset(self, value):
            self._packet = value
        def fdel(self):
            del self._packet
        return locals()
    packet = property(**packet())

    def layers():
        doc = "Une couche du paquet (Ethernet, Ip, Tcp, ...)."
        def fget(self):
            return self._layers
        def fset(self, value):
            print('This should not be done. Use the add layer method.')
        def fdel(self):
            del self._layers
        return locals()
    layers = property(**layers())

    def add_layer(self, toAdd):
        self._layers.append(toAdd)

    def get_layer(self, layer_type):
        for layer in self._layers:
            if layer['LayerType'].lower() == layer_type.lower():
                return layer
        return None

    def parseRaw(self):
        # Layer a add dans layers
        eth_layer = {}
        eth_layer['LayerType'] = "Ethernet"

        # normalement un header ethernet fait 14 bytes (2 * 6 bytes d'addresses MAC  + l'ethertype ou la taille du payload (2 bytes))
        eth_length = 14
        eth_layer['Header length'] = eth_length

        eth_header = self._packet[:eth_length]

        # on parse la struct C du header
        # ! pour le big endian (reseau) / H unsigned short / s string
        eth = unpack('!6s6sH' , eth_header)

        # on recupere le protocole (ntohs fait la conversion d'Int des bits reseau au bits machine (si differents))
        eth_protocol = socket.ntohs(eth[2])
        eth_layer['Type'] = eth_protocol
        eth_layer['Destination MAC'] = network_utils.eth_addr(self._packet[0:6])
        eth_layer['Source MAC'] = network_utils.eth_addr(self._packet[6:12])

        # On rajoute la couche Ethernet recuperee dans le paquet a ajouter au resultat
        self.add_layer(eth_layer)

        # Parsing des paquets IP (IP Protocol number = 8)
        if eth_protocol == 8 :
            # Layer a add dans self
            ip_layer = {}
            ip_layer['LayerType'] = 'IP'

            # le header IP est sur les 20 premiers bytes apres le header Ethernet
            ip_header = self._packet[eth_length:eth_length+20]

            # on parse la struct C du header IP
            # ! pour le big endian (reseau) / B unsigned char / H unsigned short / s string
            iph = unpack('!2B3H2BH4s4s', ip_header)

            # le premier octet contient la version et la taille du header (RFC 791)
            version_ihl = iph[0]
            # on recupere la version sur les 4 premiers bits
            ip_layer['Version'] = version_ihl >> 4
            # et la taille du header sur les 4 suivants
            ihl = version_ihl & 0xF
            # la taille de IHL est en multiple de 4 (convention)
            iph_length = ihl * 4
            ip_layer['Header length'] = iph_length

            ip_layer['TTL'] = iph[5]
            protocol = iph[6]
            ip_layer['Protocol'] = protocol

            # on converti les adresses IP binaire en leur notation string
            ip_layer['Source Address'] = socket.inet_ntop(socket.AF_INET, iph[8]);
            ip_layer['Destination Address'] = socket.inet_ntop(socket.AF_INET, iph[9]);

            # On rajoute la couche IP recuperee au paquet a rajouter au resultat
            self.add_layer(ip_layer)

            # TCP Protocol ( == 6)
            if protocol == 6 :

                tcp_layer = {}
                tcp_layer['LayerType'] = 'TCP'

                # on recupere le header tcp (20 bytes apres le header IP)
                tcp_header = self._packet[eth_length + iph_length:eth_length + iph_length + 20]

                # on parse la struct C du header tcp
                # ! big endian (reseau) / H unsigned short / L unsigned long / B unsigned char
                tcph = unpack('!2H2L2B3H', tcp_header)

                tcp_layer['Source port'] = tcph[0]
                tcp_layer['Destination port'] = tcph[1]
                tcp_layer['Sequence'] = tcph[2]
                tcp_layer['Acknowledgement'] = tcph[3]
                doff_reserved = tcph[4]
                tcph_length = doff_reserved >> 4
                tcp_layer['Header length'] = tcph_length * 4

                # on add la taille des header pour trouver le debut des data
                h_size = eth_length + iph_length + tcph_length * 4
                data_size = len(self._packet) - h_size

                data = self._packet[h_size:]
                tcp_layer['Data'] = data

                # On rajoute la couche TCP recuperee au paquet a rajouter au resultat
                self.add_layer(tcp_layer)

            #ICMP Protocl (== 1) ce protocole sert a vehiculer les messages d'erreur sur le re"seau
            elif protocol == 1 :

                icmp_layer = {}
                icmp_layer['LayerType'] = 'ICMP'

                u = iph_length + eth_length
                icmph_length = 4
                icmp_header = self._packet[u:u+4]

                icmph = unpack('!BBH' , icmp_header)

                icmp_layer['Type'] = icmph[0]
                icmp_layer['Code'] = icmph[1]
                icmp_layer['Checksum'] = icmph[2]

                h_size = eth_length + iph_length + icmph_length
                data_size = len(self._packet) - h_size

                data = self._packet[h_size:]
                icmp_layer['Data'] = data

                # On rajoute la couche ICMP recuperee au paquet a rajouter au resultat
                self.add_layer(icmp_layer)

            #UDP protocol
            elif protocol == 17 :

                udp_layer = {}
                udp_layer['LayerType'] = 'UDP'

                u = iph_length + eth_length
                udph_length = 8
                udp_header = self._packet[u:u+8]

                udph = unpack('!HHHH' , udp_header)

                udp_layer['Source port'] = udph[0]
                udp_layer['Destination port'] = udph[1]
                udp_layer['Length'] = udph[2]
                udp_layer['Checksum'] = udph[3]

                h_size = eth_length + iph_length + udph_length
                data_size = len(self._packet) - h_size

                data = self._packet[h_size:]
                udp_layer['Data'] = data

                # On rajoute la couche UDP recuperee au paquet a rajouter au resultat
                self.add_layer(udp_layer)

    def to_raw(self):
        ethernet_layer = self.get_layer('Ethernet')
        ip_layer = self.get_layer('IP')
        tcp_layer = self.get_layer('TCP')
        icmp_layer = self.get_layer('ICMP')
        udp_layer = self.get_layer('UDP')
        if ethernet_layer is None or ip_layer is None or (tcp_layer is None and icmp_layer is None and udp_layer is None):
            return None

        packet = None

        # Preparation des donnees du header ethernet
        eth_dst_addr = network_utils.mac_to_eth_addr(ethernet_layer['Destination MAC'])
        eth_src_addr = network_utils.mac_to_eth_addr(ethernet_layer['Source MAC'])
        eth_ethertype = network_utils.int_to_ethertype(ethernet_layer['Type'])
        eth_header = eth_dst_addr + eth_src_addr + eth_ethertype

        # Preparation des donnees du header IP
        ip_ihl = 5  # Internet Header Length
        ip_tos = 0  # Normal delay
        ip_tot_len = 0  # Longueur totale
        ip_id = 420  # Id du paquet
        ip_frag_off = 0  # Offset du fragment
        ip_ttl = ip_layer['TTL']
        ip_proto = ip_layer['Protocol']
        ip_check = 0  # Checksum
        ip_saddr = socket.inet_aton(ip_layer['Source Address'])
        ip_daddr = socket.inet_aton(ip_layer['Destination Address'])
        ip_ihl_ver = (ip_layer['Version'] << 4) + ip_ihl
        ip_header = pack('!BBHHHBBH4s4s', ip_ihl_ver, ip_tos, ip_tot_len, ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check, ip_saddr, ip_daddr)

        if tcp_layer:
            # Preparation des donnees du header TCP
            tcp_source = tcp_layer['Source port']
            tcp_dest = tcp_layer['Destination port']
            tcp_seq = tcp_layer['Sequence']
            tcp_ack_seq = tcp_layer['Acknowledgement']
            tcp_doff = 5  # Data offset
            tcp_window = socket.htons(5840)
            tcp_check = 0  # Checksum
            tcp_urg_ptr = 0  # Urgent pointer
            tcp_offset_res = (tcp_doff << 4) + 0  # Padding
            tcp_flags = 0 + (1 << 1) + (0 << 2) + (0 << 3) + (0 << 4) + (0 << 5)  # Flags: FIN + SYN + RST + PSH + ACK + URG
            tcp_header = pack('!HHLLBBHHH', tcp_source, tcp_dest, tcp_seq, tcp_ack_seq, tcp_offset_res, tcp_flags,  tcp_window, tcp_check, tcp_urg_ptr)

            tcp_user_data = tcp_layer['Data']

            # Preparation du pseudo header TCP
            ph_source_address = socket.inet_aton(ip_layer['Source Address'])
            ph_dest_address = socket.inet_aton(ip_layer['Destination Address'])
            ph_reserved = 0
            ph_protocol = socket.IPPROTO_TCP
            ph_tcp_length = len(tcp_header) + len(tcp_user_data)
            psh = pack('!4s4sBBH', ph_source_address, ph_dest_address, ph_reserved, ph_protocol, ph_tcp_length)
            psh = psh + tcp_header + tcp_user_data
            # Calcul du checksum a l'aide du pseudo header
            tcp_check = network_utils.checksum(psh)

            # On reconstruit le header TCP
            tcp_header = pack('!HHLLBBH', tcp_source, tcp_dest, tcp_seq, tcp_ack_seq, tcp_offset_res, tcp_flags,  tcp_window) + pack('H', tcp_check) + pack('!H', tcp_urg_ptr)
            # On assemble le header IP + le header TCP + les data
            packet = ip_header + tcp_header + tcp_user_data
        elif icmp_layer:
            icmp_type = icmp_layer['Type']
            icmp_code = icmp_layer['Code']
            icmp_check = 0  # Checksum
            icmp_data = icmp_layer['Data']
            # On construit le header icmp temporaire
            icmp_header = pack(">BBH", icmp_type, icmp_code, icmp_check)
            # Calcul du checksum
            icmp_check = network_utils.checksum(icmp_header)
            # On reconstruit le header
            icmp_header = pack(">BBH", icmp_type, icmp_code, icmp_check)
            # On assemble le header ip + le header icmp + les data
            packet = ip_header + icmp_header + icmp_data
        elif udp_layer:
            udp_sport = udp_layer['Source port']
            udp_dport = udp_layer['Destination port']
            udp_data = udp_layer['Data']
            udp_length = 8 + len(udp_data)
            udp_check = 0  # Checksum
            # On construit le header udp temporaire
            udp_header = pack('!HHHH', udp_sport, udp_dport, udp_length, udp_check)

            # Preparation du pseudo header UDP
            ph_source_address = socket.inet_aton(ip_layer['Source Address'])
            ph_dest_address = socket.inet_aton(ip_layer['Destination Address'])
            ph_reserved = 0
            ph_protocol = socket.IPPROTO_UDP
            psh = pack('!4s4sBBH', ph_source_address, ph_dest_address, ph_reserved, ph_protocol, udp_length)
            psh = psh + udp_header + udp_data
            # Calcul du checksum a l'aide du pseudo header
            udp_check = network_utils.checksum(psh)

            # On reconstruit le header UDP
            udp_header = pack('!HHH', udp_sport, udp_dport, udp_length) + pack('H', udp_check)
            # On assemble le header IP + le header UDP + les data
            packet = ip_header + udp_header + udp_data
        # Assemblage du paquet
        if packet is not None:
            ethernet = eth_header + packet
            eth_check = network_utils.checksum(ethernet)
            ethernet = ethernet + pack('H', eth_check)
            self._packet = ethernet
            return ethernet
        return None
