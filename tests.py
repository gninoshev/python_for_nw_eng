#!/usr/bin/env python

interface = input("Enter interface type and number: ")
vlan = input("Enter VLAN number: ")

access_template = [
    'switchport mode acceess',
    'switchport access vlan {}',
    'switchport nonegotiate',
    'spanning-tree port fast',
    'spanning-tree bpduguard enable'
]