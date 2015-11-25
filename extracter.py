import sys
import re
from PcapReader import PcapReader

def get_payload_boundaries(http_payload):
    p = []
    for m in re.finditer('Content-Type: image/jpeg', http_payload):
        d = {}
        d['start'] = m.start()
        d['end'] = m.end()
        p.append(d)
    print "Potentially found", len(p), "images"
    return p

def get_http_headers_and_content(http_payload, boundaries):
    p = []
    for i in range(len(boundaries)):
        if i < len(boundaries):
            d = {}
            tmp_payload = http_payload[boundaries[i]['start']:]
            boundaries_end = len(http_payload) - 1
            for m in re.finditer('HTTP/', tmp_payload):
                boundaries_end = boundaries[i]['start'] + m.start()
                break
            headers_raw = http_payload[boundaries[i]['start']:boundaries_end]
            headers = headers_raw.splitlines()
            for h in headers:
                h = h.split(": ")
                if len(h) == 2:
                    if 'Content-Type' in h[0] and 'image/jpeg' in h[1]:
                        d[h[0]] = h[1]
                        d['start'] = boundaries[i]['end']
                        d['end'] = boundaries_end
                        p.append(d)
    if len(p) > 0:
        return p
    return None

def extract_images(headers, http_payload, boundaries):
    image, image_type = None, None

    try:
        if 'image/jpeg' in headers['Content-Type']:
            image_type = headers['Content-Type'].split('/')[1]
            http_payload = http_payload[headers['start']:headers['end']]
            start = headers['start']
            for m in re.finditer('\r\n\r\n', http_payload):
                start = m.end()
                break
            image = http_payload[start:headers['end']]
            try:
                if 'Content-Encoding' in headers.keys():
                    if headers['Content-Encoding'] == 'gzip':
                        image = zlib.decompress(image, 16+zlb.MAX_WBITS)
                    elif headers['Content-Encoding'] == 'deflate':
                        image = zlib.decompress(image)
            except:
                print "Error", sys.exc_info()
    except:
        return None, None
    return image, image_type

def extract(filename):
    http_payload = ''
    PIC_DIR = "extracted_images"
    extracted_images = 1
    pcap = PcapReader(filename)
    pcap.parse()
    for packet in pcap.get_packets():
        if packet.layers[2]:
            if packet.layers[2]['Source port'] == 80 or packet.layers[2]['Destination port'] == 80:
                http_payload += str(packet.layers[2]['Data'])

    boundaries = get_payload_boundaries(http_payload)
    headers = get_http_headers_and_content(http_payload, boundaries)

    clean_name = filename.split('/')
    clean_name = clean_name[len(clean_name) - 1]
    
    if headers:
        for h in headers:
            if 'image/jpeg' in h['Content-Type']:
                image, image_type = extract_images(h, http_payload, boundaries)
                if image is not None and image_type is not None:
                    filename = '%s-pycket_%s.%s' %(clean_name, extracted_images, image_type)
                    fd = open('%s/%s' % (PIC_DIR, filename), 'wb')
                    fd.write(image)
                    fd.close()
                    extracted_images += 1
    return extracted_images
    
if __name__ == '__main__':
    extract(sys.argv[1])
