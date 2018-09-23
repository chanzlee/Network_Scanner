#!/usr/bin/env python3

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan(input("Your IP address until socket (ex > 10.0.2.) : ") + "1/24")
