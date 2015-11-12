import sys, time

def oneFilterPacket(filt, packet):
    filtLayer = filt[0]
    filtField = filt[1]
    filtValue = filt[2]
    for layer in packet.layers:
        if layer['LayerType'] == filtLayer :
            if layer.has_key(filtField) and layer.get(filtField) == filtValue :
                return True
    return False


def filterPacket(filterStr, packet):
    filters = filterStr.split(',')
    # pas de filtre
    if len(filterStr) == 0:
        return True
    goal = len(filters)
    passed = 0
    for filt in filters:
        filt = str(filt).strip()
        filtParsed = filt.split('/')
        if len(filtParsed) == 3 :
            if oneFilterPacket(filtParsed, packet) :
                passed += 1
        else:
            print 'Invalid filter detected'
            return False
    if passed == goal :
        return True
    return False
