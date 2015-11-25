import socket
from packet import Packet


class PacketSender(object):
    """docstring for PacketSender
    classe permettant d'envoyer des paquets"""
    def __init__(self, interface="eth0", port=0):
        super(PacketSender, self).__init__()
        self._interface = interface
        self._port = port
        self._socket = None
        self.connect()

    def __del__(self):
        self._socket.close()

    def connect(self):
        self._socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
        self._socket.bind((self._interface, self._port))

    def send_raw_packet(self, raw):
        return (self._socket.send(raw) == len(raw))

    def send_packet(self, packet):
        raw = packet.to_raw()
        if raw is not None:
            return self.send_raw_packet(raw)
        return False
