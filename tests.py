#!/usr/bin/env python

# result = {}

# with open('sh_ip_int_br.txt') as f:
#     for line in f:
#         line = line.split()
#         if line and line[1][0].isdigit():
#             interface, address, *other = line
#             result[interface] = address

# print(result)


from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))
