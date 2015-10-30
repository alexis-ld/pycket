import socket, sys, time, packet

# pour convertir les structs C recue sur le reseau en python (fonctions pack et unpack)
from struct import *

from threading import Thread

class Capture(Thread):
    """ Classe pour capturer les paquets sur le reseau
    elle utilise un thread pour ne pas couper l'execution de la GUI et autres features
    on lance la capture on utilisant .start() et on la stope avec .stopCapture()
    les resultats de la capture seront dans .result() """

    def __init__(self):
        super(Capture, self).__init__()
        self._result = []
        self.shutdown = False

    def result():
        doc = "Le resultat de la capture."
        def fget(self):
            return self._result
        def fset(self, value):
            print('This should not be done. Use start to launch a capture')
        def fdel(self):
            del self._result
        return locals()
    result = property(**result())

    def stopCapture(self):
        print 'Stopping capture'
        self.shutdown = True

    def run(self):
        # On s'assure que la capture n'est pas arretee des le lancement
        self.shutdown = False

        #Convert a string of 6 characters of ethernet address into a dash separated hex string
        def eth_addr (a) :
          b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
          return b

        # creation du socket (0x0003 est defini comme etant ETH_P_ALL en C, tout les paquets ethernet)
        try :
            sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        except socket.error, msg :
            print 'Error : Socket could not be created ['+str(msg[0])+'] : '+msg[1]
            self.shutdown = True

        print 'Starting packet capture'
        # Boucle de capture
        while not self.shutdown :


            sockPacket = sock.recvfrom(65565)
            # on recupere uniquement la string
            sockPacket = sockPacket[0]

            packetToAdd = packet.Packet(sockPacket)

            # Layer a add dans packetToAdd
            eth_layer = {}
            eth_layer['LayerType'] = "Ethernet"

            # normalement un header ethernet fait 14 bytes (2 * 6 bytes d'addresses MAC  + l'ethertype ou la taille du payload (2 bytes))
            eth_length = 14
            eth_layer['Header length'] = eth_length

            eth_header = sockPacket[:eth_length]

            # on parse la struct C du header
            # ! pour le big endian (reseau) / H unsigned short / s string
            eth = unpack('!6s6sH' , eth_header)

            # on recupere le protocole (ntohs fait la conversion d'Int des bits reseau au bits machine (si differents))
            eth_protocol = socket.ntohs(eth[2])
            eth_layer['Type'] = eth_protocol
            eth_layer['Destination MAC'] = eth_addr(sockPacket[0:6])
            eth_layer['Source MAC'] = eth_addr(sockPacket[6:12])

            # On rajoute la couche Ethernet recuperee dans le paquet a ajouter au resultat
            packetToAdd.add_layer(eth_layer)

            # Parsing des paquets IP (IP Protocol number = 8)
            if eth_protocol == 8 :

                # Layer a add dans packetToAdd
                ip_layer = {}
                ip_layer['LayerType'] = 'IP'

                # le header IP est sur les 20 premiers bytes apres le header Ethernet
                ip_header = sockPacket[eth_length:eth_length+20]

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
                packetToAdd.add_layer(ip_layer)

                # TCP Protocol ( == 6)
                if protocol == 6 :

                    tcp_layer = {}
                    tcp_layer['LayerType'] = 'TCP'

                    # on recupere le header tcp (20 bytes apres le header IP)
                    tcp_header = sockPacket[eth_length + iph_length:eth_length + iph_length + 20]

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
                    data_size = len(sockPacket) - h_size

                    data = sockPacket[h_size:]
                    tcp_layer['Data'] = data

                    # On rajoute la couche TCP recuperee au paquet a rajouter au resultat
                    packetToAdd.add_layer(tcp_layer)

                #ICMP Protocl (== 1) ce protocole sert a vehiculer les messages d'erreur sur le re"seau
                elif protocol == 1 :

                    icmp_layer = {}
                    icmp_layer['LayerType'] = 'ICMP'

                    u = iph_length + eth_length
                    icmph_length = 4
                    icmp_header = sockPacket[u:u+4]

                    icmph = unpack('!BBH' , icmp_header)

                    icmp_layer['Type'] = icmph[0]
                    icmp_layer['Code'] = icmph[1]
                    icmp_layer['Checksum'] = icmph[2]

                    h_size = eth_length + iph_length + icmph_length
                    data_size = len(sockPacket) - h_size

                    data = sockPacket[h_size:]
                    icmp_layer['Data'] = data

                    # On rajoute la couche ICMP recuperee au paquet a rajouter au resultat
                    packetToAdd.add_layer(icmp_layer)

                #UDP protocol
                elif protocol == 17 :

                    udp_layer = {}
                    udp_layer['LayerType'] = 'UDP'

                    u = iph_length + eth_length
                    udph_length = 8
                    udp_header = sockPacket[u:u+8]

                    udph = unpack('!HHHH' , udp_header)

                    udp_layer['Source port'] = udph[0]
                    udp_layer['Destination port'] = udph[1]
                    udp_layer['Length'] = udph[2]
                    udp_layer['Checksum'] = udph[3]

                    h_size = eth_length + iph_length + udph_length
                    data_size = len(sockPacket) - h_size

                    data = sockPacket[h_size:]
                    udp_layer['Data'] = data

                    # On rajoute la couche UDP recuperee au paquet a rajouter au resultat
                    packetToAdd.add_layer(udp_layer)

            #On rajoute le paquet au resultat de la capture
            self._result.append(packetToAdd)

        # Sortie de boucle, la capture a ete arretee
        # On nettoie
        sock.close()
        print 'The capture thread is stopping'
