import socket


# Convert a string of 6 characters of ethernet address into a dash separated hex string
def eth_addr(a):
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]), ord(a[1]), ord(a[2]), ord(a[3]), ord(a[4]), ord(a[5]))
    return b

# Conversion d'une adresse mac hex string
def mac_to_eth_addr(mac):
    return mac.replace(':', '').decode('hex')

# Conversion d'un int en ethertype hex string
def int_to_ethertype(n):
    n = socket.htons(n)
    s = '%x' % n
    if len(s) & 1:
        s = '0' + s
    return s.decode('hex')

def checksum(msg):
    if len(msg) % 2 == 1:
        msg += '\0'
    s = 0
    for i in range(0, len(msg), 2):
        w = ord(msg[i]) + (ord(msg[i+1]) << 8)
        s = s + w
    s = (s >> 16) + (s & 0xffff)
    s = s + (s >> 16)
    return (~s & 0xffff)
