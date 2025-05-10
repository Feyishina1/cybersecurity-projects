#!/usr/bin/env python3

from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def process_packet(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        proto = "TCP" if packet.haslayer(TCP) else "UDP" if packet.haslayer(UDP) else "OTHER"
        print(f"[+] {ip_layer.src} --> {ip_layer.dst} | Protocol: {proto}")

def main():
    print("Starting packet sniffer...")
    sniff(filter="ip", prn=process_packet, store=False)

if __name__ == "__main__":
    main()
