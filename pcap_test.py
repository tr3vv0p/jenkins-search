from scapy.all import *
import base64


pcap = rdpcap('key.pcap')

str = ''
for pkt in pcap:
    if Raw in pkt:
        str += bytes(pkt[Raw].__str__(), 'utf-8').decode('utf-8')[2]
            #pkt[Raw].decode("utf-8")

print(str)
print(base64.b64decode('TnZGFjo+k4/vaiYaQcTD8sr8vPSh\THAWEzhslIntbnBOIpaq\FNG8Hf4vzfxRlsrB/Ek/wpWX0xDdECEiKrAKqER/LTAJ3sJ7aco='))

str = '546e5a47466a6f2b6b342f76616959615163544438737238765053685c54484157457a68736c496e74626e424f497061715c464e4738486634767a6678526c7372422f456b2f7770575830784464454345694b72414b7145522f4c54414a33734a3761636f3d'
