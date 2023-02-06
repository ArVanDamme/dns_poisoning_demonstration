
# This file is part of upstream_dns.

from dnslib import *
import gevent
from gevent.server import DatagramServer
from gevent import socket
from random import randint
from time import sleep

always_respond_ip = '1.2.3.4'

# Class to store DNS records in a cache
class DNSServer(DatagramServer):

    def handle_dns_request(self, data, address):

        request = DNSRecord.parse(data)
        dataName = str(request.q.qname)
        qID = request.header.id

        response = DNSRecord(DNSHeader(qr=1, aa=1, ra=1),
                                     q=DNSQuestion(dataName),
                                     a=RR(dataName, rdata=A(always_respond_ip)))

        response.header.id = qID
        sleep(1.5)
        self.socket.sendto(response.pack(), address)
            

    def handle(self, data, address):

        self.handle_dns_request(data, address)

# Main function
def main():
    DNSServer(':53').serve_forever()


if __name__ == '__main__':
    main()
