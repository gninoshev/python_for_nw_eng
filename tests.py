#!/usr/bin/env python

# import dns.resolver
# result = dns.resolver.resolve('google.com', 'A')
#
# for ipval in result:
#     print(ipval.to_text())
#
# print(result.nameserver)

import socket

print(f'The IP is {socket.gethostbyname_ex("google.bg")[2][0]}')
