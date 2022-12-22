#!/usr/bin/env python3
import socket
import dns.resolver

domains = [domain.strip() for domain in open("domains.txt", "r")]

for domain in domains:
    try:
        ip_addr = socket.gethostbyname(domain)
    except:
        ip_addr = 'no'
        answer = dns.resolver.resolve(domain)
        if answer.qname == answer.canonical_name:
            ip_addr += "but active"
    with open("resolved_domains.txt", "a") as f:
        f.write(f"{ip_addr}\n")
        
