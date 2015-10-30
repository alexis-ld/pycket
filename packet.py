import sys, time

class Packet(object):
    """docstring for Packet
    classe representant un paquet
    sous forme d'une liste de layers (dictionnaires)
    representant les couches du paquet
    le constructeur prend en parametre le packet renvoye par le socket
    afin d'avoir acces au donnees brutes si besoin"""

    def __init__(self, packet):
        super(Packet, self).__init__()
        # on recupere le paquet brut dans la variable packet pour l'utiliser en hexdump par exemple
        self._packet = packet
        self._layers = []
        self.created = time.clock()

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


    def add_layer(self, toAdd):
        self._layers.append(toAdd)

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
