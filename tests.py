#!/usr/bin/env python

import dnspython as dns
import dns.resolver

result = dns.resolver.query('google.com', 'A')

print(result)