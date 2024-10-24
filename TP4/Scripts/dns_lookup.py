from scapy.all import *

def dns_lookup(domain):
    dns_request = IP(dst="1.1.1.1")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=domain))
    response = sr1(dns_request) 
    return response.getlayer(DNS).an.rdata

print(dns_lookup("ynov.com"))
print(dns_lookup("google.com"))
print(dns_lookup("youtube.com"))