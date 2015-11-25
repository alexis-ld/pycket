import re
import socket
import string

def mac_address(mac):
    return re.match("[0-9a-f]{2}([:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower())


def ip_address(ip):
    try:
        socket.inet_aton(ip)
        return re.match("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip)
    except:
        return False

# multiple addresses validation at once
def multiple_ip_addresses(ips):
    ips = string.split(ips, '\n')
    for ip in ips:
        print ip
        if not ip_address(ip):
            return False
    return True
