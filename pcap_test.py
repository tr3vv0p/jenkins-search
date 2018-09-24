from scapy.all import *
import base64

from scapy.layers.inet import UDP

pcap = rdpcap('key.pcap')

str = ''
for pkt in pcap:
    if Raw in pkt:
        str += bytes(pkt[Raw].__str__(), 'utf-8').decode('utf-8')[2]

print(str)
b_dec = base64.b64decode(str[str.index('>:')+2:str.index(':<')])
print(bytes_hex(b_dec).decode('utf-8'))
b_dec = base64.b64decode('TnZGFjo+k4/vaiYaQcTD8sr8vPSh')
print(bytes_hex(b_dec).decode('utf-8'))
b_dec = base64.b64decode('THAWEzhslIntbnBOIpaq')
print(bytes_hex(b_dec).decode('utf-8'))
b_dec = base64.b64decode('FNG8Hf4vzfxRlsrB/Ek/wpWX0xDdECEiKrAKqER/LTAJ3sJ7aco=')
print(bytes_hex(b_dec).decode('utf-8'))
