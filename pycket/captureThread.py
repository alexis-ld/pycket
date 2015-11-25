import socket, sys, time, packet, network_utils

# pour convertir les structs C recue sur le reseau en python (fonctions pack et unpack)
from struct import *

from PyQt4.QtCore import SIGNAL, QThread


class Capture(QThread):
    """ Classe pour capturer les paquets sur le reseau a destination de la GUI
    pour capturer des paquets sans passer par Qt utiliser capture.py """

    def __init__(self):
        super(Capture, self).__init__()
        self._result = []

    def __del__(self):
        self.wait()

    def run(self):
        # creation du socket (0x0003 est defini comme etant ETH_P_ALL en C, tout les paquets ethernet)
        try :
            sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        except socket.error, msg :
            print 'Error : Socket could not be created ['+str(msg[0])+'] : '+msg[1]
            self.emit(SIGNAL('error_user_privilege(QString)'), msg[1])
            self.terminate

        print 'Starting packet capture'
        # Boucle de capture
        while True :

            sockPacket = sock.recvfrom(65565)
            # on recupere uniquement la string
            sockPacket = sockPacket[0]

            packetToAdd = packet.Packet(sockPacket)
            #On emet un signal pour que la GUI recupere le paquet
            self.emit(SIGNAL('add_packet(PyQt_PyObject)'), packetToAdd)


        # Sortie de boucle, la capture a ete arretee
        # On nettoie
        sock.close()
        print 'The capture thread is stopping'
