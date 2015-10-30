import sys, capture, time
import lib.hexdump as hexdump


# EXEMPLE D'UTILISATION DE LA CLASSE CAPTURE

test = capture.Capture()

# on lance la capture
test.start()

time.sleep(10)

# on l'arrete
test.stopCapture()
#on attend la fin du thread
test.join()

# on boucle sur les paquets recuperes
for packet in test.result :
    print '\n'+'[PACKET TIMESTAMP] : ', packet.created

    #on boucle sur les layers du paquet
    for layer in packet.layers :
        print
        print 'COUCHE : ', layer['LayerType']
        #on boucle sur les items du layer
        for key, value in layer.items() :
            if key != 'Data' :
                print key, value


    print '\n'
    hexdump.hexdump(packet.packet)
    print '\n'
