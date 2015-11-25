import dpkt

class PcapWriter(object):
    """ Classe pour ecrire un fichier pcap
    Le constructeur prends en parametre le chemin du fichier pcap """
    def __init__(self, path):
        super(PcapWriter, self).__init__()
        self._file = None
        self.open_file(path)

    def open_file(self, path):
        if self._file is not None:
            self._file.close()
        try:
            self._file = open(path, 'wb+')
        except IOError, msg:
            print "Error : PcapWriter can't open file "+"'"+path+"' : "+str(msg)

    def close_file(self):
        if self._file is not None:
            self._file.close()
            self._file = None

    def write(self, packets):
        if self._file is None:
            print "Error : PcapWriter : Open a file before using write"
            return
        pcapfile = dpkt.pcap.Writer(self._file)
        for packet in packets:
            pcapfile.writepkt(packet.packet)
        self.close_file()
