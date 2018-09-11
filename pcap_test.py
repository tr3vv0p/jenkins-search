from scapy.all import *
import base64


pcap = rdpcap('key.pcap')

str = ''
for pkt in pcap:
    if Raw in pkt:
        str += bytes(pkt[Raw].__str__(), 'utf-8').decode('utf-8')[2]

print(str)
b_dec = base64.b64decode(str[str.index('>:')+2:str.index(':<')])
print(bytes_hex(b_dec).decode('utf-8'))

